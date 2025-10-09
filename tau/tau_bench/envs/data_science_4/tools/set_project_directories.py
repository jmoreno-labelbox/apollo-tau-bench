from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetProjectDirectories(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], files: list = None) -> str:
        pass
        # This is a mockup; in an actual setting, this would engage with a file system.
        files = files or []
        project_dir_id = "PROJ_DIR_001"
        file_dir = {
            "paths": files,
            "project_dir_id": project_dir_id,
        }
        data.get("file_directory", []).append(file_dir)
        payload = {"status": "success", "project_dir_id": project_dir_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setProjectDirectories",
                "parameters": {"type": "object", "properties": {}},
            },
        }
