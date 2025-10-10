# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateChangeRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        new_status = kwargs.get("new_status")
        performed_by = kwargs.get("performed_by")

        if not all([cr_id, new_status, performed_by]):
            return json.dumps(
                {"error": "cr_id, new_status, and performed_by are required"}
            )

        change_requests = data.get("change_requests", [])
        change_history = data.get("change_history", [])
        risk_assessments = data.get("risk_assessments", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        old_status = cr.get("status")

        valid_transitions = {
            "draft": ["in_review", "cancelled"],
            "in_review": ["approved", "pending_approval", "draft", "cancelled"],
            "pending_approval": ["approved", "rejected", "on_hold"],
            "pending": ["approved", "rejected", "on_hold"],
            "approved": ["in_implementation", "cancelled", "approved"],
            "in_implementation": ["completed", "on_hold"],
            "on_hold": ["in_review", "pending_approval", "cancelled"],
            "rejected": ["draft"],
            "completed": [],
            "cancelled": [],
        }

        if new_status not in valid_transitions.get(old_status, []):
            return json.dumps(
                {
                    "error": f"Invalid status transition from '{old_status}' to '{new_status}'"
                }
            )

        if new_status == "pending_approval" and not cr.get("impact_assessment"):
            return json.dumps(
                {
                    "error": "Impact assessment required before moving to pending_approval"
                }
            )

        if new_status == "pending_approval":
            impact = cr.get("impact_assessment", {})
            if impact.get("affects_critical_path") or impact.get("overall_risk") in [
                "high",
                "critical",
            ]:

                has_risk_assessment = any(
                    ra.get("cr_id") == cr_id for ra in risk_assessments
                )
                if not has_risk_assessment:
                    return json.dumps(
                        {
                            "error": "Risk assessment required: This change impacts the critical path or is high-risk. Must have documented mitigation strategies, contingency plans, and rollback procedures.",
                            "requirement": "Please complete risk assessment before proceeding to approval.",
                        }
                    )

                risk_assessment = next(
                    (ra for ra in risk_assessments if ra.get("cr_id") == cr_id), None
                )
                if risk_assessment:
                    if not all(
                        [
                            risk_assessment.get("mitigation_strategies"),
                            risk_assessment.get("contingency_plans"),
                            risk_assessment.get("rollback_procedure"),
                        ]
                    ):
                        return json.dumps(
                            {
                                "error": "Incomplete risk assessment: Must include mitigation strategies, contingency plans, and rollback procedures for critical path/high-risk changes."
                            }
                        )

        if new_status == "approved":
            required_approvals = cr.get("approvals_required", [])
            received_approvals = cr.get("approvals_received", [])
            missing_approvals = list(set(required_approvals) - set(received_approvals))
            if missing_approvals:
                return json.dumps({"error": f"Missing approvals from: {missing_approvals}"})

        cr["status"] = new_status
        cr["updated_date"] = datetime.now().isoformat()

        if new_status == "rejected":
            cr["rejection_date"] = datetime.now().isoformat()

            cr["can_resubmit_after"] = (datetime.now() + timedelta(days=30)).isoformat()
        elif new_status == "approved":
            cr["approval_date"] = datetime.now().isoformat()

        history_entry = {
            "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
            "cr_id": cr_id,
            "action": "status_change",
            "from_status": old_status,
            "to_status": new_status,
            "performed_by": performed_by,
            "timestamp": datetime.now().isoformat(),
        }
        change_history.append(history_entry)

        if new_status == "approved":
            cr["artifacts_pending"] = [
                "budget",
                "resource_plan",
                "schedule",
                "scope_statement",
            ]
            cr["update_deadline"] = datetime.now().isoformat()

        return json.dumps({"success": True, "change_request": cr})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_change_request_status",
                "description": "Update the status of a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "new_status": {
                            "type": "string",
                            "description": "New status: draft, in_review, pending_approval, approved, rejected, on_hold, in_implementation, completed, cancelled",
                        },
                        "performed_by": {
                            "type": "string",
                            "description": "ID of person updating status",
                        },
                    },
                    "required": ["cr_id", "new_status", "performed_by"],
                },
            },
        }
