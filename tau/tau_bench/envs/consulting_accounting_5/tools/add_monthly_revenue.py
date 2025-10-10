# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], month, revenue, snapshot_id) -> str:
        """
        Insert or update monthly revenue for a given snapshot.
        """

        record = {
            "row_id": "MON_"+snapshot_id,
            "snapshot_id": snapshot_id,
            "month_year": month,
            "revenue": revenue
        }
        data["monthly_revenue"].append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMonthlyRevenue",
                "description": "Insert or update monthly revenue for a given snapshot_id and month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "revenue": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "revenue"],
                },
            },
        }
