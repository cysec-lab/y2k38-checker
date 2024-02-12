import unittest
import subprocess
import path


class MyTestCase(unittest.TestCase):
    maxDiff = None

    def assert_std_err(self, stderr: str):
        self.assertEqual(stderr, "", f"std error: {stderr}")

    def assert_std_out(self, stdout: str, expected: str):
        self.assertEqual(stdout, expected, f"std output: {stdout}")


class Test_ファイルタイムスタンプへの書き込み(MyTestCase):
    def test(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_WRITE_FS_TIMESTAMP, "-c", path.DATASET_PATHS_WRITE_FS_TIMESTAMP]
        expected = "".join([
            f"[write-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/write-fs-timestamp.c:10:5\n",
            f"[write-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/write-fs-timestamp.c:11:5\n",
            f"[write-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/write-fs-timestamp.c:17:5\n",
            f"[write-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/write-fs-timestamp.c:18:5\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)


class Test_ファイルタイムスタンプからの読み込み(MyTestCase):
    def test(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_READ_FS_TIMESTAMP, "-c", path.DATASET_PATHS_READ_FS_TIMESTAMP]
        expected = "".join([
            f"[read-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/read-fs-timestamp.c:9:25\n",
            f"[read-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/read-fs-timestamp.c:10:25\n",
            f"[read-fs-timestamp] {path.REPOSITORY_PATH}/dataset/blacklist/read-fs-timestamp.c:11:25\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)


class Test_time_tからintへのキャスト(MyTestCase):

    def test_明示的キャスト(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_INT, "-c", path.DATASET_PATHS_EXP_DOWNCAST]
        expected = "".join([
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:18:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:19:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:20:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:21:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:22:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:23:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:24:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:25:20\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/exp-downcast.c:26:20\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)

    def test_代入時キャスト(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_INT, "-c", path.DATASET_PATHS_ASSIGN_IMP_DOWNCAST]
        expected = "".join([
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:18:5\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:19:5\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:14:14\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:15:14\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:16:14\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/assign-imp-downcast.c:17:14\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)

    def test_関数引数キャスト(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_INT, "-c", path.DATASET_PATHS_FUNC_ARG_IMP_DOWNCAST]
        expected = "".join([
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:24:18\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:25:18\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:26:18\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:27:18\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:28:18\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/func-arg-imp-downcast.c:29:18\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)

    def test_return時キャスト(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_INT, "-c", path.DATASET_PATHS_RETURN_IMP_DOWNCAST]
        expected = "".join([
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:15:12\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:16:12\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:17:12\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:18:12\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:19:12\n",
            f"[timet-to-int-downcast] {path.REPOSITORY_PATH}/dataset/downcast-bug/return-imp-downcast.c:20:12\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)


class Test_time_tからlongへのキャスト(MyTestCase):
    def test_明示的キャスト(self):
        command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_LONG, "-c", path.DATASET_PATHS_EXP_DOWNCAST]
        expected = "".join([
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:14:39\n",
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:30:21\n",
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:31:21\n",
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:32:21\n",
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:33:21\n",
            "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/exp-downcast.c:34:21\n",
        ])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assert_std_err(result.stderr)
        self.assert_std_out(result.stdout, expected)

    # def test_代入時キャスト(self):
    #     command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_LONG, "-c", path.DATASET_PATHS_ASSIGN_IMP_DOWNCAST]
    #     expected = "".join([
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:27:5\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:28:5\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:23:14\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:24:14\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:25:14\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/assign-imp-downcast.c:26:14\n",
    #     ])
    #     result = subprocess.run(command, capture_output=True, text=True)
    #     self.assert_std_err(result.stderr)
    #     self.assert_std_out(result.stdout, expected)

    # def test_関数引数キャスト(self):
    #     command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_LONG, "-c", path.DATASET_PATHS_FUNC_ARG_IMP_DOWNCAST]
    #     expected = "".join([
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:32:18\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:33:18\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:34:18\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:35:18\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:36:18\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/func-arg-imp-downcast.c:37:18\n",
    #     ])
    #     result = subprocess.run(command, capture_output=True, text=True)
    #     self.assert_std_err(result.stderr)
    #     self.assert_std_out(result.stdout, expected)

    # def test_return時キャスト(self):
    #     command = [path.CLANG_COMMAND, "-fplugin=" + path.LIBRARY_PATHS_TIME_T_TO_LONG, "-c", path.DATASET_PATHS_RETURN_IMP_DOWNCAST]
    #     expected = "".join([
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:25:12\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:26:12\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:27:12\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:28:12\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:29:12\n",
    #         "[timet-to-long-downcast] /home/cysec/develop/y2k38-checker/dataset/downcast-bug/return-imp-downcast.c:30:12\n",
    #     ])
    #     result = subprocess.run(command, capture_output=True, text=True)
    #     self.assert_std_err(result.stderr)
    #     self.assert_std_out(result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
