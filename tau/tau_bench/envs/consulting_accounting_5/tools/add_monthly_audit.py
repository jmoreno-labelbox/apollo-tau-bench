# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMonthlyAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, month, snapshot_id) -> str:
        """
        Insert or update monthly expense for a given snapshot.
        Deterministic: keyed by snapshot_id + month.
        """

        record = {
            "row_id": snapshot_id+"_"+month,
            "snapshot_id": snapshot_id,
            "month_year": month,
            "amount": amount
        }
        data.setdefault("monthly_expenses", []).append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMonthlyAudit",
                "description": "Insert or update monthly expense for a given snapshot_id and month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "amount": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "amount"],
                },
            },
        }
