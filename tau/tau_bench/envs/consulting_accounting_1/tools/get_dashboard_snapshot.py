from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None) -> str:
        snaps = data.get("dashboard_snapshots", [])
        snap = next((s for s in snaps if s.get("snapshot_id") == snapshot_id), None)
        payload = snap or {"error": f"Snapshot {snapshot_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDashboardSnapshot",
                "description": "Get a dashboard snapshot by snapshot_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"snapshot_id": {"type": "string"}},
                    "required": ["snapshot_id"],
                },
            },
        }
