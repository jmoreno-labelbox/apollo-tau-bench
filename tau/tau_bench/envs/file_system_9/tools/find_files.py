# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFiles(Tool):
    """Finds files on a server based on specified criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        server_hostname = kwargs.get("server_hostname")
        search_path = kwargs.get("search_path")
        
        found_files = []
        for server in list(data.get("file_system", {}).values()):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    if directory.get("path").startswith(search_path):
                        for file in directory.get("files", []):
                            found_files.append(f"{directory.get('path')}/{file.get('filename')}")
        return json.dumps({"files": found_files})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_files",
                "description": "Finds files on a server based on specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {"type": "string", "description": "The hostname of the server to search."},
                        "search_path": {"type": "string", "description": "The directory path to start the search from."}
                    },
                    "required": ["server_hostname", "search_path"],
                },
            },
        }
