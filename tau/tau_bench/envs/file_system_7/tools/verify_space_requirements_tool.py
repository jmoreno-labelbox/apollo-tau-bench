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

class VerifySpaceRequirementsTool(Tool):
    """Contrasts total file size with available disk space to confirm adequacy."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifySpaceRequirements",
                "description": "Compares the total size of files to be moved against available disk space at the destination to ensure the operation can proceed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_path": {
                            "type": "string",
                            "description": "The destination path to check space for.",
                        }
                    },
                    "required": ["destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_path: str) -> str:
        # Retrieve the total size from the previous calculation.
        total_size = data.get("last_total_size", 0)

        # Determine the available space for the destination.
        disk_space_key = f"disk_space_{destination_path.replace('/', '_')}"
        available_space = data.get(
            disk_space_key, 10**12
        )  # Fallback to 1TB if not located.

        if total_size <= available_space:
            payload = {
                "status": "sufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "passed",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "status": "insufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "failed",
                "error": f"Insufficient disk space. Need {total_size} bytes but only {available_space} bytes available.",
            }
            out = json.dumps(payload)
            return out
