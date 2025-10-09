from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetMonthlyRevenueBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns row_ids of monthly revenue for a given snapshot_id.
        """
        records = [mr["row_id"] for mr in data["monthly_revenue"].values() if mr["snapshot_id"] == snapshot_id]
        return json.dumps(records)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyRevenueBySnapshot",
                "description": "Retrieve all monthly revenue row_ids tied to a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter monthly revenue"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
