# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessBudgetTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transfer_id = kwargs.get("transfer_id")
        approval_action = kwargs.get("approval_action")
        approver_id = kwargs.get("approver_id")
        approver_role = kwargs.get("approver_role")

        if not all([transfer_id, approval_action, approver_id, approver_role]):
            return json.dumps({"error": "All fields are required"})

        budget_transfers = data.get("budget_transfers", [])
        budgets = data.get("budgets", [])

        transfer = next(
            (t for t in budget_transfers if t.get("transfer_id") == transfer_id), None
        )
        if not transfer:
            return json.dumps({"error": f"Transfer {transfer_id} not found"})

        if transfer.get("status") != "pending_approval":
            return json.dumps({"error": "Transfer is not pending approval"})

        if "approvals" not in transfer:
            transfer["approvals"] = {}

        transfer["approvals"][approver_role] = {
            "action": approval_action,
            "approver_id": approver_id,
            "approval_date": datetime.now().isoformat(),
        }

        all_approved = all(
            transfer["approvals"].get(role, {}).get("action") == "approve"
            for role in transfer["approvals_required"]
        )

        any_rejected = any(
            transfer["approvals"].get(role, {}).get("action") == "reject"
            for role in transfer["approvals_required"]
        )

        if any_rejected:
            transfer["status"] = "rejected"
        elif all_approved:
            transfer["status"] = "approved"

            source_budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == transfer["source_project_id"]
                    and b.get("fiscal_year") == transfer["fiscal_year"]
                ),
                None,
            )
            target_budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == transfer["target_project_id"]
                    and b.get("fiscal_year") == transfer["fiscal_year"]
                ),
                None,
            )

            if source_budget and target_budget:
                source_budget["total_budget"] -= transfer["transfer_amount"]
                target_budget["total_budget"] += transfer["transfer_amount"]
                source_budget["last_modified"] = datetime.now().isoformat()
                target_budget["last_modified"] = datetime.now().isoformat()

        transfer["last_updated"] = datetime.now().isoformat()

        return json.dumps(
            {
                "success": True,
                "transfer": transfer,
                "all_approvals_complete": transfer["status"]
                in ["approved", "rejected"],
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_budget_transfer",
                "description": "Approve or reject a budget transfer request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transfer_id": {"type": "string", "description": "Transfer ID"},
                        "approval_action": {
                            "type": "string",
                            "description": "approve or reject",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Approver's employee ID",
                        },
                        "approver_role": {
                            "type": "string",
                            "description": "Approver's role in this transfer",
                        },
                    },
                    "required": [
                        "transfer_id",
                        "approval_action",
                        "approver_id",
                        "approver_role",
                    ],
                },
            },
        }
