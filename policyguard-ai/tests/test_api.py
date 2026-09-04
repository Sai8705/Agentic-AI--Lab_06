from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_policies():
    r=client.get("/api/policies")
    assert r.status_code==200
    assert len(r.json())>=3

def test_audit():
    r=client.post("/api/compliance/audit",json={
        "policy_id":"POL-SEC-01",
        "scenario":"MFA 2FA hardware security keys and complex passphrase"
    })
    assert r.status_code==200
    assert r.json()["score"]==100.0
