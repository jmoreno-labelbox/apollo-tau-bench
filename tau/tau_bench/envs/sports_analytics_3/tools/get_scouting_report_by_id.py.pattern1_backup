# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScoutingReportById(Tool):
    """Fetch a single scouting report by its report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")

        # 1) Validate
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # 2) Get DB from passed-in data
        reports: List[Dict[str, Any]] = data.get("scouting_reports", [])

        # 3) Exact match lookup
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
