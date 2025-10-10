# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateExternalDependencyStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dependency_id = kwargs.get("dependency_id")
        new_status = kwargs.get("new_status")
        actual_delivery_date = kwargs.get("actual_delivery_date")

        if not all([dependency_id, new_status]):
            return json.dumps({"error": "dependency_id and new_status are required"})

        external_dependencies = data.get("external_dependencies", [])
        milestones = list(data.get("milestones", {}).values())

        dependency = next(
            (
                d
                for d in external_dependencies
                if d.get("dependency_id") == dependency_id
            ),
            None,
        )
        if not dependency:
            return json.dumps(
                {"error": f"External dependency '{dependency_id}' not found"}
            )

        old_status = dependency.get("status")
        dependency["status"] = new_status

        if new_status == "delivered" and actual_delivery_date:
            dependency["actual_delivery_date"] = actual_delivery_date

            expected = datetime.fromisoformat(
                dependency.get("expected_delivery_date").replace("Z", "+00:00")
            )
            actual = datetime.fromisoformat(actual_delivery_date.replace("Z", "+00:00"))

            if actual > expected:
                days_late = (actual - expected).days
                dependency["days_late"] = days_late

                milestone = next(
                    (
                        m
                        for m in milestones
                        if m.get("milestone_id") == dependency.get("milestone_id")
                    ),
                    None,
                )
                if milestone and dependency.get("criticality") in ["high", "critical"]:
                    milestone["health"] = "yellow" if days_late < 7 else "red"

        elif new_status == "delayed":

            milestone = next(
                (
                    m
                    for m in milestones
                    if m.get("milestone_id") == dependency.get("milestone_id")
                ),
                None,
            )
            if milestone:
                milestone["health"] = (
                    "yellow" if milestone.get("health") == "green" else "red"
                )

        return json.dumps(
            {
                "success": True,
                "dependency": dependency,
                "status_change": f"{old_status} -> {new_status}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_external_dependency_status",
                "description": "Update the status of an external dependency",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dependency_id": {
                            "type": "string",
                            "description": "External dependency ID",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: pending, confirmed, delayed, delivered, cancelled",
                        },
                        "actual_delivery_date": {
                            "type": "string",
                            "description": "Actual delivery date (for delivered status)",
                        },
                    },
                    "required": ["dependency_id", "new_status"],
                },
            },
        }
