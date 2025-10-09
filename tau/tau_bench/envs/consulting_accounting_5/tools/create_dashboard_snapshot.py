from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        notes: str = "Year-end snapshot",
        snapshot_date: str = None,
        snapshot_id: str = None,
        year: Any = None
    ) -> str:
        """
        Create a new dashboard snapshot.
        """
        new_snapshot = {
            "snapshot_id": snapshot_id,
            "snapshot_date": snapshot_date,
            "notes": notes
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
