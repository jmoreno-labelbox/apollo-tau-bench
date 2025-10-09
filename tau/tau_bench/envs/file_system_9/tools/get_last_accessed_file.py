from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLastAccessedFile(Tool):
    """Acquires the file that was accessed most recently on a specific server."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None) -> str:
        latest_file_path = None
        latest_timestamp = (
            "1970-01-01T00:00:00Z"  # Set up with an ancient timestamp
        )

        server_found = False
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                server_found = True
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if file.get("last_accessed") > latest_timestamp:
                            latest_timestamp = file.get("last_accessed")
                            latest_file_path = (
                                f"{directory.get('path')}/{file.get('filename')}"
                            )
                break  # Cease operation upon locating the server

        if not server_found:
            payload = {"error": f"Server not found: {server_hostname}"}
            out = json.dumps(payload)
            return out

        if not latest_file_path:
            payload = {
                "message": f"No files with access times found on server {server_hostname}."
            }
            out = json.dumps(payload)
            return out
        payload = {"filepath": latest_file_path, "last_accessed": latest_timestamp}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastAccessedFile",
                "description": "Gets the most recently accessed file on a specific server.",
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
