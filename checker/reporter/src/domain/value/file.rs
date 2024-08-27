use std::path::Path;

#[derive(Debug, PartialEq)]
pub struct File {
    path: String,
}

impl File {
    pub fn new(path: String) -> Self {
        File { path }
    }
    pub fn path(&self) -> &str {
        &self.path
    }
    pub fn exists(&self) -> bool {
        Path::new(self.path()).exists()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_file() {
        let path = String::from("/path/to/file.txt");
        let file = File::new(path.clone());

        assert_eq!(file.path, path);
    }

    #[test]
    fn test_is_exist() {
        use std::fs;

        let test_file_path = "test_file.txt";
        fs::File::create(test_file_path).expect("Failed to create test file");
        let file = File::new(test_file_path.to_string());

        assert!(file.exists());

        fs::remove_file(test_file_path).expect("Failed to delete test file");
    }
}
