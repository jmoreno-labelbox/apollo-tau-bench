from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class ParseArchiveInstructionsTool(Tool):
    """Interprets user instructions for generating and moving an archive."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ParseArchiveInstructions",
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
    def invoke(
        data: dict[str, Any],
        instructions: dict[str, Any] = None,
        archive_name: Any = None,
        destination_directory: str = None,
        remote_address: str = None,
        files_to_archive: list = None,
        compression_level: int = None,
        encryption_key_id: str = None,
        retention_days: int = None,
        archive_tier: str = None, encryption_enabled: Any = None,
        create_manifest: Any = None,
        verify_after_creation: Any = None,
        ) -> str:
        data["archive_instruct"] = instructions
        payload = {"status": "success", "instructions": instructions}
        out = json.dumps(payload)
        return out
