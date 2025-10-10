# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListBeneficiaries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        customer_beneficiaries = [b for b in data['beneficiaries'] if b['customer_id'] == customer_id]
        return json.dumps(customer_beneficiaries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_beneficiaries",
                        "description": "Lists all beneficiaries for a given customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {"customer_id": {"type": "string"}},
                                "required": ["customer_id"]
                        }
                }
        }
