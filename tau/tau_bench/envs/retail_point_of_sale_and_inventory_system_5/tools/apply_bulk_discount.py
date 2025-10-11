# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyBulkDiscount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"bulk_discount_applied": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", 
            "function": {
                "name": "apply_bulk_discount",
                "description": "Apply bulk discount to eligible products",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
