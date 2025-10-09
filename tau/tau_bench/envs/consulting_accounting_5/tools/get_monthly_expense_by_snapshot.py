from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetMonthlyExpenseBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        for record in data.get("monthly_expenses", []):
            if record["snapshot_id"] == snapshot_id:
                return json.dumps(record["row_id"])
        return None
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyExpenseBySnapshot",
                "description": "Get monthly expense for a given snapshot_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
