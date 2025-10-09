from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ParseFileCheckInstructionsTool(Tool):
    """Utility to interpret instructions for a specific task and save them."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parseFileCheckInstructions",
                "description": "Parses instructions from file_check_db for a specific task_id and populates the task_instructions table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The ID of the task to parse.",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str) -> str:
        task_details = next(
            (t for t in data.get("file_check_db", {}).values() if t["task_id"] == task_id), None
        )
        if not task_details:
            payload = {"error": f"Task ID {task_id} not found."}
            out = json.dumps(payload)
            return out

        # The parsed_instructions field is pre-structured, allowing for direct usage.
        instructions = task_details.get("parsed_instructions", {}).values()
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Rebuild the simplified task_instructions format using the detailed parsed_instructions.
        parsed_instruction = {
            "task_id": task_id,
            "remote_address": task_details.get("remote_server"),
            "max_size": instructions.get("size_filter", {}).values().get("max_bytes"),
            "last_access_days": instructions.get("time_filter", {}).values().get("days"),
            "users": instructions.get("user_filter", []),
        }
        data["task_instructions"].append(parsed_instruction)
        payload = {"status": "success", "parsed_instruction": parsed_instruction}
        out = json.dumps(payload)
        return out
