from app.schemas import RuleEvaluation

def evaluate_rule(rule: dict, scenario: str) -> RuleEvaluation:
    text = scenario.lower()
    keywords = [k for k in rule.get("required_keywords", []) if k.lower() in text]
    prohibitions = [p for p in rule.get("prohibited_actions", []) if p.lower() in text]

    if prohibitions:
        status = "FAIL"
        reason = "Prohibited action detected: " + ", ".join(prohibitions)
    elif keywords:
        status = "PASS"
        reason = "Required compliance evidence detected: " + ", ".join(keywords)
    else:
        status = "WARNING"
        reason = "No explicit evidence of the required control was found."

    return RuleEvaluation(
        rule_id=rule["rule_id"], name=rule["name"], severity=rule["severity"],
        status=status, matched_keywords=keywords,
        matched_prohibitions=prohibitions, reason=reason
    )
