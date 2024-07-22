import os
import subprocess


def run_clang_process(path: str) -> str:
    from dotenv import load_dotenv
    env_path = os.path.join(os.path.dirname(__file__), "../.env")
    load_dotenv(env_path)
    cmd = [
        os.environ['CHECK_Y2K38'],
        "-c",
        path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to run clang: {e}")
