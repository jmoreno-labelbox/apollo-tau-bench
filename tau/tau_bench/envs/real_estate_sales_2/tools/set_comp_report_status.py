from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetCompReportStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_id: int, status: str) -> str:
        rpt = next(
            (
                r
                for r in data.get("comp_reports", [])
                if r.get("report_id") == int(report_id)
            ),
            None,
        )
        if not rpt:
            payload = {"error": f"Report {report_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        rpt["status"] = status
        payload = {"report_id": report_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCompReportStatus",
                "description": "Update the status of a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "status": {"type": "string"},
                    },
                    "required": ["report_id", "status"],
                },
            },
        }
