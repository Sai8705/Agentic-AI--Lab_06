from app.services.rule_engine import evaluate_rule

def test_prohibition_fails():
    rule={"rule_id":"X","name":"test","severity":"CRITICAL","required_keywords":["https"],"prohibited_actions":["http transmission"]}
    r=evaluate_rule(rule,"data sent by http transmission")
    assert r.status=="FAIL"

def test_keyword_passes():
    rule={"rule_id":"X","name":"test","severity":"HIGH","required_keywords":["mfa"],"prohibited_actions":[]}
    assert evaluate_rule(rule,"mfa enabled").status=="PASS"
