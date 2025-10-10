# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRiskAssessment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        assessed_by = kwargs.get("assessed_by")
        risk_categories = kwargs.get("risk_categories", {})
        identified_risks = kwargs.get("identified_risks", [])
        mitigation_strategies = kwargs.get("mitigation_strategies", [])
        contingency_plans = kwargs.get("contingency_plans", {})
        rollback_procedure = kwargs.get("rollback_procedure")

        if not all([cr_id, assessed_by]):
            return json.dumps({"error": "cr_id and assessed_by are required"})

        change_requests = list(data.get("change_requests", {}).values())
        risk_assessments = list(data.get("risk_assessments", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        if cr.get("requires_risk_assessment") or (
            cr.get("impact_assessment", {}).get("affects_critical_path")
        ):
            if not mitigation_strategies:
                return json.dumps(
                    {
                        "error": "RULE 5: Mitigation strategies are required for critical path changes"
                    }
                )
            if not contingency_plans:
                return json.dumps(
                    {
                        "error": "RULE 5: Contingency plans are required for critical path changes"
                    }
                )
            if not rollback_procedure:
                return json.dumps(
                    {
                        "error": "RULE 5: Rollback procedure is required for critical path changes"
                    }
                )

        risk_scores = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        total_score = sum(
            risk_scores.get(level, 0) for level in risk_categories.values()
        )
        avg_score = total_score / max(len(risk_categories), 1)

        overall_risk_level = (
            "critical"
            if avg_score >= 3.5
            else "high"
            if avg_score >= 2.5
            else "medium"
            if avg_score >= 1.5
            else "low"
        )

        requires_contingency_budget = (
            overall_risk_level in ["critical", "high"]
            or cr.get("priority") == "critical"
        )

        monitoring_frequency = (
            "continuous"
            if overall_risk_level == "critical"
            else "daily"
            if overall_risk_level == "high"
            else "weekly"
            if overall_risk_level == "medium"
            else "bi-weekly"
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

        return json.dumps({"success": True, "risk_assessment": risk_assessment})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_risk_assessment",
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
