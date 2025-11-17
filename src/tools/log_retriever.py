"""Small RAG-style log retriever using local files in /data.
For demo, it returns last N lines of matching log files.
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def fetch_recent_logs(service_name: str, minutes: int = 15):
    path = DATA_DIR / "sample_logs.txt"
    if not path.exists():
        return "NO_LOGS_FOUND"
    with open(path, "r") as f:
        lines = f.readlines()
    # return last 200 lines as demo
    return "".join(lines[-200:])
