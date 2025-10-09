from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetLogDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_id: Any = None) -> str:
        log_id = log_id
        if not log_id:
            payload = {"error": "log_id is required."}
            out = json.dumps(payload)
            return out
        for log in data.get("research_logs", {}).values():
            if log["record_log_id"] == log_id:
                return log.get("annotations", "")
        payload = {"error": f"Log entry with ID '{log_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLogDetails",
                "description": "Retrieves just the notes from a single log entry by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The unique ID of the log entry to retrieve.",
                        }
                    },
                    "required": ["log_id"],
                },
            },
        }
