from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CompareProjectPriorities(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id_1: str = None, project_id_2: str = None) -> str:
        if not all([project_id_1, project_id_2]):
            payload = {"error": "project_id_1 and project_id_2 are required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])

        project_1 = None
        project_2 = None

        for project in projects:
            if project.get("project_id") == project_id_1:
                project_1 = project
            elif project.get("project_id") == project_id_2:
                project_2 = project

        if not project_1 or not project_2:
            payload = {"error": "One or both projects not found"}
            out = json.dumps(payload)
            return out

        priority_1 = project_1.get("priority", 3)
        priority_2 = project_2.get("priority", 3)

        if priority_1 < priority_2:
            higher_priority = project_id_1
            lower_priority = project_id_2
        elif priority_2 < priority_1:
            higher_priority = project_id_2
            lower_priority = project_id_1
        else:
            higher_priority = project_id_1
            lower_priority = project_id_2
        payload = {
                "higher_priority_project": higher_priority,
                "lower_priority_project": lower_priority,
                "priority_values": {project_id_1: priority_1, project_id_2: priority_2},
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompareProjectPriorities",
                "description": "Compare priorities of two projects to determine which has higher priority",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_1": {
                            "type": "string",
                            "description": "First project ID",
                        },
                        "project_id_2": {
                            "type": "string",
                            "description": "Second project ID",
                        },
                    },
                    "required": ["project_id_1", "project_id_2"],
                },
            },
        }
