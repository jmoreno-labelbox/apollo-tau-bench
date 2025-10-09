from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLastAccessTime(Tool):
    """Fetches the last access timestamp for a particular file on a specified server."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str = None, server_hostname: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = {"last_accessed": file.get("last_accessed")}
                            out = json.dumps(
                                payload)
                            return out
                payload = {"error": f"File not found: {filepath} on server {server_hostname}"}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastAccessTime",
                "description": "Retrieves the last access timestamp for a specific file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "The full path to the file.",
                        },
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server where the file is located.",
                        },
                    },
                    "required": ["filepath", "server_hostname"],
                },
            },
        }
