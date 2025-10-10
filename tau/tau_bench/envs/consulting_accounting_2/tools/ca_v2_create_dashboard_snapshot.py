# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateDashboardSnapshot(Tool):
    """Create a dashboard snapshot with current financial metrics."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snapshot_id = kwargs.get("snapshot_id")
        snapshot_date = kwargs.get("snapshot_date")
        ytd_revenue = kwargs.get("ytd_revenue")
        ytd_tax_reserve = kwargs.get("ytd_tax_reserve")
        pdf_path = kwargs.get("pdf_path")

        if not snapshot_date:
            return _error("snapshot_date is required")

        snapshot = {
            "snapshot_id": snapshot_id or f"SNAP{len(data.get('dashboard_snapshots', [])) + 1:03d}",
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue or 0.0,
            "ytd_tax_reserve": ytd_tax_reserve or 0.0,
            "pdf_path": pdf_path or f"/dashboards/{snapshot_date[:4]}/dashboard_{snapshot_date}.pdf"
        }

        data.setdefault("dashboard_snapshots", []).append(snapshot)

        return _ok(
            snapshot_id=snapshot_id,
            snapshot_date=snapshot_date
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_dashboard_snapshot",
                "description": "Create a financial dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string", "format": "date"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"}
                    },
                    "required": ["snapshot_date"],
                },
            },
        }
