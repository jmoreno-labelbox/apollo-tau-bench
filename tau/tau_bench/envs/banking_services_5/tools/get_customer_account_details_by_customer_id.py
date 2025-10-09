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
        return list(db.values())
    return db

class GetCustomerAccountDetailsByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({
                "error": "customer_id is required."
            }, indent=2)

        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("customer_id") == customer_id:
                return json.dumps(account, indent=2)

        return json.dumps({"error": "Account not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCustomerAccountDetailsByCustomerId",
                "description": (
                    "Returns the full account record for a customer using their customer_id "
                    "and the last 4 digits of their account number."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
