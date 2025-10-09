from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProjectConfigByCity(Tool):
    """Fetches a project_config entry based on target_city."""

    @staticmethod
    def invoke(data: dict[str, Any], target_city: str) -> str:
        rows = data.get("project_config", [])
        for row in rows:
            if row.get("target_city") == target_city:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "project_config not found", "target_city": target_city}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectConfigByCity",
                "description": "Retrieves a project_config entry by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {
                            "type": "string",
                            "description": "City name key in project_config.",
                        }
                    },
                    "required": ["target_city"],
                },
            },
        }
