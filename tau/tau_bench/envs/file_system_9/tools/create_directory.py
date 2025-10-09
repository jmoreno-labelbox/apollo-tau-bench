from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateDirectory(Tool):
    """Establishes a new directory."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None, new_directory_path: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                server["directories"].append({"path": new_directory_path, "files": []})
                payload = {
                    "status": "success",
                    "message": f"Directory '{new_directory_path}' created on '{server_hostname}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDirectory",
                "description": "Creates a new directory on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server.",
                        },
                        "new_directory_path": {
                            "type": "string",
                            "description": "The full path of the new directory.",
                        },
                    },
                    "required": ["server_hostname", "new_directory_path"],
                },
            },
        }
