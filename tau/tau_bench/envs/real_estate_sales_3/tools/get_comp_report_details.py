# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCompReportDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], report_id) -> str:
        rpt = next((r for r in data.get("comp_reports", []) if r.get("report_id") == int(report_id)), None)
        if not rpt:
            return json.dumps({"error": f"Report {report_id} not found"}, indent=2)
        comps = [c for c in data.get("comparables", []) if c.get("report_id") == int(report_id)]
        docs = [d for d in data.get("documents", []) if d.get("entity_type") == "comp_report" and d.get("entity_id") == int(report_id)]
        return json.dumps({"report": rpt, "comparables": comps, "documents": docs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_comp_report_details",
            "description":"Fetch a comp report with its comparables and attached document(s).",
            "parameters":{"type":"object","properties":{"report_id":{"type":"integer"}},"required":["report_id"]}
        }}
