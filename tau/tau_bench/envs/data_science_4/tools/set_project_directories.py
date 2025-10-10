# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetProjectDirectories(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # This is a simulation; in a real environment, this would interact with a file system.
        files = kwargs.get("files", [])
        project_dir_id = "PROJ_DIR_001"
        file_dir = {
            "paths": files,
            "project_dir_id": project_dir_id,
        }
        data.get("file_directory", []).append(file_dir)
        return json.dumps({"status": "success", "project_dir_id": project_dir_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectDirectories",
                "parameters": {"type": "object", "properties": {}},
            },
        }
