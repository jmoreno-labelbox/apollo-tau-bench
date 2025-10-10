# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_code_owner_for_module(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], module_name: str) -> str:
        ownership_map = data.get("ownership_map", [])
        path_map = {
            "GameEngine.dll": "src/game/engine/renderer.cpp"
        }
        file_path = path_map.get(module_name)
        if not file_path:
            return json.dumps({"error": f"No known file path for module '{module_name}'"}, indent=2)

        for owner_info in ownership_map:
            if owner_info.get("file_path") in file_path:
                return json.dumps(owner_info, indent=2)
        return json.dumps({"error": f"Owner for module '{module_name}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_code_owner_for_module", "description": "Finds the code owner for a given module name by mapping it to a file path.", "parameters": { "type": "object", "properties": { "module_name": { "type": "string" } }, "required": ["module_name"] } } }
