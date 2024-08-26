use crate::domain::value::date::Date;

#[derive(Debug)]
pub struct Analysis {
    date: Date,
    processing_time: Option<f64>,
    count_files: Option<u32>,
}

impl Analysis {
    pub fn new() -> Self {
        Analysis {
            date: Date::new(),
            processing_time: None,
            count_files: None,
        }
    }

    pub fn date(&self) -> &Date {
        &self.date
    }

    pub fn set_processing_time(&mut self, processing_time: f64) {
        self.processing_time = Some(processing_time);
    }
    pub fn processing_time(&self) -> Option<f64> {
        self.processing_time
    }

    pub fn set_count_files(&mut self, count_files: u32) {
        self.count_files = Some(count_files);
    }
    pub fn count_files(&self) -> Option<u32> {
        self.count_files
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_analysis() {
        let analysis = Analysis::new();
        assert!(analysis.date.date().len() > 0);
        assert_eq!(analysis.processing_time, None);
        assert_eq!(analysis.count_files, None);
    }

    #[test]
    fn test_set_processing_time() {
        let mut analysis = Analysis::new();
        analysis.set_processing_time(0.5);
        assert_eq!(analysis.processing_time, Some(0.5));
    }

    #[test]
    fn test_set_count_files() {
        let mut analysis = Analysis::new();
        analysis.set_count_files(10);
        assert_eq!(analysis.count_files, Some(10));
    }
}
