from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeReallocation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reallocated_employees: list = None, cancelled_project_id: str = None, new_projects: list = None) -> str:
        reallocated_employees = reallocated_employees or []
        new_projects = new_projects or []

        if not all([reallocated_employees, cancelled_project_id]):
            payload = {"error": "reallocated_employees and cancelled_project_id are required"}
            out = json.dumps(payload)
            return out

        reallocated_count = len(reallocated_employees)

        all_resources_assigned = len(new_projects) >= reallocated_count
        payload = {
            "reallocated_count": reallocated_count,
            "all_resources_assigned": all_resources_assigned,
            "cancelled_project": cancelled_project_id,
            "reallocated_employees": reallocated_employees,
            "new_projects": new_projects,
            "summary": f"Successfully reallocated {reallocated_count} employees from cancelled project {cancelled_project_id}",
            "status": "completed",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizeReallocation",
                "description": "Generate a summary of employee reallocation after project cancellation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reallocated_employees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs that were reallocated",
                        },
                        "cancelled_project_id": {
                            "type": "string",
                            "description": "ID of the cancelled project",
                        },
                        "new_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of new project IDs where employees were assigned",
                        },
                    },
                    "required": ["reallocated_employees", "cancelled_project_id"],
                },
            },
        }
