# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDashboardSnapshotWithInvoiceId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, snapshot_date, ytd_revenue, ytd_tax_reserve, notes = "Year-end snapshot", pdf_path = f"/dashboards/2024/SNAP_{kwargs['snapshot_date']}.pdf") -> str:
        """
        Create a new dashboard snapshot.
        """
        snapshot_id = f"SNAP_{invoice_id}",
        new_snapshot = {
            "snapshot_id": str(snapshot_id[0]),
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
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": [ "snapshot_date", "year"],
                },
            },
        }
