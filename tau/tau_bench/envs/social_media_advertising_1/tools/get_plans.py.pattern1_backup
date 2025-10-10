# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlans(Tool):
    """Retrieves all plan IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plans = data.get("plans", [])
        ids_ = []
        for i in plans:
            ids_ += [i.get("plan_id")]
        return json.dumps({"plan_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_plans",
                "description": "Retrieves all plan IDs.",
                "parameters": {},
            },
        }
