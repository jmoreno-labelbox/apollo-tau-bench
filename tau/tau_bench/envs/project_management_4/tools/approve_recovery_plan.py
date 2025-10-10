# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApproveRecoveryPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        decision = kwargs.get("decision")
        approver_id = kwargs.get("approver_id")

        if not all([plan_id, decision, approver_id]):
            return json.dumps(
                {"error": "plan_id, decision, and approver_id are required"}
            )

        recovery_plans = data.get("recovery_plans", [])
        milestones = list(data.get("milestones", {}).values())

        plan = next((p for p in recovery_plans if p.get("plan_id") == plan_id), None)
        if not plan:
            return json.dumps({"error": f"Recovery plan '{plan_id}' not found"})

        if plan.get("status") != "pending_approval":
            return json.dumps({"error": "Plan is not in pending_approval status"})

        plan["status"] = "approved" if decision == "approve" else "rejected"
        plan["approver_id"] = approver_id
        plan["approval_date"] = datetime.now(timezone.utc).isoformat()
        plan["approval_notes"] = kwargs.get("approval_notes", "")

        if decision == "approve":

            milestone = next(
                (
                    m
                    for m in milestones
                    if m.get("milestone_id") == plan.get("milestone_id")
                ),
                None,
            )
            if milestone:
                milestone["target_date"] = plan.get("recovery_target_date")
                milestone["has_recovery_plan"] = True
                milestone["recovery_plan_id"] = plan_id

                if plan.get("feasibility") == "high":
                    milestone["health"] = (
                        "yellow"
                        if milestone.get("health") == "red"
                        else milestone.get("health")
                    )

                if (
                    milestone.get("is_critical_path")
                    and milestone.get("resource_allocation", 100) < 100
                ):
                    return json.dumps(
                        {
                            "error": "Cannot approve recovery plan that reduces critical path task resources below 100%"
                        }
                    )

        return json.dumps(
            {"success": True, "recovery_plan": plan, "decision": decision}
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_recovery_plan",
                "description": "Approve or reject a recovery plan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "Recovery plan ID",
                        },
                        "decision": {
                            "type": "string",
                            "description": "Decision: approve or reject",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Approver employee ID",
                        },
                        "approval_notes": {
                            "type": "string",
                            "description": "Approval notes",
                        },
                    },
                    "required": ["plan_id", "decision", "approver_id"],
                },
            },
        }
