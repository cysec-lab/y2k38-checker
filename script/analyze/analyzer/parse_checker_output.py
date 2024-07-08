import re
from typing import List, TypedDict


class ParsedResult(TypedDict):
    category: str
    path: str


def parse_checker_output(checker_output: str) -> List[ParsedResult]:
    """
    checker_output: checkerの出力結果
    return: パスのリスト, [{category: str, path: str}, ...]

    clang-analyzer の出力形式は以下。
    [category1] path/to/file1
    [category2] path/to/file2
    [category3] path/to/file3
    """

    result_list: List[ParsedResult] = []
    for line in checker_output.split('\n'):
        if line == "":
            continue

        match = re.match(r'\[(.+?)\] (.*)', line)
        if match:
            result: ParsedResult = {
                'category': match.group(1),
                'path': match.group(2)
            }
            result_list.append(result)

    return result_list
