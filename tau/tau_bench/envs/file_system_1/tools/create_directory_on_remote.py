# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDirectoryOnRemote(Tool):
    """Simulates creating a directory on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], directory_path, hostname) -> str:
        return json.dumps({
            "status": "success", "message": f"Directory '{directory_path}' created on {hostname}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_directory_on_remote", "description": "Creates a new directory at the specified path on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "directory_path": {"type": "string"}}, "required": ["hostname", "directory_path"]}}}
