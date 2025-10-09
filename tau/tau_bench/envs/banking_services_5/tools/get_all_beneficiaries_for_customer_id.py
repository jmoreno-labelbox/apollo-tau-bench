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
        return list(db.values())
    return db

class GetAllBeneficiariesForCustomerId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        all_benes = [
            bene for bene in data.get("beneficiaries", [])
            if bene.get("customer_id") == customer_id
        ]

        return json.dumps(all_benes, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllBeneficiariesForCustomerId",
                "description": "Returns a list of all beneficiary records for a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose beneficiaries you want to retrieve"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
