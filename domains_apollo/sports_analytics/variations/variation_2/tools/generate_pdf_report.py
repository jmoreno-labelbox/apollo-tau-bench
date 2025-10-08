from tau_bench.envs.tool import Tool
import json
from typing import Any

class GeneratePdfReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        report_type = kwargs.get("report_type")
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GeneratePdfReport",
                "description": "Generates a PDF report and returns its S3 path.",
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
