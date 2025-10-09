from tau_bench.envs.tool import Tool
import json
from typing import Any

class UploadQaReports(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        qa_json: Any,
        tex_report: Any,
        engine_report: Any,
        previews: dict[str, Any],
    ) -> str:
        payload = {
            "report_uris": {
                "summary": "artifact://qa/summary",
                "details": "artifact://qa/details",
            }
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UploadQaReports",
                "description": "Returns deterministic report URIs for uploaded QA artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "qa_json": {"type": "array"},
                        "tex_report": {"type": "array"},
                        "engine_report": {"type": "object"},
                        "previews": {"type": "object"},
                    },
                    "required": ["qa_json", "tex_report", "engine_report", "previews"],
                },
            },
        }
