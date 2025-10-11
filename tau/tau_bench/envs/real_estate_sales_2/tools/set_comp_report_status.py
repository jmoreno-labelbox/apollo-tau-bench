# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetCompReportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], report_id, status) -> str:
        new_status = status
        rpt = next((r for r in data.get("comp_reports", []) if r.get("report_id") == int(report_id)), None)
        if not rpt:
            return json.dumps({"error": f"Report {report_id} not found"}, indent=2)
        rpt["status"] = new_status
        return json.dumps({"report_id": report_id, "status": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_comp_report_status",
                "description": "Update the status of a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}, "status": {"type": "string"}},
                    "required": ["report_id", "status"],
                },
            },
        }
