# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ParseDirectoryRestructureInstructionsTool(Tool):
    """Parses user instructions for moving and sorting files into a structured format."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parse_directory_restructure_instructions",
                "description": "Parses instructions to move files from a target directory to a destination, sorting by file type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_directory": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "sort_rules": {
                            "type": "object",
                            "description": "A dictionary mapping file extensions to subdirectory names.",
                        },
                    },
                    "required": [
                        "target_directory",
                        "destination_directory",
                        "sort_rules",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "directories_db" not in data:
            data["directories_db"] = []
        instruction = {**kwargs}
        data["directories_db"].append(instruction)
        return json.dumps({"status": "success", "instruction": instruction})
