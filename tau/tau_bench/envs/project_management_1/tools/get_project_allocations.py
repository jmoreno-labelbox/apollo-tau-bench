# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        project_allocations = [
            alloc for alloc in allocations if alloc.get("project_id") == project_id
        ]

        return json.dumps(project_allocations, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_allocations",
                "description": "Get all allocations for a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
