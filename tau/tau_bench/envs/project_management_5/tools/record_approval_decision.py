# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordApprovalDecision(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], approver_id, cr_id, decision, approval_id = f"appr_ch_{uuid.uuid4().hex[:8]}", comments = "", conditions = []) -> str:

        if not all([cr_id, approver_id, decision]):
            return json.dumps(
                {"error": "cr_id, approver_id, and decision are required"}
            )

        if decision not in ["approve", "reject", "approve_with_conditions"]:
            return json.dumps(
                {
                    "error": "Decision must be: approve, reject, or approve_with_conditions"
                }
            )

        change_requests = list(data.get("change_requests", {}).values())
        approval_workflows = list(data.get("approval_workflows", {}).values())
        change_approvals = list(data.get("change_approvals", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        workflow = next(
            (
                w
                for w in approval_workflows
                if w.get("cr_id") == cr_id and w.get("status") == "active"
            ),
            None,
        )
        if not workflow:
            return json.dumps({"error": f"No active workflow found for CR '{cr_id}'"})

        current_step = {}
        for step in workflow.get("steps", []):
            if (
                step.get("approver_id") == approver_id
                and step.get("status") == "pending"
            ):
                current_step = step
                break

        if current_step and current_step.get("step_number") != workflow.get("current_step"):
            return json.dumps({"error": "Cannot approve out of sequence"})

        approval_record = {
            "approval_id": approval_id,
            "cr_id": cr_id,
            "approver_id": approver_id,
            "approver_role": current_step.get("approval_level"),
            "decision": decision,
            "comments": comments,
            "conditions": conditions if decision == "approve_with_conditions" else [],
            "action_date": datetime.now().isoformat(),
        }

        change_approvals.append(approval_record)

        current_step["status"] = "approved" if decision != "reject" else "rejected"
        current_step["action_date"] = datetime.now().isoformat()

        if decision == "reject":
            workflow["status"] = "rejected"
            cr["status"] = "rejected"

            cr["rejection_date"] = datetime.now().isoformat()
            cr["can_resubmit_after"] = (datetime.now() + timedelta(days=30)).isoformat()
        else:

            approval_level = current_step.get("approval_level")
            if "approvals_received" not in cr:
                cr["approvals_received"] = []
            if approval_level not in cr["approvals_received"]:
                cr["approvals_received"].append(approval_level)

            all_steps_complete = all(
                s.get("status") != "pending" for s in workflow.get("steps", [])
            )

            if all_steps_complete:
                workflow["status"] = "completed"

                if set(cr.get("approvals_required", [])) == set(
                    cr.get("approvals_received", [])
                ):
                    cr["status"] = "approved"
                    cr["approval_date"] = datetime.now().isoformat()
            else:

                workflow["current_step"] = current_step.get("step_number", 0) + 1

        return json.dumps(
            {
                "success": True,
                "approval": approval_record,
                "workflow_status": workflow.get("status"),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_approval_decision",
                "description": "Record an approval decision for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "aproval_id": {"type": "string", "description": "Aproval ID"},
                        "approver_id": {"type": "string", "description": "Approver ID"},
                        "decision": {
                            "type": "string",
                            "description": "Decision: approve, reject, approve_with_conditions",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Approval comments",
                        },
                        "conditions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Conditions if approved conditionally",
                        },
                    },
                    "required": ["cr_id", "approver_id", "decision"],
                },
            },
        }
