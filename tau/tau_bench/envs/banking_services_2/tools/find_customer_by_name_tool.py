# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCustomerByNameTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name = '', last_name = '') -> str:
        first_name = first_name.lower()
        last_name = last_name.lower()
        customers = list(data.get('customers', {}).values())

        matches = []
        for customer in customers:
            if (customer['personal_info']['first_name'].lower() == first_name and
                customer['personal_info']['last_name'].lower() == last_name):
                matches.append({
                    'customer_id': customer['customer_id'],
                    'full_name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': customer['contact_info']['email_address']
                })

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_customer_by_name",
                "description": "Find customer records by first and last name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "Customer's first name"},
                        "last_name": {"type": "string", "description": "Customer's last name"}
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        }
