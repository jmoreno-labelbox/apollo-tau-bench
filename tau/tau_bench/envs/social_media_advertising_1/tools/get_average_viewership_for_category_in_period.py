# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAverageViewershipForCategoryInPeriod(Tool):
    """Calculates average daily viewership for a category over a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], category, end_date, start_date) -> str:
        viewership_data = list(data.get("f_viewership", {}).values())
        
        # Determine the total days within the specified timeframe.
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1
        
        total_sessions = 0
        total_active_users = 0
        days_with_data = 0
        
        for entry in viewership_data:
            if (entry.get("category") == category and 
                start_date <= entry.get("date") <= end_date):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
                days_with_data += 1
        
        # Compute averages
        avg_sessions = total_sessions / days_in_period if days_in_period > 0 else 0
        avg_active_users = total_active_users / days_in_period if days_in_period > 0 else 0
        
        return json.dumps({
            "average_sessions": avg_sessions,
            "average_active_users": avg_active_users,
            "days_in_period": days_in_period,
            "days_with_data": days_with_data
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_average_viewership_for_category_in_period",
                "description": "Calculates average daily viewership for a category over a date range.",
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
