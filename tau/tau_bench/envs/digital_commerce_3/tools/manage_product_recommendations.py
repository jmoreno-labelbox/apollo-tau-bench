from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ManageProductRecommendations(Tool):
    """Create and oversee product suggestions for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        contact_id: Any,
        recommendation_type: Any = "similar_products",
        contacts: list = None,
        products: list = None
    ) -> str:
        pass
        contact_id = _idstr(contact_id)
        recommendation_type = f"{recommendation_type}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = contacts if contacts is not None else data.get("contacts", {}).values()
        contact = _find_one(list(contacts.values()), "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        products = products if products is not None else data.get("products", {}).values()
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
        payload = {
                "contact_id": contact_id,
                "recommendation_type": recommendation_type,
                "recommendations": recommendation_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        recommendation_type = f"{recommendation_type}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", {}).values()
        contact = _find_one(list(contacts.values()), "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        products = data.get("products", {}).values()
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
        payload = {
                "contact_id": contact_id,
                "recommendation_type": recommendation_type,
                "recommendations": recommendation_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageProductRecommendations",
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
