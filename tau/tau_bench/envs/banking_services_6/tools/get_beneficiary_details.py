# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBeneficiaryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id) -> str:
        beneficiary = next((b for b in list(data.get('beneficiaries', {}).values()) if b.get('beneficiary_id') == beneficiary_id), None)

        if beneficiary:
            return json.dumps(beneficiary)
        return json.dumps({"error": "Beneficiary not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_beneficiary_details",
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
