from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetInsightbyreportid(Tool):
    """Retrieve all curated insights linked to a specific report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        insights: list[dict[str, Any]] = data.get("curated_insights", {}).values()

        #3) Lookup for exact matches (without normalization)
        matches = [i for i in insights.values() if i.get("report_id") == report_id]

        if not matches:
            payload = {"error": f"No insights found for report_id {report_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda i: int(i.get("insight_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getInsightByReportId",
                "description": "Fetch all curated insights whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to filter insights by.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }
