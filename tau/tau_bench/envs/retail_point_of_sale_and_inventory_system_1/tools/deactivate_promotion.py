from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeactivatePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "inactive"
                payload = {"promotion_id": promotion_id, "status": "inactive"}
                out = json.dumps(payload)
                return out
        payload = {"promotion_id": promotion_id, "status": "not_found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeactivatePromotion",
                "description": "Deactivates a promotion by setting its status to 'inactive'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to deactivate.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }
