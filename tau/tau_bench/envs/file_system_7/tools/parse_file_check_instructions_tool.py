# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ParseFileCheckInstructionsTool(Tool):
    """Tool to parse instructions for a given task and store them."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parse_file_check_instructions",
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
    def invoke(data: Dict[str, Any], task_id) -> str:
        task_details = next(
            (t for t in data.get("file_check_db", []) if t["task_id"] == task_id), None
        )
        if not task_details:
            return json.dumps({"error": f"Task ID {task_id} not found."})

        # The parsed_instructions field is pre-structured, allowing for direct usage.
        instructions = task_details.get("parsed_instructions", {})
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Rebuild the simplified task_instructions structure using the detailed parsed_instructions.
        parsed_instruction = {
            "task_id": task_id,
            "remote_address": task_details.get("remote_server"),
            "max_size": instructions.get("size_filter", {}).get("max_bytes"),
            "last_access_days": instructions.get("time_filter", {}).get("days"),
            "users": instructions.get("user_filter", []),
        }
        data["task_instructions"].append(parsed_instruction)
        return json.dumps(
            {"status": "success", "parsed_instruction": parsed_instruction}
        )
