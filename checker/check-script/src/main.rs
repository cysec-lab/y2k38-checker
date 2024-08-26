pub mod analyzer {
    pub mod timer;
}
pub mod domain {
    pub mod analysis;
    pub mod analysis_detail;
    pub mod value {
        pub mod date;
        pub mod file;
    }
    pub mod types {
        pub mod y2k38_category;
    }
}

fn main() {
    println!("Hello, world!");
}
