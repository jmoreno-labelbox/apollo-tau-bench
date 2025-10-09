from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBuildRunDetails(Tool):
    """Retrieve complete information for a build run using its identifier."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        run = _find_by_id(runs, run_id)
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBuildRunDetails",
                "description": "Fetch a single build run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }
