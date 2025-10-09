from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetBeneficiaryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None) -> str:
        beneficiary = next((b for b in data.get('beneficiaries', []) if b.get('beneficiary_id') == beneficiary_id), None)

        if beneficiary:
            return json.dumps(beneficiary)
        return json.dumps({"error": "Beneficiary not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetBeneficiaryDetails",
                        "description": "Looks up a beneficiary by their unique beneficiary ID and displays the details.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "beneficiary_id": {"type": "string", "description": "The unique ID of the beneficiary."}
                                },
                                "required": ["beneficiary_id"]
                        }
                }
        }
