# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UploadQaReports(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], qa_json: Any, tex_report: Any, engine_report: Any, previews: Dict[str, Any]) -> str:
        return json.dumps({"report_uris": {"summary": "artifact://qa/summary", "details": "artifact://qa/details"}}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upload_qa_reports", "description": "Returns deterministic report URIs for uploaded QA artifacts.", "parameters": {"type": "object", "properties": {"qa_json": {"type": "array"}, "tex_report": {"type": "array"}, "engine_report": {"type": "object"}, "previews": {"type": "object"}}, "required": ["qa_json", "tex_report", "engine_report", "previews"]}}}
