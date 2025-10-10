# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetServerResourceUsage(Tool):
    """Retrieves a server's real-time CPU, memory, and disk usage."""
    @staticmethod
    def invoke(data: Dict[str, Any], hostname) -> str:
        for server in data.get('system_resources', []):
            if server.get('hostname') == hostname:
                return json.dumps(server)
        return json.dumps({"error": f"Resource usage for server '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_server_resource_usage", "description": "Retrieves current CPU, memory, and disk usage for a specific server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}}, "required": ["hostname"]}}}
