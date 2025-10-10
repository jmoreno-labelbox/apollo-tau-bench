# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], hourly_rate = 0.0, time_entries = []) -> str:
        time_entries_ids = time_entries
        hourly_rate = float(hourly_rate)
        entries_index = {t["time_entry_id"]: t for t in list(data.get("time_entries", {}).values())}
        lines = []
        subtotal = 0.0
        for idx, tid in enumerate(time_entries_ids, start=1):
            te = entries_index.get(tid)
            if not te:
                continue
            hours = float(te.get("hours_worked", 0.0))
            amount = round(hours * hourly_rate, 2)
            line_id = f"LINE-AUTO-{idx:03d}"
            lines.append({"invoice_line_id": line_id,"project_id": te.get("project_id"),"hours_billed": hours,"hourly_rate": hourly_rate,"line_amount": amount})
            subtotal += amount
        return json.dumps({"invoice_lines": lines,"subtotal": round(subtotal, 2)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "build_invoice_lines","description": "Build invoice lines from a list of time entry IDs and an hourly rate.","parameters": {"type": "object","properties": {"time_entries": {"type": "array","items": {"type": "string"}},"hourly_rate": {"type": "number"}},"required": ["time_entries","hourly_rate"]}}}
