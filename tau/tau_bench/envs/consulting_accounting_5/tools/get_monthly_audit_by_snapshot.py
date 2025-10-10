# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMonthlyAuditBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns row_ids of monthly expenses for a given snapshot_id.
        """
        snapshot_id = kwargs["snapshot_id"]
        records = [me["row_id"] for me in data.get("monthly_expenses", []) if me["snapshot_id"] == snapshot_id]
        return json.dumps(records)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyAuditBySnapshot",
                "description": "Retrieve all monthly expense row_ids tied to a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter monthly expenses"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
