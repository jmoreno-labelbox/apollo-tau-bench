from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

class CreateRiskAssessment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str = None,
        assessed_by: str = None,
        risk_categories: dict = {},
        identified_risks: list = [],
        mitigation_strategies: list = [],
        contingency_plans: dict = {},
        rollback_procedure: str = None
    ) -> str:
        if not all([cr_id, assessed_by]):
            payload = {"error": "cr_id and assessed_by are required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        risk_assessments = data.get("risk_assessments", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        if cr.get("requires_risk_assessment") or (
            cr.get("impact_assessment", {}).get("affects_critical_path")
        ):
            if not mitigation_strategies:
                payload = {
                    "error": "RULE 5: Mitigation strategies are required for critical path changes"
                }
                out = json.dumps(payload)
                return out
            if not contingency_plans:
                payload = {
                    "error": "RULE 5: Contingency plans are required for critical path changes"
                }
                out = json.dumps(payload)
                return out
            if not rollback_procedure:
                payload = {
                    "error": "RULE 5: Rollback procedure is required for critical path changes"
                }
                out = json.dumps(payload)
                return out

        risk_scores = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        total_score = sum(
            risk_scores.get(level, 0) for level in risk_categories.values()
        )
        avg_score = total_score / max(len(risk_categories), 1)

        overall_risk_level = (
            "critical"
            if avg_score >= 3.5
            else "high" if avg_score >= 2.5 else "medium" if avg_score >= 1.5 else "low"
        )

        requires_contingency_budget = (
            overall_risk_level in ["critical", "high"]
            or cr.get("priority") == "critical"
        )

        monitoring_frequency = (
            "continuous"
            if overall_risk_level == "critical"
            else (
                "daily"
                if overall_risk_level == "high"
                else "weekly" if overall_risk_level == "medium" else "bi-weekly"
            )
        )

        assessment_id = f"ra_{uuid.uuid4().hex[:8]}"

        risk_assessment = {
            "assessment_id": assessment_id,
            "cr_id": cr_id,
            "assessed_by": assessed_by,
            "assessment_date": datetime.now().isoformat(),
            "risk_categories": risk_categories,
            "overall_risk_level": overall_risk_level,
            "identified_risks": identified_risks,
            "mitigation_strategies": mitigation_strategies,
            "contingency_plans": contingency_plans,
            "rollback_procedure": rollback_procedure,
            "requires_contingency_budget": requires_contingency_budget,
            "monitoring_frequency": monitoring_frequency,
        }

        risk_assessments.append(risk_assessment)

        if cr.get("status") == "in_review":
            cr["risk_assessment_id"] = assessment_id
            cr["risk_level"] = overall_risk_level
        payload = {"success": True, "risk_assessment": risk_assessment}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRiskAssessment",
                "description": "Create risk assessment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "assessed_by": {
                            "type": "string",
                            "description": "Risk assessor ID",
                        },
                        "risk_categories": {
                            "type": "object",
                            "description": "Risk levels by category (technical, schedule, resource, quality, stakeholder): low/medium/high/critical",
                        },
                        "identified_risks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of identified risks",
                        },
                        "mitigation_strategies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Risk mitigation strategies",
                        },
                        "contingency_plans": {
                            "type": "object",
                            "description": "Contingency plans mapping",
                        },
                        "rollback_procedure": {
                            "type": "string",
                            "description": "Rollback procedure if change fails",
                        },
                    },
                    "required": ["cr_id", "assessed_by"],
                },
            },
        }
