import os
import sys
from typing import List, TypedDict
from dotenv import load_dotenv

from .analyzer.analysis_workflow_executor import AnalysisWorkflowExecutor
from .repository.repository import AnalysisRepository, AnalysisDetailRepository

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
                    os.environ["ANALYSIS_OBJECTS"], name, "compile_commands.json"
                )
            })

    # 解析結果を記録用の Repository を用意する
    analysis_repository = AnalysisRepository()
    analysis_detail_repository = AnalysisDetailRepository()

    # 解析器を用意する
    analyzer = AnalysisWorkflowExecutor()

    # 解析対象のリポジトリを走査する
    for analysis_object in analysis_object_list:
        print(analysis_object)

        analyzer.run(
            name=analysis_object["name"],
            compile_json_path=analysis_object["compile_commands"]
        )
        analysis_repository.insert(analyzer.get_analysis())
        analysis_detail_repository.bulk_insert(analyzer.get_analysis_detail())

    # 解析結果をログファイルに書き込む
    analysis_repository.write_out(path=os.environ["ANALYSIS_LOG_PATH"])
    analysis_detail_repository.write_out(path=os.environ["ANALYSIS_DETAIL_LOG_PATH"])


if __name__ == '__main__':
    main()
