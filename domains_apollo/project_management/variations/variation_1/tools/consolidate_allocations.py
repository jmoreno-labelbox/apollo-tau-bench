from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ConsolidateAllocations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, from_projects: list = None, to_project: str = None, total_hours: int = None) -> str:
        if from_projects is None:
            from_projects = []
        payload = {
            "success": True,
            "consolidation": {
                "employee_id": employee_id,
                "from_projects": from_projects,
                "to_project": to_project,
                "total_hours": total_hours,
                "status": "completed",
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidateAllocations",
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
