from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalBeneficiariesCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("beneficiaries", []))
        return json.dumps({"total_beneficiaries": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalBeneficiariesCount",
                        "description": "Returns the current total number of beneficiaries in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
