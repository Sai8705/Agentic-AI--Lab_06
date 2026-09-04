from pydantic import BaseModel, Field
from typing import Literal

Severity = Literal["CRITICAL","HIGH","MEDIUM","LOW"]
Status = Literal["PASS","FAIL","WARNING"]

class AuditRequest(BaseModel):
    policy_id: str
    scenario: str = Field(min_length=3)

class RuleEvaluation(BaseModel):
    rule_id: str
    name: str
    severity: Severity
    status: Status
    matched_keywords: list[str] = []
    matched_prohibitions: list[str] = []
    reason: str

class AuditResponse(BaseModel):
    policy_id: str
    policy_name: str
    score: float
    status: str
    passed: int
    failed: int
    warnings: int
    critical_violations: int
    evaluations: list[RuleEvaluation]
    remediations: list[str]
