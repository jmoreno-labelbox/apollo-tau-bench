# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareInventoryCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"discrepancy": 6, "percent": 6.0}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "compare_inventory_counts",
                "description": "Tool function: compare_inventory_counts",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
