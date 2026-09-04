from app.services.rule_engine import evaluate_rule
from app.services.policy_loader import get_policy

def evaluate_scenario(policy_id: str, scenario: str):
    policy = get_policy(policy_id)
    if not policy:
        raise ValueError("Policy not found")

    evaluations = [evaluate_rule(r, scenario) for r in policy["rules"]]
    passed = sum(e.status == "PASS" for e in evaluations)
    failed = sum(e.status == "FAIL" for e in evaluations)
    warnings = sum(e.status == "WARNING" for e in evaluations)
    critical = sum(e.status == "FAIL" and e.severity == "CRITICAL" for e in evaluations)

    score = round((passed / len(evaluations)) * 100, 1)
    if critical:
        score = max(0, round(score - 40, 1))

    if failed or score < 50:
        overall = "NON_COMPLIANT"
    elif warnings or score < 80:
        overall = "WARNING"
    else:
        overall = "COMPLIANT"

    remediations = []
    for rule, evaluation in zip(policy["rules"], evaluations):
        if evaluation.status == "FAIL":
            remediations.append(rule["remediation"])

    return {
        "policy_id": policy_id, "policy_name": policy["name"], "score": score,
        "status": overall, "passed": passed, "failed": failed, "warnings": warnings,
        "critical_violations": critical, "evaluations": evaluations,
        "remediations": list(dict.fromkeys(remediations))
    }
