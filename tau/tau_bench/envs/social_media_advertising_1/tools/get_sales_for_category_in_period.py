# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSalesForCategoryInPeriod(Tool):
    """Retrieves sales data for a specific category and date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], category, end_date, start_date) -> str:
        sales_data = list(data.get("f_sales", {}).values())
        
        matching_sales = []
        
        for entry in sales_data:
            if (entry.get("category") == category and 
                entry.get("start_date") >= start_date and 
                entry.get("end_date") <= end_date):
                matching_sales.append(entry)
        
        return json.dumps({"sales_data": matching_sales})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sales_for_category_in_period",
                "description": "Retrieves sales data for a specific category and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        }
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }
