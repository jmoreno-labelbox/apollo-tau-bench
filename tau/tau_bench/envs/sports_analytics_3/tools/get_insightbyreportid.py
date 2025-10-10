# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInsightbyreportid(Tool):
    """Fetch all curated insights associated with a given report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")

        # 1) Validate
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # 2) Get DB
        insights: List[Dict[str, Any]] = list(data.get("curated_insights", {}).values())

        # 3) Exact match lookup (no normalization)
        matches = [i for i in insights if i.get("report_id") == report_id]

        if not matches:
            return json.dumps({"error": f"No insights found for report_id {report_id}"}, indent=2)

        # 4) Deterministic ordering
        matches.sort(key=lambda i: int(i.get("insight_id", 0)))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_insight_by_report_id",
                "description": "Fetch all curated insights whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to filter insights by."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }
