# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeReallocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cancelled_project_id, new_projects = [], reallocated_employees = []) -> str:

        if not all([reallocated_employees, cancelled_project_id]):
            return json.dumps(
                {"error": "reallocated_employees and cancelled_project_id are required"}
            )

        reallocated_count = len(reallocated_employees)

        all_resources_assigned = len(new_projects) >= reallocated_count

        return json.dumps(
            {
                "reallocated_count": reallocated_count,
                "all_resources_assigned": all_resources_assigned,
                "cancelled_project": cancelled_project_id,
                "reallocated_employees": reallocated_employees,
                "new_projects": new_projects,
                "summary": f"Successfully reallocated {reallocated_count} employees from cancelled project {cancelled_project_id}",
                "status": "completed",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_reallocation",
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
