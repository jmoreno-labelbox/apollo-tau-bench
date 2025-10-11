# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportServiceDeskTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end_date, export_path, start_date) -> str:
        tickets = list(data.get("tickets", {}).values())
        return json.dumps({"export_path": export_path, "ticket_count": len(tickets), "start_date": start_date, "end_date": end_date}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "export_service_desk_tickets", "description": "Export service desk tickets within a date range to CSV.", "parameters": {"type": "object", "properties": {"start_date": {"type": "string"}, "end_date": {"type": "string"}, "export_path": {"type": "string"}}, "required": ["start_date", "end_date", "export_path"]}}}
