use std::{env, process::exit};
use y2k38_report::{
    analyzer::analysis_workflow_executor::AnalysisWorkflowExecutor, domain::value::file::File,
    y2k38_checker,
};

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Error: Please specify the path to the file you want to check.");
        exit(-1);
    }
    let files = vec![File::new(args[1].clone())];

    use y2k38_checker::clang_plugin_y2k38_checker::ClangPluginY2k38Checker;
    let checker = ClangPluginY2k38Checker {};
    // use y2k38_checker::y2k38_checker_mock::Y2k38CheckerMock;
    // let checker = Y2k38CheckerMock {};

    let mut analysis_workflow_executor = AnalysisWorkflowExecutor::new(files, Box::new(checker));
    analysis_workflow_executor.run();

    for analysis_detail in analysis_workflow_executor.analysis_detail() {
        println!("\n{}", analysis_detail.file().path());
        println!("- category: {:#?}", analysis_detail.y2k38_category());
        println!("- row: {}", analysis_detail.row());
        println!("- column: {}", analysis_detail.column());
    }
}
