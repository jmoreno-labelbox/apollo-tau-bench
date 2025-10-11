# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalBeneficiariesCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        count = len(list(data.get("beneficiaries", {}).values()))
        return json.dumps({"total_beneficiaries": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_beneficiaries_count",
                        "description": "Returns the current total number of beneficiaries in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
