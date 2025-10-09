from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetVendorStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], vendor_id: str = None) -> str:
        if not vendor_id:
            payload = {"error": "vendor_id is required"}
            out = json.dumps(payload)
            return out

        vendors = data.get("vendors", {}).values()
        invoices = data.get("invoices", {}).values()
        data.get("payments", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        vendor = next((v for v in vendors.values() if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            payload = {"error": f"Vendor {vendor_id} not found"}
            out = json.dumps(payload)
            return out

        vendor_invoices = [i for i in invoices.values() if i.get("vendor_id") == vendor_id]

        outstanding_amount = sum(
            i.get("amount", 0) for i in vendor_invoices if i.get("status") != "paid"
        )

        pending_pos = [
            po
            for po in purchase_orders.values() if po.get("vendor_id") == vendor_id
            and po.get("status") == "pending_approval"
        ]
        approved_pos = [
            po
            for po in purchase_orders.values() if po.get("vendor_id") == vendor_id and po.get("status") == "approved"
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
            "pending_pos_value": sum(po.get("total_amount", 0) for po in pending_pos.values()),
            "approved_pos_count": len(approved_pos),
            "approved_pos_value": sum(po.get("total_amount", 0) for po in approved_pos.values()),
            "late_invoices": late_invoices,
            "total_late_fees": sum(inv["late_fee"] for inv in late_invoices.values()),
            "last_payment_date": vendor.get("last_payment_date"),
        }
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVendorStatus",
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
