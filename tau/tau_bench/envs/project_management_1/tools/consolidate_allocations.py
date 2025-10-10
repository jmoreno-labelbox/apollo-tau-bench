# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ConsolidateAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        from_projects = kwargs.get("from_projects", [])
        to_project = kwargs.get("to_project")
        total_hours = kwargs.get("total_hours")

        return json.dumps(
            {
                "success": True,
                "consolidation": {
                    "employee_id": employee_id,
                    "from_projects": from_projects,
                    "to_project": to_project,
                    "total_hours": total_hours,
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidate_allocations",
                "description": "Consolidate multiple partial allocations into one",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "from_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs to consolidate from",
                        },
                        "to_project": {
                            "type": "string",
                            "description": "Target project ID",
                        },
                        "total_hours": {
                            "type": "number",
                            "description": "Total hours to allocate",
                        },
                    },
                    "required": [
                        "employee_id",
                        "from_projects",
                        "to_project",
                        "total_hours",
                    ],
                },
            },
        }
