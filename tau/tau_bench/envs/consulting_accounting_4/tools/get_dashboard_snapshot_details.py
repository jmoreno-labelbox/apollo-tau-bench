from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetDashboardSnapshotDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, snapshot_date: str = None) -> str:
        snaps = data.get("dashboard_snapshots", [])
        row = None
        if snapshot_id is not None:
            row = next(
                (s for s in snaps if str(s.get("snapshot_id")) == str(snapshot_id)), None
            )
        elif snapshot_date:
            row = next((s for s in snaps if s.get("snapshot_date") == snapshot_date), None)
        if not row:
            payload = {"error": "Snapshot not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDashboardSnapshotDetails",
                "description": "Fetch a snapshot by id or by snapshot_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
