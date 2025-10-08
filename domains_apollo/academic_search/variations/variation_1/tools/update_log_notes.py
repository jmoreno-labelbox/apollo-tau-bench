from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateLogNotes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_id: Any = None, new_notes: str = None) -> str:
        if not all([log_id, new_notes]):
            payload = {"error": "log_id and new_notes are required."}
            out = json.dumps(payload)
            return out
        for log in data.get("research_logs", []):
            if log["record_log_id"] == log_id:
                log["annotations"] += f"\n[UPDATE]: {new_notes}"
                payload = {"success": True, "log_entry": log}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Log entry with ID '{log_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLogNotes",
                "description": "Appends new notes to an existing research log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The ID of the log entry to update.",
                        },
                        "new_notes": {
                            "type": "string",
                            "description": "The new notes to append to the existing log.",
                        },
                    },
                    "required": ["log_id", "new_notes"],
                },
            },
        }
