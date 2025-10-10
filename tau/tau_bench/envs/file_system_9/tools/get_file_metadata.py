# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFileMetadata(Tool):
    """Retrieves metadata for a specific file on a specific server."""
    @staticmethod
    def invoke(data: Dict[str, Any], filepath, server_hostname) -> str:

        for server in list(data.get("file_system", {}).values()):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if f"{directory.get('path')}/{file.get('filename')}" == filepath:
                            return json.dumps(file)
                # If the inner loop completes, the file is not present on this server.
                return json.dumps({"error": f"File not found: {filepath} on server {server_hostname}"})
        # If the outer loop completes, the server was not located.
        return json.dumps({"error": f"Server not found: {server_hostname}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_file_metadata",
                "description": "Retrieves metadata for a specific file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {"type": "string", "description": "The full path to the file."},
                        "server_hostname": {"type": "string", "description": "The hostname of the server where the file is located."}
                    },
                    "required": ["filepath", "server_hostname"],
                },
            },
        }
