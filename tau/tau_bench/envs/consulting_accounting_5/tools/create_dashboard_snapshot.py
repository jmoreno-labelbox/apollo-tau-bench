# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Create a new dashboard snapshot.
        """
        new_snapshot = {
            "snapshot_id": kwargs["snapshot_id"],
            "snapshot_date": kwargs["snapshot_date"],
            "notes": kwargs.get("notes", "Year-end snapshot")
        }
        data["dashboard_snapshots"].append(new_snapshot)
        return json.dumps(new_snapshot["snapshot_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshot",
                "description": "Create a new financial dashboard snapshot for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": ["snapshot_id", "snapshot_date", "year"],
                },
            },
        }
