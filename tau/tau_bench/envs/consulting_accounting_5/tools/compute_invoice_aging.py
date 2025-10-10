# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Compute days overdue, bucket, and escalation policy for a given invoice_id and as_of_date.
        """
        invoice_id = kwargs["invoice_id"]
        as_of_date = datetime.strptime(kwargs["as_of_date"], "%Y-%m-%d")

        invoice = next((inv for inv in data["invoices"] if inv["invoice_id"] == invoice_id), None)
        if not invoice:
            return json.dumps({"error": "invoice not found"})

        due_date = datetime.strptime(invoice["invoice_date"], "%Y-%m-%d")  # assume net 0 / same day due
        days_overdue = (as_of_date - due_date).days

        if days_overdue < 0:
            bucket = "upcoming_due"
            escalation = "none"
        elif days_overdue <= 30:
            bucket = "0-30"
            escalation = "friendly_reminder"
        elif days_overdue <= 60:
            bucket = "31-60"
            escalation = "formal_notice"
        elif days_overdue <= 90:
            bucket = "61-90"
            escalation = "phone_call"
        else:
            bucket = "90+"
            escalation = "collections_hold"

        return json.dumps({
            "invoice_id": invoice_id,
            "as_of_date": kwargs["as_of_date"],
            "days_overdue": days_overdue,
            "bucket": bucket,
            "escalation": escalation
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeInvoiceAging",
                "description": "Compute the aging and categorizes into bucket from invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "as_of_date": {"type": "string"}
                    },
                    "required": ["as_of_date", "invoice_id"],
                },
            },
        }
