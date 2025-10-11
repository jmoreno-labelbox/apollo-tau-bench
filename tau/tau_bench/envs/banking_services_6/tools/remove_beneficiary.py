# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id) -> str:
        beneficiaries = list(data.get('beneficiaries', {}).values())

        initial_len = len(beneficiaries)
        data['beneficiaries'] = [b for b in beneficiaries if b['beneficiary_id'] != beneficiary_id]

        if len(data['beneficiaries']) < initial_len:
            return json.dumps({"status": "Success", "beneficiary_id": beneficiary_id, "action": "removed"})
        return json.dumps({"error": "Beneficiary not found or could not be removed."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "remove_beneficiary",
                        "description": "Removes a beneficiary from the database.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "beneficiary_id": {"type": "string", "description": "The unique ID of the beneficiary to remove."}
                                },
                                "required": ["beneficiary_id"]
                        }
                }
        }
