use crate::{
    domain::{analysis::Analysis, analysis_detail::AnalysisDetail, value::file::File},
    y2k38_checker::y2k38_checker_trait::Y2k38Checker,
};

use super::timer::Timer;

pub struct AnalysisWorkflowExecutor {
    files: Vec<File>,
    analysis: Analysis,
    analysis_detail: Vec<AnalysisDetail>,
    y2k38_checker: Box<dyn Y2k38Checker>,
}

impl AnalysisWorkflowExecutor {
    pub fn new(files: Vec<File>, y2k38_checker: Box<dyn Y2k38Checker>) -> Self {
        AnalysisWorkflowExecutor {
            files: files,
            analysis: Analysis::new(),
            analysis_detail: Vec::new(),
            y2k38_checker: y2k38_checker,
        }
    }

    pub fn run(&mut self) {
        let mut timer = Timer::new();
        timer.start();

        let analysis_detail_list: Vec<AnalysisDetail> = self
            .files
            .iter()
            .flat_map(|file| run_checker(file, &*self.y2k38_checker))
            .collect();

        self.analysis_detail = analysis_detail_list;

        timer.stop();
        self.analysis.set_processing_time(timer.time());
    }

    pub fn files(&self) -> &Vec<File> {
        &self.files
    }
    pub fn analysis(&self) -> &Analysis {
        &self.analysis
    }
    pub fn analysis_detail(&self) -> &Vec<AnalysisDetail> {
        &self.analysis_detail
    }
}

fn run_checker(file: &File, y2k38_checker: &dyn Y2k38Checker) -> Vec<AnalysisDetail> {
    let result = y2k38_checker.run(file, false);
    if result.is_ok() {
        return result.unwrap();
    } else {
        println!("run_checker: {:?}", result.err());
        return Vec::new();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::y2k38_checker::clang_plugin_y2k38_checker::ClangPluginY2k38Checker;

    #[test]
    fn test_run() {
        let file = File::new(String::from(
            "/root/y2k38-checker/dataset/blacklist/read-fs-timestamp.c",
        ));
        let checker = ClangPluginY2k38Checker {};
        let mut executor = AnalysisWorkflowExecutor::new(vec![file], Box::new(checker));
        executor.run();

        assert!(executor.analysis_detail().len() > 0);
    }
}
