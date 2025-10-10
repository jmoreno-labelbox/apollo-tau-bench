# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, due_date, invoice_date, invoice_number, po_number, vendor_id, invoice_id = f"inv_{uuid.uuid4().hex[:8]}") -> str:

        if not all([vendor_id, invoice_number, amount, invoice_date, due_date]):
            return json.dumps({"error": "All fields except po_number are required"})

        invoices = data.get("invoices", [])
        purchase_orders = data.get("purchase_orders", [])
        vendors = data.get("vendors", [])

        vendor = next((v for v in vendors if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            return json.dumps({"error": f"Vendor {vendor_id} not found"})

        if po_number:
            po = next(
                (p for p in purchase_orders if p.get("po_number") == po_number), None
            )
            if po:
                if po.get("vendor_id") != vendor_id:
                    return json.dumps(
                        {"error": "PO vendor does not match invoice vendor"}
                    )
                if abs(po.get("total_amount", 0) - amount) > 0.01:
                    return json.dumps(
                        {
                            "error": f"Invoice amount ${amount} does not match PO amount ${po.get('total_amount', 0)}"
                        }
                    )

        new_invoice = {
            "invoice_id": invoice_id,
            "vendor_id": vendor_id,
            "po_number": po_number,
            "invoice_number": invoice_number,
            "amount": amount,
            "invoice_date": invoice_date,
            "due_date": due_date,
            "status": "pending",
            "recorded_date": datetime.now().isoformat(),
            "payment_terms": vendor.get("payment_terms", "Net 30"),
        }

        invoices.append(new_invoice)

        due_dt = datetime.fromisoformat(due_date.replace("Z", "+00:00"))

        from datetime import timezone

        if datetime.now(timezone.utc) > due_dt:
            days_late = (datetime.now(timezone.utc) - due_dt).days
            return json.dumps(
                {
                    "success": True,
                    "invoice": new_invoice,
                    "warning": f"Invoice is already {days_late} days past due",
                }
            )

        return json.dumps({"success": True, "invoice": new_invoice})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_invoice",
                "description": "Record a vendor invoice for payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_id": {"type": "string", "description": "Vendor ID"},
                        "invoice_id": {"type": "string", "description": "Invoice ID"},
                        "po_number": {
                            "type": "string",
                            "description": "Related PO number (optional)",
                        },
                        "invoice_number": {
                            "type": "string",
                            "description": "Vendor's invoice number",
                        },
                        "amount": {"type": "number", "description": "Invoice amount"},
                        "invoice_date": {
                            "type": "string",
                            "description": "Invoice date",
                        },
                        "due_date": {
                            "type": "string",
                            "description": "Payment due date",
                        },
                    },
                    "required": [
                        "vendor_id",
                        "invoice_number",
                        "amount",
                        "invoice_date",
                        "due_date",
                    ],
                },
            },
        }
