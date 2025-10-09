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

class ExtractTaskInstructionsTool(Tool):
    """Retrieves and saves task instructions from the file check database."""

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
        target_task_id = task_id

        # Fetch task from the database
        task_record = None
        for record in data.get("file_check_db", {}).values():
            if record["task_id"] == target_task_id:
                task_record = record
                break

        if task_record is None:
            payload = {"error": f"Task ID {target_task_id} not found."}
            out = json.dumps(payload)
            return out

        # Obtain pre-parsed instructions from the task record
        instruction_data = task_record.get("parsed_instructions", {}).values()

        # Set up storage if necessary
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Create a simplified instruction entry from the detailed parsed information
        simplified_entry = {
            "task_id": target_task_id,
            "remote_address": task_record.get("remote_server"),
            "max_size": instruction_data.get("size_filter", {}).values().get("max_bytes"),
            "last_access_days": instruction_data.get("time_filter", {}).values().get("days"),
            "users": instruction_data.get("user_filter", {}).values()),
        }

        data["task_instructions"].append(simplified_entry)
        payload = {"status": "success", "parsed_instruction": simplified_entry}
        out = json.dumps(payload)
        return out
