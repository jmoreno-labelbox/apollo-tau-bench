from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetPromotionByNameAndDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_name: str = None, query_date: str = None) -> str:
        promotions = data.get("promotions", [])

        if not query_date:
            payload = {}
            out = json.dumps(payload)
            return out

        try:
            query_date_obj = datetime.strptime(query_date, "%Y-%m-%d").date()
        except ValueError:
            payload = {"error": "Invalid date format for query_date. Use YYYY-MM-DD."}
            out = json.dumps(payload)
            return out

        for promo in promotions:
            if promo.get("name") == promotion_name:
                start_date_str = promo.get("start_date", "").split("T")[0]
                end_date_str = promo.get("end_date", "").split("T")[0]

                if promo.get("status") == "active" and start_date_str and end_date_str:
                    try:
                        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                        if start_date <= query_date_obj <= end_date:
                            payload = promo
                            out = json.dumps(payload)
                            return out
                    except ValueError:
                        continue
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionByNameAndDate",
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
