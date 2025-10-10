# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildOpenTicketsCSV(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        open_tickets = kwargs.get("open_tickets")
        file_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Open_Tickets.csv"
        return json.dumps({"file_path": file_path, "rows_written": len(open_tickets)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "build_open_tickets_csv", "description": "Builds and saves the Open_Tickets.csv file from a list of open tickets.", "parameters": {"type": "object", "properties": {"open_tickets": {"type": "array", "items": {"type": "object"}}}, "required": ["open_tickets"]}}}
