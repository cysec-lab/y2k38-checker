import re
from typing import List

from domain.analysis_detail import AnalysisDetail, Y2k38Category
from domain.value.file import File

from .clang_subprocess import run_clang_process


def _check_category(string: str) -> Y2k38Category:
    # Note: 同じ文字列を返しているが、clang toolの出力形式に依存しないために分けている
    if string == "read-fs-timestamp":
        return "read-fs-timestamp"
    elif string == "write-fs-timestamp":
        return "write-fs-timestamp"
    elif string == "timet-to-int-downcast":
        return "timet-to-int-downcast"
    elif string == "timet-to-long-downcast":
        return "timet-to-long-downcast"
    else:
        raise Exception("Invalid y2k38 category")


def _parse_checker_output(checker_output: str) -> List[AnalysisDetail]:
    analysis_detail_list: List[AnalysisDetail] = []

    for line in checker_output.split('\n'):
        # clang-analyzer の出力形式:
        # file.c:3:11: warning: y2k38 (read-fs-timestamp): {description}
        match = re.match(r"^(.+?):(\d+):(\d+): warning: y2k38 \((.+)\)", line)
        if not match:
            continue

        file = File(match.group(1))

        row = match.group(2)
        if not row.isdigit():
            raise Exception(f"row should be digit: {row}")
        row = int(row)

        column = match.group(3)
        if not column.isdigit():
            raise Exception(f"column should be digit: {column}")
        column = int(column)

        category = _check_category(match.group(4))

        analysis_detail_list.append(
            AnalysisDetail(y2k38_category=category, file=file, row=row, column=column)
        )

    return analysis_detail_list


def run_clang(file: File, is_stdout: bool = False) -> List[AnalysisDetail]:
    output = run_clang_process(file.get_path())
    if is_stdout:
        print(output)

    return _parse_checker_output(output)
