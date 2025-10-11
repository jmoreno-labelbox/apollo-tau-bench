# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id) -> str:
        sid = snapshot_id
        snaps = list(data.get("dashboard_snapshots", {}).values())
        snap = next((s for s in snaps if s.get("snapshot_id") == sid), None)
        return json.dumps(snap or {"error": f"Snapshot {sid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_dashboard_snapshot","description": "Get a dashboard snapshot by snapshot_id.","parameters": {"type": "object","properties": {"snapshot_id": {"type": "string"}},"required": ["snapshot_id"]}}}
