# PolicyGuard AI — Policy Compliance Agent

A fast educational implementation of a Policy Compliance Agent based on the provided Experiment 06 design.

## Architecture
User UI → FastAPI → Policy Loader → Deterministic Rule Engine → Compliance Evaluator → Remediation Plan.

The deterministic rule engine is authoritative for compliance decisions; the agent orchestrates the evaluation.

## Run

### Windows PowerShell
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

Open: http://127.0.0.1:8005

### Test
```powershell
python -m pytest tests
```

## Sample scenarios
- PII transmitted over HTTP and raw PII written to logs → NON_COMPLIANT
- MFA + hardware security keys + strong credentials → COMPLIANT
- API key pasted into public chatbot → NON_COMPLIANT

All datasets are synthetic and intended for educational use.
