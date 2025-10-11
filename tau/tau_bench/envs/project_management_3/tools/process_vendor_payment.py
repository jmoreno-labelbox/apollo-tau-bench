# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessVendorPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, payment_amount, payment_method, processor_id) -> str:

        if not all([invoice_id, payment_amount, payment_method, processor_id]):
            return json.dumps({"error": "All fields are required"})

        invoices = data.get("invoices", [])
        payments = data.get("payments", [])
        vendors = data.get("vendors", [])

        invoice = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        if not invoice:
            return json.dumps({"error": f"Invoice {invoice_id} not found"})

        if invoice.get("status") == "paid":
            return json.dumps({"error": "Invoice is already paid"})

        if payment_amount != invoice["amount"]:
            return json.dumps(
                {
                    "error": f"Payment amount ${payment_amount} does not match invoice amount ${invoice['amount']}"
                }
            )

        due_date = datetime.fromisoformat(invoice["due_date"].replace("Z", "+00:00"))

        from datetime import timezone

        is_late = datetime.now(timezone.utc) > due_date
        late_fee = 0
        days_late = 0

        if is_late:
            days_late = (datetime.now(timezone.utc) - due_date).days
            months_late = days_late // 30
            late_fee = invoice["amount"] * 0.02 * months_late

        payment_id = f"pay_{uuid.uuid4().hex[:8]}"

        new_payment = {
            "payment_id": payment_id,
            "invoice_id": invoice_id,
            "vendor_id": invoice["vendor_id"],
            "amount": payment_amount,
            "late_fee": late_fee,
            "total_paid": payment_amount + late_fee,
            "payment_method": payment_method,
            "payment_date": datetime.now(timezone.utc).isoformat(),
            "processed_by": processor_id,
            "is_late": is_late,
            "days_late": days_late,
        }

        payments.append(new_payment)

        invoice["status"] = "paid"
        invoice["payment_id"] = payment_id
        invoice["paid_date"] = datetime.now(timezone.utc).isoformat()

        vendor = next(
            (v for v in vendors if v.get("vendor_id") == invoice["vendor_id"]), None
        )
        if vendor:
            if "late_payments" not in vendor:
                vendor["late_payments"] = 0
            if is_late:
                vendor["late_payments"] += 1

            vendor["last_payment_date"] = datetime.now(timezone.utc).isoformat()

        result = {"success": True, "payment": new_payment}

        if vendor and vendor.get("late_payments", 0) >= 3:
            result[
                "warning"
            ] = f"Vendor has {vendor['late_payments']} late payments - review required"

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_vendor_payment",
                "description": "Process payment for a vendor invoice",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID"},
                        "payment_amount": {
                            "type": "number",
                            "description": "Payment amount",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method (check, wire, ach)",
                        },
                        "processor_id": {
                            "type": "string",
                            "description": "Employee processing payment",
                        },
                    },
                    "required": [
                        "invoice_id",
                        "payment_amount",
                        "payment_method",
                        "processor_id",
                    ],
                },
            },
        }
