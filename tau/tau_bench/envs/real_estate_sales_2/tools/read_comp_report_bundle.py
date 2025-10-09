from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any

class ReadCompReportBundle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_id: int) -> str:
        rpt = next(
            (
                r
                for r in data.get("comp_reports", [])
                if r.get("report_id") == report_id
            ),
            None,
        )
        if not rpt:
            payload = {"error": f"Report {report_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        comps = [
            c
            for c in data.get("comparables", [])
            if c.get("report_id") == report_id
        ]
        docs = [
            d
            for d in data.get("documents", [])
            if d.get("entity_type") == "comp_report"
            and d.get("entity_id") == report_id
        ]
        payload = {"report": rpt, "comparables": comps, "documents": docs}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadCompReportBundle",
                "description": "Fetch a comp report with its comparables and attached document(s).",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }
