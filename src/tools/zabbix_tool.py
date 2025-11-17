"""Mock Zabbix tool - returns a sample alert from data/sample_alerts.json"""
import json
from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def get_alert():
    path = DATA_DIR / "sample_alerts.json"
    if not path.exists():
        return {"id":"alert-000","source":"zabbix","summary":"sample alert - no file"}
    with open(path) as f:
        return json.load(f)[0]
