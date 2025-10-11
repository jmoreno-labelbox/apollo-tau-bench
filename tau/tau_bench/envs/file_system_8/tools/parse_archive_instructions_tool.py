# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ParseArchiveInstructionsTool(Tool):
    """Parses user instructions for creating and transferring an archive."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parse_archive_instructions",
                "description": "Loads and validates instructions for an archival task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_name": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "files_to_archive": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "archive_name",
                        "destination_directory",
                        "remote_address",
                        "files_to_archive",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        data["archive_instruct"] = {**kwargs}
        return json.dumps({"status": "success", "instructions": kwargs})
