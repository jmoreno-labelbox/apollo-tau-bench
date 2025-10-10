# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListScenes(Tool):
    """Retrieve all pre‑defined scenes and their actions."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(list(data.get("scenes", {}).values()), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_scenes",
                "description": "Retrieve all pre‑defined scenes and their actions.",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }
