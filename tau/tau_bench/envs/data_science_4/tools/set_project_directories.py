from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
        data["file_directory"][file_dir["file_directory_id"]] = file_dir
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
