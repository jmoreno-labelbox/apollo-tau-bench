from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMilestoneStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str = None,
        new_status: str = None,
        progress_percentage: int = None,
        health: str = None,
        deliverables_completed: list = None,
        status_notes: str = ""
    ) -> str:
        if deliverables_completed is None:
            deliverables_completed = []

        if not all([milestone_id, new_status]):
            payload = {"error": "milestone_id and new_status are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        milestone_updates = data.get("milestone_updates", {}).values()

        for milestone in milestones.values():
            if milestone.get("milestone_id") == milestone_id:
                milestone.get("status")
                old_health = milestone.get("health")

                if new_status == "completed":
                    start_date = datetime.fromisoformat(
                        milestone.get("start_date").replace("Z", "+00:00")
                    )
                    current_date = datetime.now(timezone.utc)

                    if current_date < start_date:
                        payload = {
                            "error": "Cannot mark milestone as completed before its start date"
                        }
                        out = json.dumps(payload)
                        return out

                    total_deliverables = len(milestone.get("deliverables", []))
                    if total_deliverables > 0:
                        if len(deliverables_completed) < total_deliverables:
                            payload = {
                                "error": f"All {total_deliverables} deliverables must be completed before marking milestone as completed. Only {len(deliverables_completed)} completed."
                            }
                            out = json.dumps(payload)
                            return out

                    milestone["actual_completion_date"] = datetime.now(
                        timezone.utc
                    ).isoformat()
                    milestone["progress_percentage"] = 100
                else:
                    if progress_percentage is not None:
                        milestone["progress_percentage"] = progress_percentage

                milestone["status"] = new_status
                if health:
                    milestone["health"] = health

                update_id = f"upd_{uuid.uuid4().hex[:8]}"
                update_record = {
                    "update_id": update_id,
                    "milestone_id": milestone_id,
                    "progress_percentage": milestone["progress_percentage"],
                    "status": new_status,
                    "status_notes": status_notes,
                    "deliverables_completed": deliverables_completed,
                    "health_change": f"{old_health} -> {milestone['health']}",
                    "updated_date": datetime.now(timezone.utc).isoformat(),
                }
                data["milestone_updates"][update_record["milestone_update_id"]] = update_record
                payload = {"success": True, "milestone": milestone, "update": update_record}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Milestone '{milestone_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMilestoneStatus",
                "description": "Update milestone status, progress, and health",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: not_started, in_progress, completed, delayed",
                        },
                        "progress_percentage": {
                            "type": "number",
                            "description": "Progress percentage (0-100)",
                        },
                        "health": {
                            "type": "string",
                            "description": "Health status: green, yellow, red",
                        },
                        "status_notes": {
                            "type": "string",
                            "description": "Notes about the update",
                        },
                        "deliverables_completed": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of completed deliverables (required for completion)",
                        },
                    },
                    "required": ["milestone_id", "new_status"],
                },
            },
        }
