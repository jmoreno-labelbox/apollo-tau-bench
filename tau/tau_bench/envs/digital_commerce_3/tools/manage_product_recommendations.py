# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one


class ManageProductRecommendations(Tool):
    """Generate and manage product recommendations for customers."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], contact_id: Any, recommendation_type: Any = "similar_products"
    ) -> str:
        contact_id = _idstr(contact_id)
        recommendation_type = f"{recommendation_type}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        products = list(data.get("products", {}).values())
        recommendations = products[:3]

        recommendation_list = [
            {
                "product_id": p.get("product_id"),
                "product_name": p.get("name"),
                "confidence_score": round(0.9 - (i * 0.1), 2),
            }
            for i, p in enumerate(recommendations)
        ]

        _append_audit(
            data,
            "recommendations_generated",
            contact_id,
            {"recommendation_type": recommendation_type},
        )
        return json.dumps(
            {
                "contact_id": contact_id,
                "recommendation_type": recommendation_type,
                "recommendations": recommendation_list,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_product_recommendations",
                "description": "Generate and manage product recommendations for customers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "recommendation_type": {"type": "string"},
                    },
                    "required": ["contact_id"],
                },
            },
        }
