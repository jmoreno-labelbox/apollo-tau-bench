from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ResolveHourlyRate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        proj = next(
            (p for p in data.get("projects", []) if p.get("project_id") == project_id), None
        )
        if not proj:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        rate = (
            proj.get("override_hourly_rate") or proj.get("default_hourly_rate") or 0.0
        )
        payload = {"project_id": project_id, "hourly_rate": float(rate)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveHourlyRate",
                "description": "Return effective hourly rate for a project (override > default).",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
