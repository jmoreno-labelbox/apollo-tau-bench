# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetProjectDirectories(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files = []) -> str:
        project_dir_id = "PROJ_DIR_001"
        file_dir = {
            "paths": files,
            "project_dir_id": project_dir_id,
        }
        list(data.get("file_directory", {}).values()).append(file_dir)
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
