# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DraftSellerBrokerBatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, property_ids) -> str:
        props = property_ids or []
        drafts_uri = f"https://test.storage.com/drafts/client_{client_id}_props_{len(props)}.pdf"
        return json.dumps({"client_id": client_id, "property_ids": props, "drafts_uri": drafts_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draft_seller_broker_batch",
                "description": "Generate a drafts bundle for seller broker emails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["client_id", "property_ids"],
                },
            },
        }
