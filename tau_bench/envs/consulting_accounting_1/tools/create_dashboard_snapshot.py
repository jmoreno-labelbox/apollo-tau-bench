from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_date: str = None, ytd_revenue: float = None, ytd_tax_reserve: float = None, pdf_path: str = None) -> str:
        required = ["snapshot_date", "ytd_revenue", "ytd_tax_reserve", "pdf_path"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for k in required:
            if params_dict.get(k) is None:
                payload = {"error": f"{k} is required"}
                out = json.dumps(payload, indent=2)
                return out
        snaps = data.setdefault("dashboard_snapshots", [])
        new_id = f"SNAP-AUTO-{len(snaps)+1:03d}"
        record = {
            "snapshot_id": new_id,
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path,
        }
        snaps.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshot",
                "description": "Append a new dashboard snapshot with artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_date": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": [
                        "snapshot_date",
                        "ytd_revenue",
                        "ytd_tax_reserve",
                        "pdf_path",
                    ],
                },
            },
        }
