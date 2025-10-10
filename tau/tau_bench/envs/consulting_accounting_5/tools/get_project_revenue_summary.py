# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectRevenueSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id) -> str:
        """
        Returns row_ids of project revenue for a given snapshot_id.
        """
        records = [pr["row_id"] for pr in data["project_revenue"] if pr["snapshot_id"] == snapshot_id]
        return json.dumps(records)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectRevenueSummary",
                "description": "Retrieve project revenue row_ids tied to a snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter project revenue"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
