# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_departments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(list(data.get("departments", {}).values()), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_departments",
                "description": "Return every department record.",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }
        }
