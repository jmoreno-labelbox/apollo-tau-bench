# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalSupportTicketsCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        count = len(list(data.get("support_tickets", {}).values()))
        return json.dumps({"total_support_tickets": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_support_tickets_count",
                        "description": "Returns the current total number of support tickets in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
