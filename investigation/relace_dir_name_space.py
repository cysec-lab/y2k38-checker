import os
import glob


def replace_spaces(directory_path):
    # 指定されたディレクトリ内のファイルとディレクトリを取得
    entries = os.listdir(directory_path)

    for entry in entries:
        entry_path = os.path.join(directory_path, entry)

        if os.path.isdir(entry_path):
            # サブディレクトリがある場合は再帰的に処理
            replace_spaces(entry_path)

            # スペースをアンダースコアに置換したディレクトリ名を作成
            new_entry = entry.replace(" ", "_")
            new_entry_path = os.path.join(directory_path, new_entry)

            # ディレクトリ名を変更
            os.rename(entry_path, new_entry_path)