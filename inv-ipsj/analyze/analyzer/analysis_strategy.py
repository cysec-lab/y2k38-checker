import os
from typing import List
from dotenv import load_dotenv

from .clang_static_analyzer import run_clang
from .parse_checker_output import parse_checker_output
from domain.analysis_detail import AnalysisDetail

load_dotenv("../.env")


def parse(result: str, analysis_id: str) -> List[AnalysisDetail]:
    # 出力をパース
    parsed_result_list = parse_checker_output(result)

    # 解析結果を AnalysisDetail のリストに変換
    return [
        AnalysisDetail(analysis_id, parsed["category"], parsed["path"])
        for parsed in parsed_result_list
    ]

def analyze_timet_to_int(compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
    result = run_clang(compile_json_path, os.environ["CSA_PLUGIN_PATH_TIMET_TO_INT"])
    return parse(result, analysis_id)

def analyze_timet_to_long(compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
    result = run_clang(compile_json_path, os.environ["CSA_PLUGIN_PATH_TIMET_TO_LONG"])
    return parse(result, analysis_id)

def analyze_read_fs_timestamp(compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
    result = run_clang(compile_json_path, os.environ["CSA_PLUGIN_PATH_READ_FS_TIMESTAMP"])
    return parse(result, analysis_id)

def analyze_write_fs_timestamp(compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
    result = run_clang(compile_json_path, os.environ["CSA_PLUGIN_PATH_WRITE_FS_TIMESTAMP"])
    return parse(result, analysis_id)

if __name__ == "__main__":
    compile_json_path = os.path.join(os.environ["ANALYSIS_OBJECTS"], "y2k38-checker", "compile_commands.json")
    print(analyze_timet_to_int(compile_json_path, "1"))
    print(analyze_timet_to_long(compile_json_path, "2"))
    print(analyze_read_fs_timestamp(compile_json_path, "3"))
    print(analyze_write_fs_timestamp(compile_json_path, "4"))