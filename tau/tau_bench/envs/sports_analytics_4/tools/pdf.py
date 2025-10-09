from tau_bench.envs.tool import Tool
import json
from typing import Any

class Pdf(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, report_type: str = None, insights: Any = None, draft_status: str = None, label: str = None) -> str:
        if not game_pk or not report_type:
            payload = {"report_s3_path": "s3://reports/UNKNOWN/UNKNOWN_report.pdf"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"report_s3_path": f"s3://reports/{game_pk}/{report_type}_report.pdf"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makePdf",
                "description": "Creates a PDF report and returns its S3 path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "insights": {"type": "string"},
                        "game_pk": {"type": "string"},
                        "report_type": {"type": "string"},
                    },
                    "required": ["insights", "game_pk", "report_type"],
                },
            },
        }
