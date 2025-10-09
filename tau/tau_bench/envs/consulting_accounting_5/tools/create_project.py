from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: str, publisher_id: str, isbn: str, project_title: str, default_hourly_rate: float) -> str:
        """
        Creates a new project for a publisher.
        """
        new_project = {
            "project_id": project_id,
            "publisher_id": publisher_id,
            "isbn": isbn,
            "project_title": project_title,
            "default_hourly_rate": default_hourly_rate,
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
