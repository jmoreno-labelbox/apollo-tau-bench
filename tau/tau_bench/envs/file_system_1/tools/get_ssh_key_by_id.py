from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSshKeyByID(Tool):
    """Retrieves information for a specific SSH key, including the servers it is permitted on."""

    @staticmethod
    def invoke(data: dict[str, Any], key_id: str = None) -> str:
        for key in data.get("ssh_keys", {}).values():
            if key.get("key_id") == key_id:
                payload = key
                out = json.dumps(payload)
                return out
        payload = {"error": f"SSH key with ID '{key_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSshKeyById",
                "description": "Retrieves details for a specific SSH key, including its list of authorized servers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "key_id": {
                            "type": "string",
                            "description": "The ID of the SSH key (e.g., 'alice_rsa_key').",
                        }
                    },
                    "required": ["key_id"],
                },
            },
        }
