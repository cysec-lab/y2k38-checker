use std::io;

use crate::domain::analysis_detail::AnalysisDetail;
use crate::domain::value::file::File;

pub trait Y2k38Checker {
    fn health_check(&self) -> bool;
    fn run(&self, file: &File, is_stdout: bool) -> Result<Vec<AnalysisDetail>, io::Error>;
}
    