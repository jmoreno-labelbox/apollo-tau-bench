from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetupScheduledPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, from_account_id: str = None, 
               beneficiary_id: str = None, amount: float = None, frequency: str = None, 
               start_date: str = None) -> str:
        scheduled_payments = data.get('scheduled_payments', {}).values()

        payment_id = f"sched_{generate_unique_id()}"

        new_payment = {
            "payment_id": payment_id,
            "customer_id": customer_id,
            "from_account_id": from_account_id,
            "beneficiary_id": beneficiary_id,
            "amount": amount,
            "frequency": frequency,
            "start_date": start_date,
            "status": "Active",
            "created_date": get_current_timestamp(),
            "next_payment_date": start_date
        }

        data["scheduled_payments"][new_payment["scheduled_payment_id"]] = new_payment

        return json.dumps({
            "payment_id": payment_id,
            "status": "Active",
            "next_payment_date": start_date,
            "amount": amount,
            "frequency": frequency
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetupScheduledPayment",
                "description": "Setup a recurring scheduled payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "from_account_id": {"type": "string", "description": "Source account"},
                        "beneficiary_id": {"type": "string", "description": "Beneficiary identifier"},
                        "amount": {"type": "number", "description": "Payment amount"},
                        "frequency": {"type": "string", "description": "Payment frequency", "enum": ["Weekly", "Monthly", "Quarterly"]},
                        "start_date": {"type": "string", "description": "First payment date (YYYY-MM-DD)"}
                    },
                    "required": ["customer_id", "from_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                }
            }
        }
