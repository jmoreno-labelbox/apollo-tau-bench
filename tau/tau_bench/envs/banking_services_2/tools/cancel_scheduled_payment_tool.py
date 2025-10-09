from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CancelScheduledPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str, reason: str = 'Customer request') -> str:
        scheduled_payments = data.get('scheduled_payments', [])

        for payment in scheduled_payments:
            if payment['payment_id'] == payment_id:
                old_status = payment['status']
                payment['status'] = 'Cancelled'
                payment['cancellation_reason'] = reason
                payment['cancelled_date'] = get_current_timestamp()

                return json.dumps({
                    "payment_id": payment_id,
                    "old_status": old_status,
                    "new_status": "Cancelled",
                    "reason": reason,
                    "cancelled_date": payment['cancelled_date']
                }, indent=2)

        return json.dumps({"error": f"Scheduled payment {payment_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelScheduledPayment",
                "description": "Cancel a scheduled payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payment_id": {"type": "string", "description": "Scheduled payment identifier"},
                        "reason": {"type": "string", "description": "Cancellation reason"}
                    },
                    "required": ["payment_id"]
                }
            }
        }
