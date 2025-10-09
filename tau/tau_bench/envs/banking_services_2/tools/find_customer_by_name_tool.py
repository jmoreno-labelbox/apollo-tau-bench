from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindCustomerByNameTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = '', last_name: str = '') -> str:
        first_name = first_name.lower()
        last_name = last_name.lower()
        customers = data.get('customers', [])

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
                "name": "FindCustomerByName",
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
