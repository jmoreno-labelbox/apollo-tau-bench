from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CreateProjectRevenue(Tool):
    """Generate a project revenue entry for the dashboard snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], row_id: str = None, snapshot_id: str = None, project_id: str = None, ytd_revenue: float = None) -> str:
        if not all([row_id, snapshot_id, project_id, ytd_revenue]):
            return _error(
                "Required fields: row_id, snapshot_id, project_id, ytd_revenue"
            )

        project_revenue = {
            "row_id": row_id,
            "snapshot_id": snapshot_id,
            "project_id": project_id,
            "ytd_revenue": ytd_revenue,
        }

        data.setdefault("project_revenue", []).append(project_revenue)

        return _ok(row_id=row_id, project_id=project_id, ytd_revenue=ytd_revenue)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateProjectRevenue",
                "description": "Create a project revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "ytd_revenue"],
                },
            },
        }
