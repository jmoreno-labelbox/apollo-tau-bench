# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateProjectRevenue(Tool):
    """Create project revenue record for dashboard snapshot."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_id = kwargs.get("row_id")
        snapshot_id = kwargs.get("snapshot_id")
        project_id = kwargs.get("project_id")
        ytd_revenue = kwargs.get("ytd_revenue")

        if not all([row_id, snapshot_id, project_id, ytd_revenue]):
            return _error("Required fields: row_id, snapshot_id, project_id, ytd_revenue")

        project_revenue = {
            "row_id": row_id,
            "snapshot_id": snapshot_id,
            "project_id": project_id,
            "ytd_revenue": ytd_revenue
        }

        data.setdefault("project_revenue", []).append(project_revenue)

        return _ok(row_id=row_id, project_id=project_id, ytd_revenue=ytd_revenue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_project_revenue",
                "description": "Create a project revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "ytd_revenue": {"type": "number"}
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "ytd_revenue"],
                },
            },
        }
