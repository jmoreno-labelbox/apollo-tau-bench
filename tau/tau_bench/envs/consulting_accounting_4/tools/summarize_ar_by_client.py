from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SummarizeARByClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoices: list[dict[str, Any]] = None) -> str:
        invoices = invoices or []
        summary: dict[str, dict[str, float]] = {}
        for inv in invoices:
            pid = inv.get("publisher_id")
            bucket = inv.get("aging_bucket", "0-30")
            amt = float(inv.get("total_due", 0))
            summary.setdefault(pid, {}).values()
            summary[pid][bucket] = summary[pid].get(bucket, 0.0) + amt
        payload = {"summary_by_publisher": summary}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizeArByClient",
                "description": "Summarize A/R by publisher and aging bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["invoices"],
                },
            },
        }
