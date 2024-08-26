use std::io;

use crate::domain::analysis_detail::AnalysisDetail;
use crate::domain::value::file::File;

pub trait Y2k38Checker {
    fn run(&self, file: &File, is_stdout: bool) -> Result<Vec<AnalysisDetail>, io::Error>;

    fn health_check(&self) -> bool;
    fn name(&self) -> String;
    fn description(&self) -> Vec<String>;
}
