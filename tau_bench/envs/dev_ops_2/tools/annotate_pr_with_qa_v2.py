from tau_bench.envs.tool import Tool
import json
from typing import Any

class AnnotatePrWithQaV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pr_number: int, summary: str, report_uri: str
    ) -> str:
        pass
        comments = _get_table(data, "notifications")
        comment_id = f"cmt-{len(comments)+1}"
        comments.append(
            {
                "id": comment_id,
                "type": "pr_comment",
                "pr_number": pr_number,
                "summary": summary,
                "report_uri": report_uri,
            }
        )
        payload = {"comment_id": comment_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnnotatePrWithQaV2",
                "description": "Annotate a PR with QA summary and report URI deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "summary": {"type": "string"},
                        "report_uri": {"type": "string"},
                    },
                    "required": ["pr_number", "summary", "report_uri"],
                },
            },
        }
