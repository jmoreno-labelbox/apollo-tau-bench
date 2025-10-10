# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new project for a publisher.
        """
        new_project = {
            "project_id": kwargs["project_id"],
            "publisher_id": kwargs["publisher_id"],
            "isbn": kwargs["isbn"],
            "project_title": kwargs["project_title"],
            "default_hourly_rate": kwargs["default_hourly_rate"],
            "is_active": True,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        data["projects"].append(new_project)
        return json.dumps(new_project["project_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CreateProject",
                "description": "Create a new project record for a publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "project_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "project_title": {"type": "string"},
                        "default_hourly_rate": {"type": "number"}
                    },
                    "required": ["project_id", "publisher_id", "isbn", "project_title", "default_hourly_rate"],
                },
            },
        }
