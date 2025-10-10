# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckRemoteFileExists(Tool):
    """Verifies that a specific file exists on a given remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        filepath = kwargs.get("filepath")
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    for file in directory.get('files', []):
                        if f"{directory.get('path')}/{file.get('filename')}" == filepath:
                             return json.dumps({"exists": True, "file_details": file})
        return json.dumps({"exists": False})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_remote_file_exists", "description": "Checks if a file exists at a specific path on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}
