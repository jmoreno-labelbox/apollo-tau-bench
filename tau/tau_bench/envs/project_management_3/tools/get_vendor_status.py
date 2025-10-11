# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetVendorStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], vendor_id) -> str:

        if not vendor_id:
            return json.dumps({"error": "vendor_id is required"})

        vendors = data.get("vendors", [])
        invoices = data.get("invoices", [])
        payments = data.get("payments", [])
        purchase_orders = data.get("purchase_orders", [])

        vendor = next((v for v in vendors if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            return json.dumps({"error": f"Vendor {vendor_id} not found"})

        vendor_invoices = [i for i in invoices if i.get("vendor_id") == vendor_id]

        outstanding_amount = sum(
            i.get("amount", 0) for i in vendor_invoices if i.get("status") != "paid"
        )

        pending_pos = [
            po
            for po in purchase_orders
            if po.get("vendor_id") == vendor_id
            and po.get("status") == "pending_approval"
        ]
        approved_pos = [
            po
            for po in purchase_orders
            if po.get("vendor_id") == vendor_id and po.get("status") == "approved"
        ]

        late_invoices = []
        for invoice in vendor_invoices:
            if invoice.get("status") != "paid":
                due_date = datetime.fromisoformat(
                    invoice["due_date"].replace("Z", "+00:00")
                )

                current_time = datetime.now(timezone.utc)
                if current_time > due_date:
                    days_late = (current_time - due_date).days
                    late_invoices.append(
                        {
                            "invoice_id": invoice["invoice_id"],
                            "amount": invoice["amount"],
                            "days_late": days_late,
                            "late_fee": invoice["amount"] * 0.02 * (days_late // 30),
                        }
                    )

        status = {
            "vendor_id": vendor_id,
            "vendor_name": vendor.get("vendor_name"),
            "payment_terms": vendor.get("payment_terms", "Net 30"),
            "status": vendor.get("status", "active"),
            "late_payments_count": vendor.get("late_payments", 0),
            "requires_prepayment": vendor.get("late_payments", 0) >= 3,
            "outstanding_amount": outstanding_amount,
            "pending_pos_count": len(pending_pos),
            "pending_pos_value": sum(po.get("total_amount", 0) for po in pending_pos),
            "approved_pos_count": len(approved_pos),
            "approved_pos_value": sum(po.get("total_amount", 0) for po in approved_pos),
            "late_invoices": late_invoices,
            "total_late_fees": sum(inv["late_fee"] for inv in late_invoices),
            "last_payment_date": vendor.get("last_payment_date"),
        }

        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_vendor_status",
                "description": "Get vendor payment status and history",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_id": {"type": "string", "description": "Vendor ID"}
                    },
                    "required": ["vendor_id"],
                },
            },
        }
