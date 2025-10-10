# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateResourceConflict(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        competing_projects = kwargs.get("competing_projects", [])
        conflict_type = kwargs.get("conflict_type", "allocation")
        resolution = kwargs.get("resolution", "")

        if not all([employee_id, competing_projects]):
            return json.dumps(
                {"error": "employee_id and competing_projects are required"}
            )

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

        return json.dumps({"success": True, "conflict": new_conflict})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_resource_conflict",
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
