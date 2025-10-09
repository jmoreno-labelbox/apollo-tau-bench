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

class GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None) -> str:
        beneficiary_name = beneficiary_name.strip().lower() if beneficiary_name else ""

        if not customer_id or not beneficiary_name:
            return json.dumps({
                "error": "Both customer_id and beneficiary_name are required."
            }, indent=2)

        beneficiaries = data.get("beneficiaries", {}).values()
        for beneficiary in beneficiaries.values():
            if (beneficiary.get("customer_id") == customer_id and
                beneficiary.get("beneficiary_name", "").strip().lower() == beneficiary_name):
                return json.dumps(beneficiary, indent=2)

        return json.dumps({"error": "Beneficiary not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "description": "Fetches the full details of a beneficiary using customer ID and beneficiary name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_name": {
                            "type": "string",
                            "description": "Full name of the beneficiary to match (case-insensitive)"
                        }
                    },
                    "required": ["customer_id", "beneficiary_name"]
                }
            }
        }
