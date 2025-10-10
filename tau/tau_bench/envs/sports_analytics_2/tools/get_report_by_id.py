# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReportById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], report_id) -> str:
        report = next((r for r in data.get("scouting_reports", []) if r.get("report_id") == report_id), None)
        return json.dumps(report or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_report_by_id", "description": "Reads a scouting report by id.", "parameters": {"type": "object", "properties": {"report_id": {"type": "string"}}, "required": ["report_id"]}}}
