from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddPromotion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        promotion_id: str,
        name: str,
        description: str,
        discount_type: str,
        value: float,
        start_date: str,
        end_date: str
    ) -> str:
        promotions = data.get("promotions", [])

        if any(p.get("promotion_id") == promotion_id for p in promotions):
            payload = {"error": f"Promotion with ID {promotion_id} already exists."}
            out = json.dumps(payload)
            return out

        new_promotion = {
            "promotion_id": promotion_id,
            "name": name,
            "description": description,
            "discount_type": discount_type,
            "value": value,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        promotions.append(new_promotion)
        data["promotions"] = promotions
        payload = new_promotion
        out = json.dumps(payload, indent=2)
        return out
        pass
        promotions = data.get("promotions", [])

        if any(p.get("promotion_id") == promotion_id for p in promotions):
            payload = {"error": f"Promotion with ID {promotion_id} already exists."}
            out = json.dumps(
                payload)
            return out

        new_promotion = {
            "promotion_id": promotion_id,
            "name": name,
            "description": description,
            "discount_type": discount_type,
            "value": value,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        promotions.append(new_promotion)
        data["promotions"] = promotions
        payload = new_promotion
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPromotion",
                "description": "Add a new promotion to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "Unique identifier for the promotion.",
                        },
                        "name": {
                            "type": "string",
                            "description": "Name of the promotion.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of the promotion.",
                        },
                        "discount_type": {
                            "type": "string",
                            "description": "Type of discount (percentage or fixed).",
                        },
                        "value": {"type": "number", "description": "Discount value."},
                        "start_date": {
                            "type": "string",
                            "description": "Start date of the promotion (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date of the promotion (YYYY-MM-DD).",
                        },
                    },
                    "required": [
                        "promotion_id",
                        "name",
                        "description",
                        "discount_type",
                        "value",
                        "start_date",
                        "end_date",
                    ],
                },
            },
        }
