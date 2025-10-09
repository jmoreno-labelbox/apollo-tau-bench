from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListFailedBuildRunsByBranch(Tool):
    """Enumerate unsuccessful build runs for a specified branch."""

    @staticmethod
    def invoke(data: dict[str, Any], branch: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        failed = [
            r for r in runs.values() if r.get("branch") == branch and r.get("status") == "failed"
        ]
        payload = {"count": len(failed), "runs": failed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListFailedBuildRunsByBranch",
                "description": "List failed build runs for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"branch": {"type": "string"}},
                    "required": ["branch"],
                },
            },
        }
