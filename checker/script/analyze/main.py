from typing import List
import sys

from analyzer.analysis_workflow_executor import AnalysisWorkflowExecutor
from domain.value.file import File


def parse_args() -> List[str]:
    args = sys.argv
    if len(args) < 2:
        raise ValueError("No arguments specified: main.py [file1]")

    return args[1:]

def main():
    args = parse_args()
    files = [File(arg) for arg in args]

   # 解析を実行する
    analyzer = AnalysisWorkflowExecutor(files)
    analyzer.run()

    analysis = analyzer.get_analysis()
    print("file count: ", analysis.get_count_files())
    print("time: ", analysis.get_processing_time())
    print("date: ", analysis.get_date())
    print("====================================================")
    for detail in analyzer.get_analysis_detail_list():
        print(
            detail.get_y2k38_category().ljust(23), 
            f"{detail.get_file().get_path()}:{detail.get_row()}:{detail.get_column()}")

if __name__ == '__main__':
    main()
