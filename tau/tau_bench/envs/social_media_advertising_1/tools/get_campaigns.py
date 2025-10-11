# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCampaigns(Tool):
    """Retrieves all advertising campaigns."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        campaigns = list(data.get("campaigns", {}).values())
        ids_ = []
        for i in campaigns:
            ids_ += [i.get("campaign_id")]
        return json.dumps({"campaigns_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_campaigns",
                "description": "Retrieves all advertising campaign ids.",
                "parameters": {},
            },
        }
