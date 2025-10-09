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

class RemoveBeneficiaryByBeneficiaryId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_id: str = None) -> str:
        if not customer_id or not beneficiary_id:
            return json.dumps({"error": "customer_id and beneficiary_id are required."}, indent=2)

        beneficiaries = data.get("beneficiaries", {}).values()
        for i, beneficiary in enumerate(beneficiaries.values()):
            if (beneficiary.get("beneficiary_id") == beneficiary_id
                    and beneficiary.get("customer_id") == customer_id):
                del beneficiaries[i]
                return json.dumps({
                    "status": "Beneficiary removed successfully."
                }, indent=2)

        return json.dumps({"error": "Beneficiary not found for this customer."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "description": "Removes a beneficiary from the database using the beneficiary ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Unique ID of the beneficiary to be removed"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }
