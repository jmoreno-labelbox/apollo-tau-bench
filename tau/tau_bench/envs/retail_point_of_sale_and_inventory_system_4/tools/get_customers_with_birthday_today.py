# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomersWithBirthdayToday(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], current_day: str) -> str:
        db = list(data.get("customers", {}).values())
        # current_day should be in "MM-DD" format
        result = []
        for row in db:
            birthdate = row.get("birthdate", "")
            # Accept birthdate in "YYYY-MM-DD" or "MM-DD"
            if len(birthdate) >= 5:
                birthdate = birthdate[-5:]
            if birthdate == current_day:
                result.append(row.get("customer_id"))
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customers_with_birthday_today",
                "description": "Return a list of customer IDs who have a birthday on the given day (MM-DD).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_day": {
                            "type": "string",
                            "description": "The current day in MM-DD format (e.g., '04-23')."
                        }
                    },
                    "required": ["current_day"]
                }
            }
        }
