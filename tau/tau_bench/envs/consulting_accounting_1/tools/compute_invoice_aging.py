from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, today: str = None) -> str:
        import datetime as _dt

        if not invoice_id or not today:
            payload = {"error": "invoice_id and today are required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        if not inv:
            payload = {"error": f"Invoice {invoice_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if inv.get("paid_at"):
            payload = {
                    "invoice_id": invoice_id,
                    "status": "paid",
                    "days_overdue": 0,
                    "bucket": "current",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
        today_date = _dt.datetime.fromisoformat(today)
        days = (today_date - inv_date).days
        bucket = (
            "0-30"
            if days <= 30
            else "31-60" if days <= 60 else "61-90" if days <= 90 else "90+"
        )
        payload = {
                "invoice_id": invoice_id,
                "status": "unpaid",
                "days_overdue": days,
                "bucket": bucket,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeInvoiceAging",
                "description": "Compute days overdue and aging bucket for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "today": {
                            "type": "string",
                            "description": "YYYY-MM-DD reference date",
                        },
                    },
                    "required": ["invoice_id", "today"],
                },
            },
        }
