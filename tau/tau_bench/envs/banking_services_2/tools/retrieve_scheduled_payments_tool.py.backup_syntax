from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RetrieveScheduledPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, month: str = None, frequency: Any = None, source_account_ids: list = None) -> str:
        # Support source_account_ids parameter
        if source_account_ids and not source_account_id:
            source_account_id = source_account_ids[0] if source_account_ids else None
        scheduled_payments = data.get('scheduled_payments', {}).values()
        results = []

        for payment in scheduled_payments.values()):
            if payment.get('customer_id') != customer_id:
                continue
            if payment.get('from_account_id', None) != source_account_id:
                continue
            next_payment_date = payment.get('next_payment_date', '')
            if not next_payment_date.startswith(month):
                continue
            if frequency and payment.get('frequency') not in frequency:
                continue
            results.append({
                "payment_id": payment.get("payment_id"),
                "amount": payment.get("amount"),
                "frequency": payment.get("frequency"),
                "next_payment_date": payment.get("next_payment_date"),
                "status": payment.get("status"),
                "beneficiary_id": payment.get("beneficiary_id"),
                "from_account_id": payment.get("from_account_id", "N/A"),
            })

        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveScheduledPayments",
                "description": "Retrieve scheduled payments for a customer and account, with optional month and frequency filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "source_account_id": {"type": "string", "description": "Source account identifier"},
                        "month": {"type": "string", "description": "Filter payments scheduled for this month (YYYY-MM)"},
                        "frequency": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by frequency (e.g. Monthly, Weekly)"
                        }
                    },
                    "required": ["customer_id", "source_account_id", "month"]
                }
            }
        }
