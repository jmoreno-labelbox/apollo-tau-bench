# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddExternalDependency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], dependency_name, expected_delivery_date, milestone_id, provider, confirmed = False, contact_info = {}, contingency_days = 0, criticality = "medium", dependency_id = f"ext_{uuid.uuid4().hex[:8]}", notice_days = 30) -> str:

        if not all([milestone_id, dependency_name, provider, expected_delivery_date]):
            return json.dumps(
                {
                    "error": "milestone_id, dependency_name, provider, and expected_delivery_date are required"
                }
            )

        milestones = list(data.get("milestones", {}).values())
        external_dependencies = data.get("external_dependencies", [])

        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        new_dependency = {
            "dependency_id": dependency_id,
            "milestone_id": milestone_id,
            "dependency_name": dependency_name,
            "provider": provider,
            "expected_delivery_date": expected_delivery_date,
            "confirmed": confirmed,
            "contact_info": contact_info,
            "criticality": criticality,
            "contingency_days": contingency_days,
            "notice_days": notice_days,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "status": "pending",
        }

        external_dependencies.append(new_dependency)

        if criticality == "critical" and not new_dependency["confirmed"]:
            milestone["health"] = (
                "yellow"
                if milestone.get("health") == "green"
                else milestone.get("health")
            )

        return json.dumps({"success": True, "external_dependency": new_dependency})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_external_dependency",
                "description": "Add an external dependency to a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "dependency_name": {
                            "type": "string",
                            "description": "Name of the dependency",
                        },
                        "provider": {
                            "type": "string",
                            "description": "External provider name",
                        },
                        "expected_delivery_date": {
                            "type": "string",
                            "description": "Expected delivery date",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "Criticality: low, medium, high, critical",
                        },
                        "confirmed": {
                            "type": "boolean",
                            "description": "Is delivery confirmed",
                        },
                        "contact_info": {
                            "type": "object",
                            "description": "Contact information for provider",
                        },
                        "contingency_days": {
                            "type": "number",
                            "description": "Contingency buffer days",
                        },
                        "notice_days": {
                            "type": "number",
                            "description": "Notice period required",
                        },
                        "dependency_id": {
                            "type": "string",
                            "description": "External dependency ID",
                        }
                    },
                    "required": [
                        "milestone_id",
                        "dependency_name",
                        "provider",
                        "expected_delivery_date",
                    ],
                },
            },
        }
