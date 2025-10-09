from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MapHourlyRates(Tool):
    """Determine hourly rate for each project (override → default)."""
    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list[str] = None) -> str:
        project_ids = project_id_list or []
        projects = _by_key(data.get("projects", {}).values()), "project_id")
        rate_map = {
            pid: (
                projects.get(pid, {}).values().get("override_hourly_rate")
                or projects.get(pid, {}).values().get("default_hourly_rate")
                or 0
            )
            for pid in project_ids
        }
        payload = {"rate_map": rate_map}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapHourlyRates",
                "description": "Resolve hourly rate for each project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    },
                    "required": ["project_id_list"],
                },
            },
        }
