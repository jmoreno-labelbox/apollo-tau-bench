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

class CreateMilestoneFromTemplate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        template_id: str,
        project_id: str,
        milestone_name: str,
        target_date: str,
        owner_id: str,
        milestone_id: str = None
    ) -> str:
        if not all([template_id, project_id, milestone_name, target_date, owner_id]):
            payload = {
                "error": "template_id, project_id, milestone_name, target_date, and owner_id are required"
            }
            out = json.dumps(payload)
            return out

        milestone_templates = data.get("milestone_templates", {}).values()
        milestones = data.get("milestones", {}).values()

        template = next(
            (t for t in milestone_templates.values() if t.get("template_id") == template_id),
            None,
        )
        if not template:
            payload = {"error": f"Template '{template_id}' not found"}
            out = json.dumps(payload)
            return out

        if template.get("template_type") == "major" and not template.get(
            "gate_criteria"
        ):
            payload = {"error": "Major milestone templates must include gate criteria"}
            out = json.dumps(payload)
            return out

        milestone_id = milestone_id or f"ms_{uuid.uuid4().hex[:8]}"

        target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))
        duration_days = template.get("duration_days", 30)
        start_dt = target_dt - timedelta(days=duration_days)

        buffer_days = int(duration_days * (template.get("buffer_percentage", 0) / 100))

        new_milestone = {
            "milestone_id": milestone_id,
            "project_id": project_id,
            "milestone_name": milestone_name,
            "milestone_type": template.get("template_type"),
            "start_date": start_dt.isoformat(),
            "target_date": target_date,
            "description": f"Created from template: {template.get('template_name')}",
            "deliverables": template.get("deliverables", []),
            "gate_criteria": template.get("gate_criteria", []),
            "owner_id": owner_id,
            "status": "not_started",
            "health": "green",
            "progress_percentage": 0,
            "float_days": buffer_days,
            "is_critical_path": template.get("is_critical_path_candidate", False),
            "buffer_consumed": 0,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "baseline_start": start_dt.isoformat(),
            "baseline_target": target_date,
            "original_baseline_start": start_dt.isoformat(),
            "original_baseline_target": target_date,
            "template_id": template_id,
            "resource_allocation": 100,
        }

        data["milestones"][milestone_id] = new_milestone
        payload = {
            "success": True,
            "milestone": new_milestone,
            "template_used": template.get("template_name"),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMilestoneFromTemplate",
                "description": "Create a new milestone from a predefined template",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_id": {"type": "string", "description": "Template ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "project_id": {"type": "string", "description": "Project ID"},
                        "milestone_name": {
                            "type": "string",
                            "description": "Name for the new milestone",
                        },
                        "target_date": {
                            "type": "string",
                            "description": "Target completion date",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Owner employee ID",
                        },
                    },
                    "required": [
                        "template_id",
                        "project_id",
                        "milestone_name",
                        "target_date",
                        "owner_id",
                    ],
                },
            },
        }
