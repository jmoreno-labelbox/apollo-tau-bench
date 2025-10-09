from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2CreateDashboardSnapshot(Tool):
    """Generate a dashboard snapshot displaying current financial metrics."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        snapshot_id: str = None,
        snapshot_date: str = None,
        ytd_revenue: float = None,
        ytd_tax_reserve: float = None,
        pdf_path: str = None
    ) -> str:
        if not snapshot_date:
            return _error("snapshot_date is required")

        snapshot = {
            "snapshot_id": snapshot_id
            or f"SNAP{len(data.get('dashboard_snapshots', {})) + 1:03d}",
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue or 0.0,
            "ytd_tax_reserve": ytd_tax_reserve or 0.0,
            "pdf_path": pdf_path
            or f"/dashboards/{snapshot_date[:4]}/dashboard_{snapshot_date}.pdf",
        }

        data.setdefault("dashboard_snapshots", []).append(snapshot)

        return _ok(snapshot_id=snapshot_id, snapshot_date=snapshot_date)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateDashboardSnapshot",
                "description": "Create a financial dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string", "format": "date"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": ["snapshot_date"],
                },
            },
        }
