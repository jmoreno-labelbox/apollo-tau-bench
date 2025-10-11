# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_today_date(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps({"today": "2025-10-02"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_today_date",
                "description": "Get today's date",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
