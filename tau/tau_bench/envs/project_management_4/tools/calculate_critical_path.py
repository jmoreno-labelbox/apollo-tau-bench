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

class CalculateCriticalPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        data.get("milestone_dependencies", [])
        critical_paths = data.get("critical_paths", [])

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(
                payload)
            return out

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

            if (
                milestone.get("is_critical_path")
                and milestone.get("is_critical_path") is True
            ):
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
        payload = {
                "success": True,
                "critical_path": result,
                "critical_milestones_count": len(critical_milestone_ids),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateCriticalPath",
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
