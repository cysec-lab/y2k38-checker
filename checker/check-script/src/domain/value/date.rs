use chrono::prelude::Utc;

#[derive(Debug, PartialEq)]
pub struct Date {
    date: String,
}

impl Date {
    pub fn new() -> Self {
        let now = Utc::now();
        let formatted = now.format("%Y-%m-%d %H:%M:%S").to_string();
        Date { date: formatted }
    }

    pub fn date(&self) -> &str {
        &self.date
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_date() {
        let date = Date::new();
        assert_eq!(date.date.len(), "YYYY-MM-DD HH:MM:SS".len());
    }
}
