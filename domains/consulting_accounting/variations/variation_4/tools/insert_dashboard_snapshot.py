from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class InsertDashboardSnapshot(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        snapshot_date: str = None, 
        ytd_revenue: float = None, 
        ytd_tax_reserve: float = None, 
        pdf_path: str = None
    ) -> str:
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
            "pdf_path": pdf_path,
        }
        snaps.append(row)
        payload = {"snapshot_id": new_id, "snapshot_date": row["snapshot_date"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertDashboardSnapshot",
                "description": "Create a dashboard snapshot row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_date": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": ["snapshot_date"],
                },
            },
        }
