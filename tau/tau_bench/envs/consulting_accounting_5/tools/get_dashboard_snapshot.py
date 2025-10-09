from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns the snapshot_id if found.
        """
        snapshot = next((s for s in data["dashboard_snapshots"].values() if s["snapshot_id"] == snapshot_id), None)
        return json.dumps(snapshot["snapshot_id"] if snapshot else None)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDashboardSnapshot",
                "description": "Retrieve a financial dashboard snapshot by snapshot_id (returns only the snapshot_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Unique ID of the snapshot"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
