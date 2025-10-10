# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportRecentTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        days = kwargs.get("days", 30)
        tickets = list(data.get("tickets", {}).values())
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Tickets_Export.csv"
        return json.dumps({"export_path": report_path, "ticket_count": len(tickets)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "export_recent_tickets", "description": "Exports all tickets updated in the last N days to a CSV file.", "parameters": {"type": "object", "properties": {"days": {"type": "integer"}}, "required": ["days"]}}}
