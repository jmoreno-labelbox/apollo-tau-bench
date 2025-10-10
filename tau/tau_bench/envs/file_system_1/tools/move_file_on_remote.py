# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MoveFileOnRemote(Tool):
    """Simulates moving a file from a source to a destination on the same remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({
            "status": "success", "message": f"Moved {kwargs.get('source_path')} to {kwargs.get('destination_path')} on {kwargs.get('hostname')}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "move_file_on_remote", "description": "Moves a file on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "source_path": {"type": "string"}, "destination_path": {"type": "string"}}, "required": ["hostname", "source_path", "destination_path"]}}}
