# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccessGapSummaryFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        lines = kwargs.get("content_lines", [])
        candidate_id = kwargs.get("candidate_id")
        content_text = "\n".join(lines) + ("\n" if lines else "")
        res = json.loads(
            UpsertOnboardingFile.invoke(data, file_path=file_path, content_text=content_text, mime_type="text/markdown",
                                        candidate_id=candidate_id))
        return json.dumps({"file_path": file_path, "created": res.get("created", False)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_access_gap_summary_file",
                                                 "description": "Create a markdown summary file from lines.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_lines": {"type": "array",
                                                                                                 "items": {
                                                                                                     "type": "string"}},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_lines",
                                                                             "candidate_id"]}}}
