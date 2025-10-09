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

class GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", beneficiary_id: str = "") -> str:
        customer_id = customer_id.strip()
        beneficiary_id = beneficiary_id.strip()

        if not customer_id or not beneficiary_id:
            return json.dumps({
                "error": "customer_id and beneficiary_id are required."
            }, indent=2)

        scheduled_payments = data.get("scheduled_payments", {}).values()
        for payment in scheduled_payments.values():
            if payment.get("customer_id") == customer_id and payment.get("beneficiary_id") == beneficiary_id:
                return json.dumps(payment, indent=2)

        return json.dumps({
            "error": "No scheduled payment found for the given customer and beneficiary."
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "description": "Returns a scheduled payment using customer ID and beneficiary ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "ID of the beneficiary"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }
