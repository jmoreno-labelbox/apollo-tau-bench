# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EditPromotionsDb(Tool): # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        promotion_id: str = None,
        name: str = None,
        type: str = None,
        discount_value: float = None,
        description: str = None,
        applicable_skus: list = None,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        usage_limit: int = None,
        times_used: int = None,
        delete: bool = False
    ) -> str:
        db = data.get("promotions", [])
        if promotion_id:
            idx, row = _find_by_id(db, "promotion_id", promotion_id)
            if row:
                if delete:
                    # --- DELETE ---
                    del db[idx]
                    return json.dumps({"result": "deleted"})
                else:
                    # --- UPDATE ---
                    if name is not None: row["name"] = name
                    if type is not None: row["type"] = type
                    if discount_value is not None: row["discount_value"] = discount_value
                    if description is not None: row["description"] = description
                    if applicable_skus is not None: row["applicable_skus"] = applicable_skus
                    if start_date is not None: row["start_date"] = start_date
                    if end_date is not None: row["end_date"] = end_date
                    if status is not None: row["status"] = status
                    if usage_limit is not None: row["usage_limit"] = usage_limit
                    if times_used is not None: row["times_used"] = times_used
                    return json.dumps({"result": row})
            else:
                return json.dumps({"error": f"Promotion {promotion_id} not found"})
        else:
            # --- CREATE ---
            if not promotion_id:
                promotion_id = f"PROMO-{1000 + len(db) + 1}"
            if name is None or type is None or discount_value is None or applicable_skus is None or start_date is None:
                return json.dumps({"error": "Missing required field for creation (name, type, discount_value, applicable_skus)"})
            new_row = {
                "promotion_id": promotion_id,
                "name": name,
                "type": type,
                "discount_value": discount_value,
                "description": description if description is not None else "No description",
                "applicable_skus": applicable_skus,
                "start_date": start_date if len(start_date)<10 else start_date[:10],
                "end_date": end_date if end_date is not None else "9999-12-31",
                "status": status if status is not None else "active",
                "usage_limit": usage_limit if usage_limit is not None else 0,
                "times_used": times_used if times_used is not None else 0,
            }
            db.append(new_row)
            return json.dumps({"result": new_row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "edit_promotions_db",
                "description": "Create, update, or delete a promotion row by promotion_id. If delete is True, deletes the row. If promotion_id is given it will edit the row with the given information. If no promotion_id is given, it will create a new row with the given info, as long as name, type, discount_value, applicable_skus, start_date, end_date, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {"type": "string", "default": None, "description": "The promotion id to edit or delete. If not provided, a new id will be generated."},
                        "delete": {"type": "boolean", "default": False, "description": "Whether to delete the specified promotion."},
                        "name": {"type": "string", "default": None, "description": "Name of the promotion."},
                        "type": {"type": "string", "default": None, "description": "Type of promotion."},
                        "discount_value": {"type": "number", "default": None, "description": "Discount value."},
                        "description": {"type": "string", "default": None, "description": "Description of the promotion."},
                        "applicable_skus": {"type": "array", "items": {"type": "string"}, "default": None, "description": "SKUs to which the promotion applies. If empty, applies to all products."},
                        "start_date": {"type": "string", "default": None, "description": "Start date of the promotion."},
                        "end_date": {"type": "string", "default": None, "description": "End date of the promotion."},
                        "status": {"type": "string", "default": None, "description": "Status of the promotion."},
                        "usage_limit": {"type": "integer", "default": None, "description": "Usage limit for the promotion."},
                        "times_used": {"type": "integer", "default": None, "description": "Number of times the promotion has been used."},
                        "current_time": {"type": "string", "default": None, "description": "Current timestamp for created_at/updated_at."}
                    },
                    "required": []
                }
            }
        }
