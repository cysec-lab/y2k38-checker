"""
概要: 解析対象のリポジトリを走査し、解析結果を記録する
前提: 
    - {os.environ["ANALYSIS_LOG_PATH"]}/{repo}/compile_commands.json に解析対象のファイルパスが記録されている
    - {os.environ["ANALYSIS_LOG_PATH"]} のCSVファイルが存在する
    - {os.environ["ANALYSIS_DETAIL_LOG_PATH"]} には、それぞれ解析結果を記録するためのディレクトリが存在する
"""

import os
import sys
from typing import List, TypedDict
from dotenv import load_dotenv
import time

from analyzer.analysis_workflow_executor import AnalysisWorkflowExecutor
from repository.repository import AnalysisRepository, AnalysisDetailRepository

load_dotenv("../.env")


def main():
    class AnalysisObject(TypedDict):
        name: str
        compile_commands: str

    target_file = sys.argv[1]

    # 解析対象のリポジトリ名のリストを用意する
    analysis_object_list: List[AnalysisObject] = []
    with open(target_file, 'r') as file:
        for line in file:
            if line == "":
                continue

            name = line.rstrip()
            analysis_object_list.append({
                "name": name,
                "compile_commands": os.path.join(
                    os.environ["ANALYSIS_OBJECTS"], name.replace("/", "__"), "compile_commands.json"
                )
            })
    print(analysis_object_list)

    # 解析結果を記録用の Repository を用意する
    analysis_repository = AnalysisRepository()
    analysis_detail_repository = AnalysisDetailRepository()

    # 解析対象のリポジトリを走査する
    for analysis_object in analysis_object_list:
        print("analyzing", analysis_object)

        analyzer = AnalysisWorkflowExecutor(
            name=analysis_object["name"],
            compile_json_path=analysis_object["compile_commands"]
        )
        analyzer.run()

        analysis_repository.insert(analyzer.get_analysis())
        analysis_detail_repository.bulk_insert(analyzer.get_analysis_detail_list())

    print("analyzed:", [analysis.get_name() for analysis in analysis_repository.get_analysis_list()])
    print("found at:", [analysis_detail.get_path() for analysis_detail in analysis_detail_repository.get_analysis_detail_list()])

    # 解析結果をログファイルに書き込む
    analysis_repository.write_out(path=os.environ["ANALYSIS_LOG_PATH"])
    analysis_detail_repository.write_out(path=os.path.join(
        os.environ["ANALYSIS_DETAIL_LOG_DIR"],
        time.strftime("%Y-%m-%dT%H-%M-%S") + ".csv"
    )),


if __name__ == '__main__':
    main()
