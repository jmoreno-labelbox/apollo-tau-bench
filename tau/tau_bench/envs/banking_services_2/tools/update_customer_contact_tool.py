from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCustomerContactTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, email: str = None, phone: str = None) -> str:
        customers = data.get('customers', {}).values()

        for customer in customers.values():
            if customer['customer_id'] == customer_id:
                if email:
                    customer['contact_info']['email_address'] = email
                if phone:
                    for phone_entry in customer['contact_info']['phone_numbers']:
                        if phone_entry['is_primary']:
                            phone_entry['number'] = phone
                            break

                return json.dumps({
                    "customer_id": customer_id,
                    "updated_email": email,
                    "updated_phone": phone,
                    "status": "Updated"
                }, indent=2)

        return json.dumps({"error": f"Customer {customer_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerContact",
                "description": "Update customer contact information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "email": {"type": "string", "description": "New email address"},
                        "phone": {"type": "string", "description": "New phone number"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
