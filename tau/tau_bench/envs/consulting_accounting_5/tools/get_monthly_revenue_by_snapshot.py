# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMonthlyRevenueBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns row_ids of monthly revenue for a given snapshot_id.
        """
        snapshot_id = kwargs["snapshot_id"]
        records = [mr["row_id"] for mr in data["monthly_revenue"] if mr["snapshot_id"] == snapshot_id]
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
