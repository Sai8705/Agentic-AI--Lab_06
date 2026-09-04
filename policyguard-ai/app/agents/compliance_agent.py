from app.services.compliance_evaluator import evaluate_scenario

class ComplianceAgent:
    def run(self, policy_id: str, scenario: str):
        return evaluate_scenario(policy_id, scenario)
