# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPromotionByNameAndDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], promotion_name, query_date) -> str:
        query_date_str = query_date
        promotions = list(data.get("promotions", {}).values())

        if not query_date_str:
            return json.dumps({})

        try:
            query_date = datetime.strptime(query_date_str, "%Y-%m-%d").date()
        except ValueError:
            return json.dumps({"error": "Invalid date format for query_date. Use YYYY-MM-DD."})

        for promo in promotions:
            if promo.get("name") == promotion_name:
                start_date_str = promo.get("start_date", "").split("T")[0]
                end_date_str = promo.get("end_date", "").split("T")[0]

                if promo.get("status") == "active" and start_date_str and end_date_str:
                    try:
                        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                        if start_date <= query_date <= end_date:
                            return json.dumps(promo)
                    except ValueError:
                        continue
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotion_by_name_and_date",
                "description": "Retrieves details of a promotion by its name, only if it is active on the specified query date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_name": {
                            "type": "string",
                            "description": "The name of the promotion.",
                        },
                        "query_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The date to check for promotion activity (YYYY-MM-DD).",
                        },
                    },
                    "required": ["promotion_name", "query_date"],
                },
            },
        }
