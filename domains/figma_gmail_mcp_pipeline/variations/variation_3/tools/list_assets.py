from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_assets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        rows = list(_ensure(data, "assets", []))
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAssets",
                "description": "List exported assets and reports.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
