# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pdf_path, snapshot_date, ytd_revenue, ytd_tax_reserve) -> str:
        snaps = data.get("dashboard_snapshots", [])
        
        max_id = 0
        for s in snaps:
            try:
                snap_id = int(s.get("snapshot_id", 0))
                if snap_id > max_id:
                    max_id = snap_id
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1

        row = {
            "snapshot_id": new_id,
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path
        }
        snaps.append(row)
        return json.dumps({"snapshot_id": new_id, "snapshot_date": row["snapshot_date"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_dashboard_snapshot",
            "description":"Create a dashboard snapshot row.",
            "parameters":{"type":"object","properties":{
                "snapshot_date":{"type":"string"},
                "ytd_revenue":{"type":"number"},
                "ytd_tax_reserve":{"type":"number"},
                "pdf_path":{"type":"string"}
            },"required":["snapshot_date"]}
        }}
