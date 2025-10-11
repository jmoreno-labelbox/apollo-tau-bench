# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckSafetyStock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"safety_stock_ok": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "check_safety_stock",
                "description": "Tool function: check_safety_stock",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
