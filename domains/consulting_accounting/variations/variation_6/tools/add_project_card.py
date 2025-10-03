from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddProjectCard(Tool):
    """Add a new project entry."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str = None,
        publisher_id: str = None,
        isbn: str = None,
        project_title: str = None,
        default_hourly_rate: float = None,
        override_hourly_rate: float = None,
        account_code: str = None,
        is_active: bool = True
    ) -> str:
        projects = data.get("projects", [])
        row = {
            "project_id": project_id,
            "publisher_id": publisher_id,
            "isbn": isbn,
            "project_title": project_title,
            "default_hourly_rate": default_hourly_rate,
            "override_hourly_rate": override_hourly_rate,
            "account_code": account_code,
            "is_active": is_active,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        projects.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddProjectCard",
                "description": "Create a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "project_title": {"type": "string"},
                        "default_hourly_rate": {"type": "number"},
                        "override_hourly_rate": {"type": ["number", "null"]},
                        "account_code": {"type": ["string", "null"]},
                        "is_active": {"type": "boolean"},
                    },
                    "required": [
                        "project_id",
                        "publisher_id",
                        "isbn",
                        "project_title",
                        "default_hourly_rate",
                    ],
                },
            },
        }
