from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateExternalDependencyStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], dependency_id: str = None, new_status: str = None, actual_delivery_date: str = None) -> str:
        if not all([dependency_id, new_status]):
            payload = {"error": "dependency_id and new_status are required"}
            out = json.dumps(payload)
            return out

        external_dependencies = data.get("external_dependencies", [])
        milestones = data.get("milestones", [])

        dependency = next(
            (
                d
                for d in external_dependencies
                if d.get("dependency_id") == dependency_id
            ),
            None,
        )
        if not dependency:
            payload = {"error": f"External dependency '{dependency_id}' not found"}
            out = json.dumps(
                payload)
            return out

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
        payload = {
                "success": True,
                "dependency": dependency,
                "status_change": f"{old_status} -> {new_status}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateExternalDependencyStatus",
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
