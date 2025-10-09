from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class BuildInvoiceLines(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], time_entries: list = None, hourly_rate: float = 0.0) -> str:
        time_entries_ids = time_entries or []
        hourly_rate = float(hourly_rate)
        entries_index = {t["time_entry_id"]: t for t in data.get("time_entries", {}).values()}
        lines = []
        subtotal = 0.0
        for idx, tid in enumerate(time_entries_ids, start=1):
            te = entries_index.get(tid)
            if not te:
                continue
            hours = float(te.get("hours_worked", 0.0))
            amount = round(hours * hourly_rate, 2)
            line_id = f"LINE-AUTO-{idx:03d}"
            lines.append(
                {
                    "invoice_line_id": line_id,
                    "project_id": te.get("project_id"),
                    "hours_billed": hours,
                    "hourly_rate": hourly_rate,
                    "line_amount": amount,
                }
            )
            subtotal += amount
        payload = {"invoice_lines": lines, "subtotal": round(subtotal, 2)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildInvoiceLines",
                "description": "Build invoice lines from a list of time entry IDs and an hourly rate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_entries": {"type": "array", "items": {"type": "string"}},
                        "hourly_rate": {"type": "number"},
                    },
                    "required": ["time_entries", "hourly_rate"],
                },
            },
        }
