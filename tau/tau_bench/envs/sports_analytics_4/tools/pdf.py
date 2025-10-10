# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pdf(Tool):
    @staticmethod
        # primary call function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        report_type = kwargs.get("report_type")
        if not game_pk or not report_type:
            # Revert to a clear, deterministic error path to eliminate the use of placeholders.
        # return output
            return json.dumps({"report_s3_path": "s3://reports/UNKNOWN/UNKNOWN_report.pdf"}, indent=2)
        # return output
        return json.dumps({"report_s3_path": f"s3://reports/{game_pk}/{report_type}_report.pdf"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "makePDF", "description": "Creates a PDF report and returns its S3 path.", "parameters": {"type": "object", "properties": {"insights": {"type": "string"}, "game_pk": {"type": "string"}, "report_type": {"type": "string"}}, "required": ["insights", "game_pk", "report_type"]}}}
