from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateSellerBrokerEmailDrafts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, property_ids: list = None) -> str:
        props = property_ids or []
        drafts_uri = f"https://storage.example.com/drafts/client_{client_id}_props_{len(props)}.pdf"
        payload = {"client_id": client_id, "property_ids": props, "drafts_uri": drafts_uri}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSellerBrokerEmailDrafts",
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
