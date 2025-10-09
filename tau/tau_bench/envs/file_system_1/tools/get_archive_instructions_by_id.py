from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetArchiveInstructionsByID(Tool):
    """Fetches a particular archival task using its ID from the instructions database."""

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None) -> str:
        for instruction in data.get("archive_instructions", {}).values():
            if instruction.get("archive_id") == archive_id:
                payload = instruction
                out = json.dumps(payload)
                return out
        payload = {"error": f"Archive instruction with ID '{archive_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArchiveInstructionsById",
                "description": "Fetches a specific archival task (e.g., files to include, destination) by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {
                            "type": "string",
                            "description": "The unique ID of the archive task (e.g., 'arch_001').",
                        }
                    },
                    "required": ["archive_id"],
                },
            },
        }
