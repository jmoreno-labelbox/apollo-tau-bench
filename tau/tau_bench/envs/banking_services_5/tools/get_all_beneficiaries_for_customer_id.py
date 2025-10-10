# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllBeneficiariesForCustomerId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        all_benes = [
            bene for bene in list(data.get("beneficiaries", {}).values())
            if bene.get("customer_id") == customer_id
        ]


        return json.dumps(all_benes, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_beneficiaries_for_customer_id",
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
