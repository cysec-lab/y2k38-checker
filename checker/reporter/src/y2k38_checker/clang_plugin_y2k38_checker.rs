use regex::Regex;
use std::io;
use std::process::{Command, Output, Stdio};

use crate::domain::{
    analysis_detail::AnalysisDetail, types::y2k38_category::Y2k38Category, value::file::File,
};

use super::y2k38_checker_trait::Y2k38Checker;

const CLANG_PATH: &str =
    "/root/y2k38-checker/checker/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang";
const PLUGIN_PATH: &str = "/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so";

pub struct ClangPluginY2k38Checker {}

impl Y2k38Checker for ClangPluginY2k38Checker {
    fn health_check(&self) -> bool {
        let output = Command::new(CLANG_PATH)
            .arg("--version")
            .output()
            .expect("Failed to run clang --version");
        output.status.success()
    }

    fn run(&self, file: &File, is_stdout: bool) -> Result<Vec<AnalysisDetail>, io::Error> {
        let output = run_clang_process(file);

        match output {
            Ok(stderr_output) => {
                if is_stdout {
                    println!("Clang Output:{}", stderr_output);
                }
                return Ok(parse_clang_output(&stderr_output));
            }
            Err(e) => {
                return Err(e);
            }
        }
    }

    fn name(&self) -> String {
        "ClangPluginY2k38Checker".to_string()
    }
    fn description(&self) -> Vec<String> {
        vec![
            format!("clang path: {}", CLANG_PATH),
            format!("plugin path: {}", PLUGIN_PATH),
        ]
    }
}

fn run_clang_process(file: &File) -> Result<String, io::Error> {
    let cmd = [
        CLANG_PATH,
        "-w",
        &format!("-fplugin={}", PLUGIN_PATH),
        "-c",
        file.path(),
    ];

    let output: Output = Command::new(cmd[0])
        .args(&cmd[1..])
        .stderr(Stdio::piped()) // 標準エラーをキャプチャ
        .output()?; // コマンドを実行

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stderr).to_string())
    } else {
        Err(io::Error::new(
            io::ErrorKind::Other,
            format!(
                "Failed to run clang: {}",
                String::from_utf8_lossy(&output.stderr)
            ),
        ))
    }
}

fn parse_clang_output(output: &str) -> Vec<AnalysisDetail> {
    let mut analysis_details: Vec<AnalysisDetail> = Vec::new();

    for line in output.lines() {
        // clang-analyzer の出力形式:
        // file.c:3:11: warning: y2k38 (read-fs-timestamp): {description}
        let re = Regex::new(r"^(.+?):(\d+):(\d+): warning: y2k38 \((.+)\)").unwrap();
        if let Some(captures) = re.captures(line) {
            let parsed1 = &captures[1].to_string();
            let file = File::new(parsed1.clone());
            file.is_exist();

            let parsed2 = &captures[2];
            let row = parsed2.parse::<u32>().unwrap();

            let parsed3 = &captures[3];
            let column = parsed3.parse::<u32>().unwrap();

            let parsed4 = &captures[4];
            let category = to_y2k38_category_enum(parsed4);

            let analysis_detail = AnalysisDetail::new(category, file, row, column);
            analysis_details.push(analysis_detail);
        }
    }
    analysis_details
}

fn to_y2k38_category_enum(category: &str) -> Y2k38Category {
    match category {
        "read-fs-timestamp" => Y2k38Category::ReadFsTimestamp,
        "write-fs-timestamp" => Y2k38Category::WriteFsTimestamp,
        "timet-to-int-downcast" => Y2k38Category::TimetToIntDowncast,
        "timet-to-long-downcast" => Y2k38Category::TimetToLongDowncast,
        _ => Y2k38Category::Unknown,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_clang_output() {
        let output = "path/to/file.c:3:11: warning: y2k38 (read-fs-timestamp): {description}\n";
        let analysis_details = parse_clang_output(output);

        assert_eq!(analysis_details.len(), 1);
        assert_eq!(
            analysis_details[0].y2k38_category(),
            &Y2k38Category::ReadFsTimestamp
        );
        assert_eq!(analysis_details[0].file().path(), "path/to/file.c");
        assert_eq!(analysis_details[0].row(), 3);
        assert_eq!(analysis_details[0].column(), 11);
    }

    #[test]
    fn test_to_y2k38_category_enum() {
        assert_eq!(
            to_y2k38_category_enum("read-fs-timestamp"),
            Y2k38Category::ReadFsTimestamp
        );
        assert_eq!(
            to_y2k38_category_enum("write-fs-timestamp"),
            Y2k38Category::WriteFsTimestamp
        );
        assert_eq!(
            to_y2k38_category_enum("timet-to-int-downcast"),
            Y2k38Category::TimetToIntDowncast
        );
        assert_eq!(
            to_y2k38_category_enum("timet-to-long-downcast"),
            Y2k38Category::TimetToLongDowncast
        );
        assert_eq!(to_y2k38_category_enum("hoge"), Y2k38Category::Unknown);
    }

    #[test]
    fn test_run_clang_process() {
        let file = File::new(String::from(
            "/root/y2k38-checker/dataset/blacklist/read-fs-timestamp.c",
        ));
        let output = run_clang_process(&file);
        assert!(output.is_ok());
    }

    #[test]
    fn test_health_check() {
        let checker = ClangPluginY2k38Checker {};
        assert!(checker.health_check());
    }

    #[test]
    fn test_run() {
        let file = File::new(String::from(
            "/root/y2k38-checker/dataset/blacklist/read-fs-timestamp.c",
        ));
        let checker = ClangPluginY2k38Checker {};
        let result = checker.run(&file, false);
        assert!(result.unwrap().len() > 0);
    }
}
