# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDirectory(Tool):
    """Creates a new directory."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        server_hostname = kwargs.get("server_hostname")
        new_directory_path = kwargs.get("new_directory_path")

        for server in list(data.get("file_system", {}).values()):
            if server.get("hostname") == server_hostname:
                server["directories"].append({"path": new_directory_path, "files": []})
                return json.dumps({"status": "success", "message": f"Directory '{new_directory_path}' created on '{server_hostname}'."})
        
        return json.dumps({"error": f"Server not found: {server_hostname}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_directory",
                "description": "Creates a new directory on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {"type": "string", "description": "The hostname of the server."},
                        "new_directory_path": {"type": "string", "description": "The full path of the new directory."}
                    },
                    "required": ["server_hostname", "new_directory_path"],
                },
            },
        }
