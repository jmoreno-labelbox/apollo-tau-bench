# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidatePurchaseOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        po_number = kwargs.get("po_number")
        vendor_id = kwargs.get("vendor_id")
        project_id = kwargs.get("project_id")
        amount = kwargs.get("amount")
        description = kwargs.get("description")
        fiscal_year = kwargs.get("fiscal_year", datetime.now().year)

        if not all([po_number, vendor_id, project_id, amount]):
            return json.dumps(
                {"error": "po_number, vendor_id, project_id, and amount are required"}
            )

        budgets = data.get("budgets", [])
        vendors = data.get("vendors", [])
        purchase_orders = data.get("purchase_orders", [])
        projects = list(data.get("projects", {}).values())

        vendor = next((v for v in vendors if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            return json.dumps({"error": f"Vendor {vendor_id} not found"})

        if vendor.get("status") != "active":
            return json.dumps(
                {
                    "error": f"Vendor status is {vendor.get('status')}. Only active vendors allowed"
                }
            )

        budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not budget:
            return json.dumps({"error": "No budget found for project"})

        available_budget = (
            budget["total_budget"]
            - budget.get("spent_amount", 0)
            - budget.get("committed_amount", 0)
        )

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        approval_required = []

        if project:
            if project["priority"] == "low" and amount > 10000:
                approval_required.append("finance_manager")
            if amount > 50000:
                approval_required.append("department_head")
            if amount > 100000:
                approval_required.append("cfo")

        validation_result = {
            "po_number": po_number,
            "validation_status": "valid",
            "vendor_check": {
                "vendor_name": vendor.get("vendor_name"),
                "vendor_status": vendor.get("status"),
                "late_payments": vendor.get("late_payments", 0),
                "requires_prepayment": vendor.get("late_payments", 0) >= 3,
            },
            "budget_check": {
                "available_budget": available_budget,
                "po_amount": amount,
                "sufficient_funds": amount <= available_budget,
                "budget_utilization_after": round(
                    (
                        (budget.get("spent_amount", 0) + amount)
                        / budget["total_budget"]
                        * 100
                    ),
                    2,
                ),
            },
            "approval_requirements": approval_required,
            "warnings": [],
        }

        if amount > available_budget:
            validation_result["validation_status"] = "insufficient_funds"
            validation_result["warnings"].append("Insufficient budget available")

        if vendor.get("late_payments", 0) >= 3:
            validation_result["warnings"].append(
                "Vendor has history of late payments - prepayment recommended"
            )

        if validation_result["budget_check"]["budget_utilization_after"] > 90:
            validation_result["warnings"].append(
                "PO will push budget utilization over 90%"
            )

        return json.dumps(validation_result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_purchase_order",
                "description": "Validate a purchase order against budget and vendor status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {
                            "type": "string",
                            "description": "Purchase order number",
                        },
                        "vendor_id": {"type": "string", "description": "Vendor ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "amount": {"type": "number", "description": "PO amount"},
                        "description": {
                            "type": "string",
                            "description": "PO description",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["po_number", "vendor_id", "project_id", "amount"],
                },
            },
        }
