from typing import List
import sys
import json

from analyzer.analysis_workflow_executor import AnalysisWorkflowExecutor
from repository.client import Client
from domain.value.file import File


def parse_args() -> List[str]:
    args = sys.argv
    if len(args) < 2:
        raise ValueError("Error: No arguments specified")

    return args[1:]


def is_consent() -> bool:
    with open("./experimental_consent.txt", "r") as f:
        consent_text = f.read()
    print(consent_text)
    print("If you agree to the above, please enter 'y'.")
    consent = input()

    return consent == "y"


def main():
    args = parse_args()
    files = [File(arg) for arg in args]

   # 解析を実行する
    analyzer = AnalysisWorkflowExecutor(files)
    analyzer.run()

    # 解析結果を記録する
    if is_consent():
        # FIXME: OpenAPI 仕様書通りかを検証したい
        request_body = {
            "date": analyzer.get_analysis().get_date().get_date(),
            "count": analyzer.get_analysis().get_count_files(),
            "processing_time": analyzer.get_analysis().get_processing_time(),
            "analysis_detail_list": [{
                "category": detail.get_y2k38_category(),
                "path": detail.get_file().get_path(),
                "row": detail.get_row(),
                "column": detail.get_column()
            } for detail in analyzer.get_analysis_detail_list()]
        }
        client = Client()
        client.send_to_server(json.dumps(request_body))
        print("The analysis result has been sent to the server. Thank you for your cooperation.")


if __name__ == '__main__':
    main()
