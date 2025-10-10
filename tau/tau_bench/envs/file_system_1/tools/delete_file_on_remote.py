# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteFileOnRemote(Tool):
    """Simulates deleting a file from a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], filepath, hostname) -> str:
        return json.dumps({
            "status": "success", "message": f"Deleted {filepath} from {hostname}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_file_on_remote", "description": "Deletes a specified file from a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}
