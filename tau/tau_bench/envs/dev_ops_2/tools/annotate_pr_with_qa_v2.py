# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnnotatePrWithQaV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, summary: str, report_uri: str) -> str:
        comments = _get_table(data, "notifications")
        comment_id = f"cmt-{len(comments)+1}"
        comments.append({"id": comment_id, "type": "pr_comment", "pr_number": pr_number, "summary": summary, "report_uri": report_uri})
        return json.dumps({"comment_id": comment_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "annotate_pr_with_qa_v2", "description": "Annotate a PR with QA summary and report URI deterministically.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "summary": {"type": "string"}, "report_uri": {"type": "string"}}, "required": ["pr_number", "summary", "report_uri"]}}}
