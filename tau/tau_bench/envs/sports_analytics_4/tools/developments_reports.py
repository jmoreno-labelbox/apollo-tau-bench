from tau_bench.envs.tool import Tool
import json
from typing import Any

class DevelopmentsReports(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], week_of: str = None, report_count: int = None) -> str:
        data.setdefault("player_dev_reports", []).append(
            {
                "dev_report_id": f"dev_{len(data.get('player_dev_reports', []))+1}",
                "week_of": week_of,
                "report_count": report_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "reportings",
                "description": "Persists player development reports to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "week_of": {"type": "string"},
                        "report_count": {"type": "integer"},
                    },
                    "required": ["week_of"],
                },
            },
        }
