from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetReportById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        report_id = kwargs.get("report_id")
        report = next(
            (
                r
                for r in data.get("scouting_reports", [])
                if r.get("report_id") == report_id
            ),
            None,
        )
        payload = report or {}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getReportById",
                "description": "Reads a scouting report by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "string"}},
                    "required": ["report_id"],
                },
            },
        }
