# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMilestoneStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], health, milestone_id, new_status, progress_percentage, deliverables_completed = [], status_notes = "") -> str:

        if not all([milestone_id, new_status]):
            return json.dumps({"error": "milestone_id and new_status are required"})

        milestones = list(data.get("milestones", {}).values())
        milestone_updates = data.get("milestone_updates", [])

        for milestone in milestones:
            if milestone.get("milestone_id") == milestone_id:
                old_status = milestone.get("status")
                old_health = milestone.get("health")

                if new_status == "completed":
                    start_date = datetime.fromisoformat(
                        milestone.get("start_date").replace("Z", "+00:00")
                    )
                    current_date = datetime.now(timezone.utc)

                    if current_date < start_date:
                        return json.dumps(
                            {
                                "error": "Cannot mark milestone as completed before its start date"
                            }
                        )

                    total_deliverables = len(milestone.get("deliverables", []))
                    if total_deliverables > 0:
                        if len(deliverables_completed) < total_deliverables:
                            return json.dumps(
                                {
                                    "error": f"All {total_deliverables} deliverables must be completed before marking milestone as completed. Only {len(deliverables_completed)} completed."
                                }
                            )

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
                milestone_updates.append(update_record)

                return json.dumps(
                    {"success": True, "milestone": milestone, "update": update_record}
                )

        return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_milestone_status",
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
