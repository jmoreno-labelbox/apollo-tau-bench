# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLastAccessedFile(Tool):
    """Gets the most recently accessed file on a specific server."""
    @staticmethod
    def invoke(data: Dict[str, Any], server_hostname) -> str:
        
        latest_file_path = None
        latest_timestamp = "1970-01-01T00:00:00Z" # Set the initial value to a significantly outdated timestamp.

        server_found = False
        for server in list(data.get("file_system", {}).values()):
            if server.get("hostname") == server_hostname:
                server_found = True
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if file.get("last_accessed") > latest_timestamp:
                            latest_timestamp = file.get("last_accessed")
                            latest_file_path = f"{directory.get('path')}/{file.get('filename')}"
                break # Terminate upon locating the server.
        
        if not server_found:
            return json.dumps({"error": f"Server not found: {server_hostname}"})

        if not latest_file_path:
            return json.dumps({"message": f"No files with access times found on server {server_hostname}."})

        return json.dumps({
            "filepath": latest_file_path,
            "last_accessed": latest_timestamp
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_last_accessed_file",
                "description": "Gets the most recently accessed file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {"type": "string", "description": "The hostname of the server to check."}
                    },
                    "required": ["server_hostname"],
                },
            },
        }
