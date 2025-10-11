# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdSets(Tool):
    """Retrieves all ad set IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        adsets = list(data.get("adsets", {}).values())
        ids_ = []
        for i in adsets:
            ids_ += [i.get("adset_id")]
        return json.dumps({"adset_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adsets",
                "description": "Retrieves all ad set IDs.",
                "parameters": {},
            },
        }
