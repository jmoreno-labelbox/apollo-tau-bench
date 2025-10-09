from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_code_owner_for_module(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], module_name: str) -> str:
        pass
        ownership_map = data.get("ownership_map", [])
        path_map = {"GameEngine.dll": "src/game/engine/renderer.cpp"}
        file_path = path_map.get(module_name)
        if not file_path:
            payload = {"error": f"No known file path for module '{module_name}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for owner_info in ownership_map:
            if owner_info.get("file_path") in file_path:
                payload = owner_info
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Owner for module '{module_name}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCodeOwnerForModule",
                "description": "Finds the code owner for a given module name by mapping it to a file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"module_name": {"type": "string"}},
                    "required": ["module_name"],
                },
            },
        }
