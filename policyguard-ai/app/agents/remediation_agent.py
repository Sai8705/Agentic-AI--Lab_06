class RemediationAgent:
    def synthesize(self, audit: dict) -> list[str]:
        return audit.get("remediations", [])
