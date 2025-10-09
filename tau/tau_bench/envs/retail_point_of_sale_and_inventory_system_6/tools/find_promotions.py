from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_promotions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        promotion_id: str = None,
        type: str = None,
        status: str = None,
        name: str = None,
        description: str = None,
        has_sku: str = None
    ) -> str:
        promotions = data.get("promotions", [])

        # If customer id is provided, it will take precedence over all other criteria

        # These columns will match precisely with the provided value
        exact_match_cols = ["type", "status"]
        exact_match_values = {"type": type, "status": status}

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "description"]
        approximate_match_values = {"name": name, "description": description}

        # These columns possess unique matching criteria
        special_match_cols = ["has_sku"]
        special_match_values = {"has_sku": has_sku}

        matches = []
        for promotion in promotions:
            # customer_id is prioritized
            if (promotion_id is not None) and (
                promotion["promotion_id"] == promotion_id
            ):
                payload = promotion
                out = json.dumps(payload, indent=2)
                return out

            # Add to the return list if all provided criteria align
            elif (
                all(
                    [
                        exact_match_values[k] == promotion[k]
                        for k in exact_match_values.keys()
                        if exact_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        approximate_match_values[k].lower() in promotion[k].lower()
                        for k in approximate_match_values.keys()
                        if approximate_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        (
                            special_match_values["has_sku"]
                            in promotion["applicable_skus"]
                            if special_match_values["has_sku"] is not None
                            else True
                        )
                    ]
                )
            ):
                matches.append(promotion)
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindPromotions",
                "description": "Finds promotions matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The id of the promotion to return. If found, the function will return only the promotion matching the promotion_id",
                        },
                        "type": {
                            "type": "string",
                            "description": "type of the promotion. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the promotion. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the promotion. Will do an approximate match",
                        },
                        "description": {
                            "type": "string",
                            "description": "description of the promotion. Will do an approximate match",
                        },
                        "has_sku": {
                            "type": "string",
                            "description": "Will find promotions that apply to the sent sku",
                        },
                    },
                },
            },
        }
