# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScoutingReportById(Tool):
    """Fetch a single scouting report by its report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], report_id) -> str:

        # 1) Confirm accuracy
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # Retrieve the database from the provided data.
        reports: List[Dict[str, Any]] = list(data.get("scouting_reports", {}).values())

        # 3) Precise match retrieval
        for report in reports:
            if report.get("report_id") == report_id:
                return json.dumps(report, indent=2)

        return json.dumps({"error": f"No scouting report found with ID {report_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scouting_report_by_id",
                "description": "Fetch a single scouting report's full details by its report_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to retrieve."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }
