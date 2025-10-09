from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLastSuccessfulTaskRun(Tool):
    """Identifies the log entry for the last successful completion of a task of a specific type."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None) -> str:
        successful_runs = [
            log
            for log in data.get("task_logs", [])
            if log.get("task_type") == task_type and log.get("result") == "success"
        ]
        if not successful_runs:
            payload = {"error": f"No successful run found for type '{task_type}'."}
            out = json.dumps(payload)
            return out
        last_run = max(successful_runs, key=lambda x: x["completed_at"])
        payload = last_run
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastSuccessfulTaskRun",
                "description": "Finds when a specific type of task last completed successfully.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_type": {
                            "type": "string",
                            "enum": ["archive", "file_check", "file_organization"],
                        }
                    },
                    "required": ["task_type"],
                },
            },
        }
