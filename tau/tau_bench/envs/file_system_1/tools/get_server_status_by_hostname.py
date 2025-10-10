# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetServerStatusByHostname(Tool):
    """Checks the status of a remote server (e.g., online, maintenance)."""
    @staticmethod
    def invoke(data: Dict[str, Any], hostname) -> str:
        for server in data.get('remote_servers', []):
            if server.get('hostname') == hostname:
                return json.dumps({"hostname": hostname, "status": server.get("status")})
        return json.dumps({"error": f"Server with hostname '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_server_status_by_hostname", "description": "Retrieves the current operational status of a server by its hostname.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string", "description": "The fully qualified domain name of the server."}}, "required": ["hostname"]}}}
