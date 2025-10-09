from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchCustomersByEmailTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email_domain: str = '', partial_email: str = '') -> str:
        customers = data.get('customers', {}).values()
        matches = []

        for customer in customers.values():
            email = customer['contact_info']['email_address']

            if email_domain and email.endswith(f"@{email_domain}"):
                matches.append({
                    'customer_id': customer['customer_id'],
                    'name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': email
                })
            elif partial_email and partial_email.lower() in email.lower():
                matches.append({
                    'customer_id': customer['customer_id'],
                    'name': f"{customer['personal_info']['first_name']} {customer['personal_info']['last_name']}",
                    'email': email
                })

        return json.dumps(matches, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCustomersByEmail",
                "description": "Search customers by email domain or partial email",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_domain": {"type": "string", "description": "Email domain to search for"},
                        "partial_email": {"type": "string", "description": "Partial email address to match"}
                    }
                }
            }
        }
