# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRelease(Tool):
    """Creates a new release for a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        releases = data.get("releases", [])
        new_id_num = max([int(r["id"].split("_")[1]) for r in releases]) + 1
        new_id = f"release_{new_id_num:03d}"
        
        new_release = {
            "id": new_id,
            "project_id": kwargs.get("project_id"),
            "version": kwargs.get("version"),
            "notes": kwargs.get("notes"),
            "created_at": "2025-01-28T00:00:00Z",
            "created_by": kwargs.get("created_by")
        }
        releases.append(new_release)
        return json.dumps(new_release)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_release",
                "description": "Creates a new release for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "version": {"type": "string"},
                        "notes": {"type": "string"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["project_id", "version", "notes", "created_by"],
                },
            },
        }
