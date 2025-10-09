from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomerDetailsByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "") -> str:
        customer_id = customer_id.strip()
        if not customer_id:
            return json.dumps(
                {"error": "customer_id is required."},
                indent=2
            )

        customer = next(
            (c for c in data.get("customers", {}).values()
             if c.get("customer_id") == customer_id),
            None
        )
        if not customer:
            return json.dumps(
                {"error": f"Customer '{customer_id}' not found."},
                indent=2
            )

        return json.dumps(customer, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsByCustomerId",
                "description": "Fetches the complete customer record for the given customer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
