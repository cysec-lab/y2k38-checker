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

use analyzer::analysis_workflow_executor::AnalysisWorkflowExecutor;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Error: Please specify the path to the file you want to check.");
        return;
    }

    let files = vec![domain::value::file::File::new(args[1].clone())];
    let checker = y2k38_checker::clang_plugin_y2k38_checker::ClangPluginY2k38Checker {};

    let mut analysis_workflow_executor = AnalysisWorkflowExecutor::new(files, Box::new(checker));
    analysis_workflow_executor.run();

    for analysis_detail in analysis_workflow_executor.analysis_detail() {
        println!("\n{}", analysis_detail.file().path());
        println!("- category: {:#?}", analysis_detail.y2k38_category());
        println!("- row: {}", analysis_detail.row());
        println!("- column: {}", analysis_detail.column());
    }
}
