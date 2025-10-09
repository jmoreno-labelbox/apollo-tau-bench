from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetPendingFileChecks(Tool):
    """Fetches tasks for pending file checks."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pending_tasks = [
            task for task in data.get("file_check_db", []) if not task.get("completed")
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
