from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from app.schemas import AuditRequest, AuditResponse
from app.services.policy_loader import load_policies
from app.agents.compliance_agent import ComplianceAgent

app = FastAPI(title="PolicyGuard AI", version="1.0")
agent = ComplianceAgent()
STATIC = Path(__file__).resolve().parent / "static"

@app.get("/")
def home():
    return FileResponse(STATIC / "index.html")

@app.get("/api/policies")
def policies():
    return [{"policy_id": p["policy_id"], "name": p["name"]} for p in load_policies()]

@app.post("/api/compliance/audit", response_model=AuditResponse)
def audit(req: AuditRequest):
    try:
        return agent.run(req.policy_id, req.scenario)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8005, reload=False)
