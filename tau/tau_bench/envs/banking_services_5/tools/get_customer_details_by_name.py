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

class GetCustomerDetailsByName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = "", last_name: str = "") -> str:
        first_name = first_name.strip().lower()
        last_name = last_name.strip().lower()

        if not first_name or not last_name:
            return json.dumps({
                "error": "first_name and last_name are required."
            }, indent=2)

        customers = data.get("customers", {}).values()
        for customer in customers.values():
            pi = customer.get("personal_info", {}).values()
            if (
                pi.get("first_name", "").strip().lower() == first_name and
                pi.get("last_name", "").strip().lower() == last_name
            ):
                return json.dumps(customer, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsByName",
                "description": "Returns the full customer object based on first name and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Customer's first name"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer's last name"
                        }
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        }
