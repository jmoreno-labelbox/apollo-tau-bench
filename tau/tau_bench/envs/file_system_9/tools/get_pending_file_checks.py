from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPendingFileChecks(Tool):
    """Fetches tasks for pending file checks."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pending_tasks = [
            task for task in data.get("file_check_db", {}).values() if not task.get("completed")
        ]
        payload = {"pending_tasks": pending_tasks}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPendingFileChecks",
                "description": "Retrieves pending file check tasks.",
                "parameters": {},
            },
        }
