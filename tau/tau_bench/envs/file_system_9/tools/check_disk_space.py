# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckDiskSpace(Tool):
    """Checks the available disk space on a server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        server_hostname = kwargs.get("server_hostname")
        for server in data.get("system_resources", []):
            if server.get("hostname") == server_hostname:
                return json.dumps(server.get("disk"))
        return json.dumps({"error": f"Server not found: {server_hostname}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_disk_space",
                "description": "Checks the available disk space on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {"type": "string", "description": "The hostname of the server to check."}
                    },
                    "required": ["server_hostname"],
                },
            },
        }
