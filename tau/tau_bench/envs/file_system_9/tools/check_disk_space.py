from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckDiskSpace(Tool):
    """Assesses the free disk space on a server."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None) -> str:
        for server in data.get("system_resources", []):
            if server.get("hostname") == server_hostname:
                payload = server.get("disk")
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
                "name": "CheckDiskSpace",
                "description": "Checks the available disk space on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server to check.",
                        }
                    },
                    "required": ["server_hostname"],
                },
            },
        }
