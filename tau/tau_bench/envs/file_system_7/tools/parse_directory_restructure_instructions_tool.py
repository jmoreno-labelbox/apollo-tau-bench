from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class ParseDirectoryRestructureInstructionsTool(Tool):
    """Interprets user instructions for organizing and relocating files into a structured format."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ParseDirectoryRestructureInstructions",
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
    def invoke(
        data: dict[str, Any],
        instruction: dict[str, Any] = None,
        target_directory: Any = None,
        destination_directory: str = None,
        sort_rules: dict = None
    ) -> str:
        if "directories_db" not in data:
            data["directories_db"] = []
        data["directories_db"].append(instruction)
        payload = {"status": "success", "instruction": instruction}
        out = json.dumps(payload)
        return out
