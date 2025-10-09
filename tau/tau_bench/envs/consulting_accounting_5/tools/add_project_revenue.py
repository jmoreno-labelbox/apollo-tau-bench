from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class AddProjectRevenue(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        project_id: int,
        revenue: float,
        row_id: int = None,
        snapshot_id: int = None
    ) -> str:
        """
        Insert or update project revenue for a given snapshot.
        """
        record = next((pr for pr in data["project_revenue"].values()
                       if pr["snapshot_id"] == snapshot_id and pr["project_id"] == project_id),
                      None)

        if record:
            record["revenue"] = revenue
        else:
            record = {
                "row_id": row_id,
                "snapshot_id": snapshot_id,
                "project_id": project_id,
                "revenue": revenue
            }
            data["project_revenue"].append(record)

        return json.dumps(record["row_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddProjectRevenue",
                "description": "Insert or update project revenue for a given snapshot_id and project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "revenue": {"type": "number"}
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "revenue"],
                },
            },
        }
