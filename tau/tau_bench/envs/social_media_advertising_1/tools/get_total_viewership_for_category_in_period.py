# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalViewershipForCategoryInPeriod(Tool):
    """Calculates total viewership for a category over a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        viewership_data = list(data.get("f_viewership", {}).values())
        
        total_sessions = 0
        total_active_users = 0
        
        for entry in viewership_data:
            if (entry.get("category") == category and 
                start_date <= entry.get("date") <= end_date):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
        
        return json.dumps({
            "total_sessions": total_sessions,
            "total_active_users": total_active_users
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_total_viewership_for_category_in_period",
                "description": "Calculates total viewership for a category over a date range.",
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
