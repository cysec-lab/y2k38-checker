from abc import ABCMeta, abstractmethod
import os
from typing import List
from dotenv import load_dotenv

from .clang_static_analyzer import run_clang
from .parse_checker_output import parse_checker_output
from ..domain.analysis_detail import AnalysisDetail

load_dotenv("../.env")


class AnalysisStrategy(metaclass=ABCMeta):
    @abstractmethod
    def analyze(self, compile_json_path: str):
        pass


class ReadFsTimestampStrategy(AnalysisStrategy):
    def analyze(self, compile_json_path: str) -> str:
        return run_clang(compile_json_path, plugin_path=os.environ["CSA_PLUGIN_PATH_READ_FS_TIMESTAMP"])


class WriteFsTimestampStrategy(AnalysisStrategy):
    def analyze(self, compile_json_path: str) -> str:
        return run_clang(compile_json_path, plugin_path=os.environ["CSA_PLUGIN_PATH_WRITE_FS_TIMESTAMP"])


class TimetToIntDowncastStrategy(AnalysisStrategy):
    def analyze(self, compile_json_path: str) -> str:
        return run_clang(compile_json_path, plugin_path=os.environ["CSA_PLUGIN_PATH_TIMET_TO_INT"])


class TimetToLongDowncastStrategy(AnalysisStrategy):
    def analyze(self, compile_json_path: str) -> str:
        return run_clang(compile_json_path, plugin_path=os.environ["CSA_PLUGIN_PATH_TIMET_TO_LONG"])


class AnalysisContext:
    def __init__(
        self,
        strategy: AnalysisStrategy,
    ) -> List[AnalysisDetail]:
        self.strategy: AnalysisStrategy = strategy

    def operation(self, compile_json_path: str, analysis_id: AnalysisDetail["analysis_id"]) -> List[AnalysisDetail]:
        # 解析を実行
        result = self.strategy.analyze(compile_json_path)

        # 出力をパース
        parsed_result_list = parse_checker_output(result)

        analysis_detail_list: List[AnalysisDetail] = [
            AnalysisDetail(analysis_id, parsed["category"], parsed["path"])
            for parsed in parsed_result_list
        ]

        return analysis_detail_list
