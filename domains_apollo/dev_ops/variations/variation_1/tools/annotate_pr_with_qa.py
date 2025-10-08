from tau_bench.envs.tool import Tool
import json
from typing import Any

class AnnotatePrWithQa(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pr_number: int, summary: str, report_uri: str
    ) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        if not pr:
            return _error(f"PR '{pr_number}' not found.")
        comments = pr.setdefault("comments", [])
        comments.append({"summary": summary, "report_uri": report_uri})
        payload = {"commented": True, "count": len(comments)}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnnotatePrWithQa",
                "description": "Adds a deterministic QA annotation to a PR.",
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
