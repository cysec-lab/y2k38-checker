import unittest
from unittest.mock import MagicMock
import textwrap

from domain.analysis_detail import AnalysisDetail
from domain.value.file import File

from . import clang_static_analyzer

file = "../../../dataset/blacklist/read-fs-timestamp.c"


class TestClangStaticAnalyzer(unittest.TestCase):
    def assert_analysis_detail(self, actual: AnalysisDetail, expect: AnalysisDetail):
        self.assertEqual(actual.y2k38_category, expect.y2k38_category)
        self.assertEqual(actual.file.get_path(), expect.file.get_path())
        self.assertEqual(actual.row, expect.row)
        self.assertEqual(actual.column, expect.column)

    def test_run_clang(self):
        clang_static_analyzer.run_clang_process = MagicMock(return_value=textwrap.dedent(f"""
            {file}:4:11: warning: y2k38 (write-fs-timestamp): description
            {file}:54:15: warning: y2k38 (timet-to-int-downcast): description
        """))

        accepted = clang_static_analyzer.run_clang(File(file))

        expect = [
            AnalysisDetail("write-fs-timestamp", file=File(file), row=4, column=11),
            AnalysisDetail("timet-to-int-downcast", file=File(file), row=54, column=15),
        ]

        self.assertEqual(len(accepted), 2)
        self.assert_analysis_detail(accepted[0], expect[0])
        self.assert_analysis_detail(accepted[1], expect[1])
