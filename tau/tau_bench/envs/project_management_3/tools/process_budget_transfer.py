from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ProcessBudgetTransfer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        transfer_id: str = None,
        approval_action: str = None,
        approver_id: str = None,
        approver_role: str = None
    ) -> str:
        if not all([transfer_id, approval_action, approver_id, approver_role]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        budget_transfers = data.get("budget_transfers", [])
        budgets = data.get("budgets", [])

        transfer = next(
            (t for t in budget_transfers if t.get("transfer_id") == transfer_id), None
        )
        if not transfer:
            payload = {"error": f"Transfer {transfer_id} not found"}
            out = json.dumps(payload)
            return out

        if transfer.get("status") != "pending_approval":
            payload = {"error": "Transfer is not pending approval"}
            out = json.dumps(payload)
            return out

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
        payload = {
            "success": True,
            "transfer": transfer,
            "all_approvals_complete": transfer["status"] in ["approved", "rejected"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processBudgetTransfer",
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
