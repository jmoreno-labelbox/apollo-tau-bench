# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDashboardSnapshotDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snaps = data.get("dashboard_snapshots", [])
        sid = kwargs.get("snapshot_id")
        sdate = kwargs.get("snapshot_date")
        row = None
        if sid is not None:
            row = next((s for s in snaps if str(s.get("snapshot_id")) == str(sid)), None)
        elif sdate:
            row = next((s for s in snaps if s.get("snapshot_date") == sdate), None)
        if not row:
            return json.dumps({"error":"Snapshot not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_dashboard_snapshot_details",
            "description":"Fetch a snapshot by id or by snapshot_date.",
            "parameters":{"type":"object","properties":{"snapshot_id":{"type":"string"},"snapshot_date":{"type":"string"}},"required":[]}
        }}
