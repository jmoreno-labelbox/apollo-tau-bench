from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CreateResourceConflict(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, competing_projects: list = [], conflict_type: str = "allocation", resolution: str = "") -> str:
        if not all([employee_id, competing_projects]):
            payload = {"error": "employee_id and competing_projects are required"}
            out = json.dumps(payload)
            return out

        resource_conflicts = data.get("resource_conflicts", [])

        conflict_id = f"conflict_{uuid.uuid4().hex[:8]}"

        new_conflict = {
            "conflict_id": conflict_id,
            "employee_id": employee_id,
            "competing_projects": competing_projects,
            "conflict_type": conflict_type,
            "resolution": resolution,
            "created_date": datetime.now().isoformat(),
            "status": "resolved" if resolution else "pending",
        }

        resource_conflicts.append(new_conflict)
        payload = {"success": True, "conflict": new_conflict}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResourceConflict",
                "description": "Create a record of resource conflict when multiple projects compete for the same employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "competing_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of competing project IDs",
                        },
                        "conflict_type": {
                            "type": "string",
                            "description": "Type of conflict",
                        },
                        "resolution": {
                            "type": "string",
                            "description": "How the conflict was resolved",
                        },
                    },
                    "required": ["employee_id", "competing_projects"],
                },
            },
        }
