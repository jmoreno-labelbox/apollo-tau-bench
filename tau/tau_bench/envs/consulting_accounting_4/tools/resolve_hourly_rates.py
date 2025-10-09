from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ResolveHourlyRates(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list[str] = None) -> str:
        project_id_list = project_id_list or []
        projects = _index_by(list(data.get("projects", {}).values()), "project_id")
        rate_map = {}
        for pid in project_id_list:
            pr = projects.get(pid) or {}
            rate_map[pid] = (
                pr.get("override_hourly_rate") or pr.get("default_hourly_rate") or 0
            )
        payload = {"rate_map": rate_map}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveHourlyRates",
                "description": "Resolve hourly rate per project (override else default).",
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
