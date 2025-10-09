from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchDashboardSnapshot(Tool):
    """Retrieve a dashboard snapshot using id or date."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, snapshot_date: str = None) -> str:
        snaps = data.get("dashboard_snapshots", {}).values()
        sid = snapshot_id
        sdate = snapshot_date
        row = None
        if sid is not None:
            row = next(
                (s for s in snaps.values() if str(s.get("snapshot_id")) == str(sid)), None
            )
        elif sdate:
            row = next((s for s in snaps.values() if s.get("snapshot_date") == sdate), None)
        if not row:
            payload = {"error": "snapshot not found"}
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
                "name": "FetchDashboardSnapshot",
                "description": "Read a snapshot by id or date.",
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
