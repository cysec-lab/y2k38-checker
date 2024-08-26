use super::{types::y2k38_category::Y2k38Category, value::file::File};

#[derive(Debug)]
pub struct AnalysisDetail {
    y2k38_category: Y2k38Category,
    file: File,
    row: u32,
    column: u32,
}

impl AnalysisDetail {
    pub fn new(y2k38_category: Y2k38Category, file: File, row: u32, column: u32) -> Self {
        AnalysisDetail {
            y2k38_category,
            file,
            row,
            column,
        }
    }

    pub fn y2k38_category(&self) -> &Y2k38Category {
        &self.y2k38_category
    }
    pub fn file(&self) -> &File {
        &self.file
    }
    pub fn row(&self) -> u32 {
        self.row
    }
    pub fn column(&self) -> u32 {
        self.column
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_analysis_detail() {
        let file = File::new(String::from("file.txt"));
        let analysis_detail = AnalysisDetail::new(Y2k38Category::ReadFsTimestamp, file, 1, 2);

        assert_eq!(
            analysis_detail.y2k38_category(),
            &Y2k38Category::ReadFsTimestamp
        );
        assert_eq!(analysis_detail.file().path(), "file.txt");
        assert_eq!(analysis_detail.row, 1);
        assert_eq!(analysis_detail.column, 2);
    }
}
