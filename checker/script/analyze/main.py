# checkerは ../build/bin/check-y2k38 にある実行形式ファイル

from dotenv import load_dotenv
from typing import List, TypedDict, Dict, Union, Literal
import glob
import json
import os
import sys
import textwrap
import time
import argparse


from analyzer.analysis_workflow_executor import AnalysisWorkflowExecutor
from repository.repository import AnalysisRepository, AnalysisDetailRepository

load_dotenv("../.env")


def parse_args() -> Dict[Literal["is_consent"], bool]:
    if len(sys.argv) == 1:
        print("Error: No arguments specified")
        exit()

    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', required=False, help='')
    parser.add_argument("--version", "-v", action="store_true", help="Display version", )
    parser.add_argument("--consent", required=True, choices=["Yes", "No"], help="If  Agree to the use of analysis results in our research (Yes/No)")
    args: Dict[] = parser.parse_args()

    if args.version:
        print("Version: 0.0.1")
        exit()


    if args.consent is None:
        print("Error: --consent is required")
        exit()

    if args.arg1 is not None and not isinstance(args["arg1"], str):
        raise ValueError("Error: arg1 must be a string")

    return {
        "arg1": args.arg1,
        "is_consent": args.consent == "Yes"
    }


def main():
    args = parse_args()
    input_paths: List[str] = glob.glob(args["input_path"], recursive=True)
    print(input_paths, )

    # compile_commands.json を作成する
    compile_commands_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "tmp",
        "compile_commands.json"
    )
    with open(compile_commands_path, 'w+') as file:
        data = [{"file": os.path.join(os.getcwd(), path)} for path in input_paths]
        json.dump(data, file)

   # 解析を実行する
    analyzer = AnalysisWorkflowExecutor(
        name=time.strftime("%Y-%m-%dT%H-%M-%S"),
        compile_json_path=compile_commands_path
    )
    analyzer.run()

    # 解析結果を記録する
    results = {}
    for analysis_detail in analyzer.get_analysis_detail_list():
        results[analysis_detail.get_analysis_id()] = {
            "id": analysis_detail.get_analysis_id(),
            "y2k38_category": analysis_detail.get_y2k38_category(),
            "path": analysis_detail.get_path()
        }
    if args["output_path"] is None:
        print(results)
    else:
        with open(args["output_path"], 'w+') as file:
            json.dump(analyzer.get_analysis_detail_list(), results)


if __name__ == '__main__':
    main()
