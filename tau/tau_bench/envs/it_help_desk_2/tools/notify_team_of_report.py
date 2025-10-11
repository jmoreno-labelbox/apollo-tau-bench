# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyTeamOfReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], csv_path, pdf_path) -> str:
        recipient = "it-management-dl@company.com"
        return json.dumps({"status": "notified", "recipient": recipient, "attachments": [pdf_path, csv_path]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_team_of_report", "description": "Sends an email notification with the generated reports as attachments.", "parameters": {"type": "object", "properties": {"pdf_path": {"type": "string"}, "csv_path": {"type": "string"}}, "required": ["pdf_path", "csv_path"]}}}
