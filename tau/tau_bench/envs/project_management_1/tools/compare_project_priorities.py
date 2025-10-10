# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareProjectPriorities(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id_1 = kwargs.get("project_id_1")
        project_id_2 = kwargs.get("project_id_2")

        if not all([project_id_1, project_id_2]):
            return json.dumps({"error": "project_id_1 and project_id_2 are required"})

        projects = list(data.get("projects", {}).values())

        project_1 = None
        project_2 = None

        for project in projects:
            if project.get("project_id") == project_id_1:
                project_1 = project
            elif project.get("project_id") == project_id_2:
                project_2 = project

        if not project_1 or not project_2:
            return json.dumps({"error": "One or both projects not found"})

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

        return json.dumps(
            {
                "higher_priority_project": higher_priority,
                "lower_priority_project": lower_priority,
                "priority_values": {project_id_1: priority_1, project_id_2: priority_2},
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_project_priorities",
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
