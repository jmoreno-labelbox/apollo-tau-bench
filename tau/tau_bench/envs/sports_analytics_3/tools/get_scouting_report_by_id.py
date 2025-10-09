from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetScoutingReportById(Tool):
    """Retrieve a single scouting report using its report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Lookup for exact matches
        for report in reports:
            if report.get("report_id") == report_id:
                payload = report
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No scouting report found with ID {report_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getScoutingReportById",
                "description": "Fetch a single scouting report's full details by its report_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to retrieve.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }
