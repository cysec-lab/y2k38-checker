pub mod analyzer {
    pub mod analysis_workflow_executor;
    pub mod timer;
}
pub mod y2k38_checker {
    pub mod clang_plugin_y2k38_checker;
    pub mod y2k38_checker_trait;
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
