from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class ApproveRecoveryPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, decision: str = None, approver_id: str = None, approval_notes: str = "") -> str:
        if not all([plan_id, decision, approver_id]):
            payload = {"error": "plan_id, decision, and approver_id are required"}
            out = json.dumps(payload)
            return out

        recovery_plans = data.get("recovery_plans", [])
        milestones = data.get("milestones", [])

        plan = next((p for p in recovery_plans if p.get("plan_id") == plan_id), None)
        if not plan:
            payload = {"error": f"Recovery plan '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        if plan.get("status") != "pending_approval":
            payload = {"error": "Plan is not in pending_approval status"}
            out = json.dumps(payload)
            return out

        plan["status"] = "approved" if decision == "approve" else "rejected"
        plan["approver_id"] = approver_id
        plan["approval_date"] = datetime.now(timezone.utc).isoformat()
        plan["approval_notes"] = approval_notes

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
                    payload = {
                        "error": "Cannot approve recovery plan that reduces critical path task resources below 100%"
                    }
                    out = json.dumps(payload)
                    return out

        payload = {"success": True, "recovery_plan": plan, "decision": decision}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveRecoveryPlan",
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
