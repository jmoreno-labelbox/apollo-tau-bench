# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMilestone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], description, milestone_name, owner_id, project_id, start_date, target_date, deliverables = [], gate_criteria = [], milestone_id = f"ms_{uuid.uuid4().hex[:8]}", milestone_type = "standard") -> str:

        if not all([project_id, milestone_name, target_date, owner_id]):
            return json.dumps(
                {
                    "error": "project_id, milestone_name, target_date, and owner_id are required"
                }
            )

        if milestone_type == "major" and not gate_criteria:
            return json.dumps(
                {"error": "Major milestones must have defined gate criteria"}
            )

        milestones = list(data.get("milestones", {}).values())
        if not start_date:
            target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))
            start_dt = target_dt - timedelta(days=30)
            start_date = start_dt.isoformat()

        start_dt = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))

        if start_dt >= target_dt:
            return json.dumps({"error": "Start date must be before target date"})

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

        return json.dumps({"success": True, "milestone": new_milestone})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_milestone",
                "description": "Create a new project milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "milestone_id": {"type": "string", "description": "Milestone ID"},
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
