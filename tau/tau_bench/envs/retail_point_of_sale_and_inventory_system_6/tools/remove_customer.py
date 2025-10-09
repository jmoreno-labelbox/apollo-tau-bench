from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class remove_customer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None) -> str:
        customers = data.get("customers", [])

        if customer_id is None:
            payload = {"error": "customer_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for customer in customers:
            if customer["customer_id"] == customer_id:
                del customer
                payload = {"success": f"Removed customer: {customer_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "No customer found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeCustomer",
                "description": "Removes a customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer to remove",
                        },
                    },
                },
            },
        }
