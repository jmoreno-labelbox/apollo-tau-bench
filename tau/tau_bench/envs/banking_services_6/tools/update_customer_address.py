from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class UpdateCustomerAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, street_address: str = None, city: str = None, state: str = None, postal_code: str = None, country: str = None) -> str:
        for customer in data.get("customers", []):
            if customer.get("customer_id") == customer_id:
                new_address = {
                    "street_address": street_address,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code,
                    "country": country
                }
                customer["contact_info"]["mailing_address"] = new_address
                customer["contact_info"]["residential_address"] = new_address
                return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerAddress",
                        "description": "Updates the mailing and residential address for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                                        "street_address": {"type": "string", "description": "The new street address."},
                                        "city": {"type": "string", "description": "The new city."},
                                        "state": {"type": "string", "description": "The new state or province."},
                                        "postal_code": {"type": "string", "description": "The new postal code."},
                                        "country": {"type": "string", "description": "The new country."}
                                },
                                "required": ["customer_id", "street_address", "city", "state", "postal_code", "country"],
                        },
                },
        }
