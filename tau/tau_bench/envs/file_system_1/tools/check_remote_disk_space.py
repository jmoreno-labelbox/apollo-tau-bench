# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckRemoteDiskSpace(Tool):
    """Checks the available disk space on a remote server's filesystem."""
    @staticmethod
    def invoke(data: Dict[str, Any], hostname) -> str:
        for server_resources in data.get('system_resources', []):
            if server_resources.get('hostname') == hostname:
                disk_info = server_resources.get('disk', {})
                return json.dumps({
                    "hostname": hostname, "available_gb": disk_info.get("available_gb"), "total_gb": disk_info.get("total_gb"), "usage_percent": disk_info.get("usage_percent")})
        return json.dumps({"error": f"Resource information for server '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_remote_disk_space", "description": "Checks the available disk space on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string", "description": "The hostname of the server to check."}}, "required": ["hostname"]}}}
