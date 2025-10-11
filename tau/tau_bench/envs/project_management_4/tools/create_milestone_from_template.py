# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMilestoneFromTemplate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], milestone_name, owner_id, project_id, target_date, template_id, milestone_id = f"ms_{uuid.uuid4().hex[:8]}") -> str:

        if not all([template_id, project_id, milestone_name, target_date, owner_id]):
            return json.dumps(
                {
                    "error": "template_id, project_id, milestone_name, target_date, and owner_id are required"
                }
            )

        milestone_templates = data.get("milestone_templates", [])
        milestones = list(data.get("milestones", {}).values())

        template = next(
            (t for t in milestone_templates if t.get("template_id") == template_id),
            None,
        )
        if not template:
            return json.dumps({"error": f"Template '{template_id}' not found"})

        if template.get("template_type") == "major" and not template.get(
            "gate_criteria"
        ):
            return json.dumps(
                {"error": "Major milestone templates must include gate criteria"}
            )

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

        milestones.append(new_milestone)

        return json.dumps(
            {
                "success": True,
                "milestone": new_milestone,
                "template_used": template.get("template_name"),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_milestone_from_template",
                "description": "Create a new milestone from a predefined template",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_id": {"type": "string", "description": "Template ID"},
                        "milestone_id": {"type": "string", "description": "Milestone ID"},
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
