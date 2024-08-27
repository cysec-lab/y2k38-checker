use std::io;

use crate::domain::{
    analysis_detail::AnalysisDetail, types::y2k38_category::Y2k38Category, value::file::File,
};

use super::y2k38_checker_trait::Y2k38Checker;

pub struct Y2k38CheckerMock {}

impl Y2k38Checker for Y2k38CheckerMock {
    fn run(&self, _file: &File, is_stdout: bool) -> Result<Vec<AnalysisDetail>, io::Error> {
        if is_stdout {
            println!("Y2k38CheckerMock run");
        }
        Ok(vec![AnalysisDetail::new(
            Y2k38Category::ReadFsTimestamp,
            File::new("path/to/file.txt".to_string()),
            1,
            2,
        )])
    }

    fn health_check(&self) -> bool {
        true
    }

    fn name(&self) -> String {
        "Y2k38CheckerMock".to_string()
    }

    fn description(&self) -> Vec<String> {
        vec!["mock".to_string()]
    }
}
