# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_details_by_id", "description": "Gets one ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}},
                                                                "required": ["adset_id"]}}}
