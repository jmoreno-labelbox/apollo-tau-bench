from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindFiles(Tool):
    """Locates files on a server according to defined criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None, search_path: str = None) -> str:
        found_files = []
        for server in data.get("file_system", {}).values():
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    if directory.get("path").startswith(search_path):
                        for file in directory.get("files", []):
                            found_files.append(
                                f"{directory.get('path')}/{file.get('filename')}"
                            )
        payload = {"files": found_files}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFiles",
                "description": "Finds files on a server based on specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server to search.",
                        },
                        "search_path": {
                            "type": "string",
                            "description": "The directory path to start the search from.",
                        },
                    },
                    "required": ["server_hostname", "search_path"],
                },
            },
        }
