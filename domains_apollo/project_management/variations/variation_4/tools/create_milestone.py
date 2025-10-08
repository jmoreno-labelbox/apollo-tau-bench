from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class CreateMilestone(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        milestone_name: str,
        target_date: str,
        owner_id: str,
        milestone_type: str = "standard",
        description: str = None,
        deliverables: list = None,
        gate_criteria: list = None,
        milestone_id: str = None,
        start_date: str = None
    ) -> str:
        if deliverables is None:
            deliverables = []
        if gate_criteria is None:
            gate_criteria = []
        if milestone_id is None:
            milestone_id = f"ms_{uuid.uuid4().hex[:8]}"

        if not all([project_id, milestone_name, target_date, owner_id]):
            payload = {
                "error": "project_id, milestone_name, target_date, and owner_id are required"
            }
            out = json.dumps(payload)
            return out

        if milestone_type == "major" and not gate_criteria:
            payload = {"error": "Major milestones must have defined gate criteria"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])

        if not start_date:
            target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))
            start_dt = target_dt - timedelta(days=30)
            start_date = start_dt.isoformat()

        start_dt = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))

        if start_dt >= target_dt:
            payload = {"error": "Start date must be before target date"}
            out = json.dumps(payload)
            return out

        new_milestone = {
            "milestone_id": milestone_id,
            "project_id": project_id,
            "milestone_name": milestone_name,
            "milestone_type": milestone_type,
            "start_date": start_date,
            "target_date": target_date,
            "description": description,
            "deliverables": deliverables,
            "gate_criteria": gate_criteria,
            "owner_id": owner_id,
            "status": "not_started",
            "health": "green",
            "progress_percentage": 0,
            "float_days": 0,
            "is_critical_path": False,
            "buffer_consumed": 0,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "baseline_start": start_date,
            "baseline_target": target_date,
            "resource_allocation": 100,
        }

        milestones.append(new_milestone)
        payload = {"success": True, "milestone": new_milestone}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMilestone",
                "description": "Create a new project milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "milestone_name": {
                            "type": "string",
                            "description": "Name of the milestone",
                        },
                        "milestone_type": {
                            "type": "string",
                            "description": "Type: standard, major, phase_gate",
                        },
                        "target_date": {
                            "type": "string",
                            "description": "Target completion date (ISO format)",
                        },
                        "description": {
                            "type": "string",
                            "description": "Milestone description",
                        },
                        "deliverables": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of deliverables",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Owner employee ID",
                        },
                        "gate_criteria": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Gate review criteria (required for major milestones)",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Optional start date",
                        },
                    },
                    "required": [
                        "project_id",
                        "milestone_name",
                        "target_date",
                        "owner_id",
                    ],
                },
            },
        }
