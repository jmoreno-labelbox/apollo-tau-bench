# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCriticalPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        if not project_id:
            return json.dumps({"error": "project_id is required"})

        milestones = list(data.get("milestones", {}).values())
        milestone_dependencies = data.get("milestone_dependencies", [])
        critical_paths = data.get("critical_paths", [])

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if not project_milestones:
            return json.dumps(
                {"error": f"No milestones found for project '{project_id}'"}
            )

        critical_milestone_ids = []
        total_duration = 0

        for milestone in project_milestones:
            if milestone.get("float_days", 0) == 0:
                critical_milestone_ids.append(milestone.get("milestone_id"))

                start = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target - start).days
                total_duration = max(total_duration, duration)

            if milestone.get("is_critical_path") and milestone.get("is_critical_path") is True:
                critical_milestone_ids.append(milestone.get("milestone_id"))

                start = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target - start).days
                total_duration = max(total_duration, duration)

        path_id = f"cp_{uuid.uuid4().hex[:8]}"
        existing_path = next(
            (cp for cp in critical_paths if cp.get("project_id") == project_id), None
        )

        if existing_path:
            existing_path["critical_tasks"] = critical_milestone_ids
            existing_path["total_duration_days"] = total_duration
            existing_path["last_calculated"] = datetime.now(timezone.utc).isoformat()
            result = existing_path
        else:
            new_path = {
                "path_id": path_id,
                "project_id": project_id,
                "critical_tasks": critical_milestone_ids,
                "total_duration_days": total_duration,
                "slack_time": 0,
                "last_calculated": datetime.now(timezone.utc).isoformat(),
            }
            critical_paths.append(new_path)
            result = new_path

        return json.dumps(
            {
                "success": True,
                "critical_path": result,
                "critical_milestones_count": len(critical_milestone_ids),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_critical_path",
                "description": "Calculate and update the critical path for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"}
                    },
                    "required": ["project_id"],
                },
            },
        }
