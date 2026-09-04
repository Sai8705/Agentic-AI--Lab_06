import json
from pathlib import Path

POLICY_FILE = Path(__file__).resolve().parents[2] / "data" / "policies.json"

def load_policies():
    return json.loads(POLICY_FILE.read_text(encoding="utf-8"))

def get_policy(policy_id: str):
    return next((p for p in load_policies() if p["policy_id"] == policy_id), None)
