# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MapPathToOwner(Tool):
    """Map a code/asset path to its owner using ownership_map."""
    @staticmethod
    def invoke(data: Dict[str, Any], file_path) -> str:
        maps = list(data.get("ownership_map", {}).values())
        rec = next((m for m in maps if m.get("file_path") == file_path), None)
        return json.dumps({"owner_map": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "map_path_to_owner",
                "description": "Look up an ownership record by exact file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"}
                    },
                    "required": ["file_path"]
                }
            }
        }
