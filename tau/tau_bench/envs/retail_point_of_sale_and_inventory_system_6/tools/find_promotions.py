# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_promotions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotions = data.get("promotions", [])

        # If customer id is sent, then it will override all other criteria
        promotion_id = kwargs.get("promotion_id")

        # These columns will be matched exactly to the value sent
        exact_match_cols = ["type", "status"]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "description"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        # These columns have special matching criteria
        special_match_cols = ["has_sku"]
        special_match_values = {k: kwargs.get(k) for k in special_match_cols}

        matches = []
        for promotion in promotions:
            # customer_id takes priority
            if (promotion_id is not None) and (
                promotion["promotion_id"] == promotion_id
            ):
                return json.dumps(promotion, indent=2)

            # If all sent criteria match, then add it to the return list
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

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_promotions",
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
