# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExtractTaskInstructionsTool(Tool):
    """Extracts and stores task instructions from the file check database."""

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_task_id = kwargs["task_id"]

        # Fetch task from the database.
        task_record = None
        for record in data.get("file_check_db", []):
            if record["task_id"] == target_task_id:
                task_record = record
                break

        if task_record is None:
            return json.dumps({"error": f"Task ID {target_task_id} not found."})

        # Retrieve pre-processed directives from the task log.
        instruction_data = task_record.get("parsed_instructions", {})

        # Set up storage if required.
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Construct a streamlined instruction input from the analyzed data.
        simplified_entry = {
            "task_id": target_task_id,
            "remote_address": task_record.get("remote_server"),
            "max_size": instruction_data.get("size_filter", {}).get("max_bytes"),
            "last_access_days": instruction_data.get("time_filter", {}).get("days"),
            "users": instruction_data.get("user_filter", []),
        }

        data["task_instructions"].append(simplified_entry)

        return json.dumps({
            "status": "success",
            "parsed_instruction": simplified_entry
        })
