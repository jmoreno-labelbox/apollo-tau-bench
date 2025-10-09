from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CreateDashboardSnapshotWithInvoiceId(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        invoice_id: str,
        notes: str = "Year-end snapshot",
        pdf_path: str = None,
        snapshot_date: str = None,
        year: Any = None,
        ytd_revenue: float = None,
        ytd_tax_reserve: float = None
    ) -> str:
        """
        Create a new dashboard snapshot.
        """
        snapshot_id = f"SNAP_{invoice_id}"
        if pdf_path is None:
            pdf_path = f"/dashboards/2024/SNAP_{snapshot_date}.pdf"
        new_snapshot = {
            "snapshot_id": snapshot_id,
            "snapshot_date": snapshot_date,
            "notes": notes,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path
        }
        data["dashboard_snapshots"].append(new_snapshot)
        return json.dumps(new_snapshot["snapshot_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshotWithInvoiceId",
                "description": "Create a new financial dashboard snapshot for a given year with invoice id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": ["invoice_id", "snapshot_date", "year"],
                },
            },
        }
