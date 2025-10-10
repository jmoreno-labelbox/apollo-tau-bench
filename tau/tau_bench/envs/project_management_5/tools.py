import json
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from domains.dto import Tool


class CreateChangeRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get("title")
        description = kwargs.get("description")
        requester_id = kwargs.get("requester_id")
        project_id = kwargs.get("project_id")
        change_type = kwargs.get("change_type")
        priority = kwargs.get("priority", "medium")
        affected_deliverables = kwargs.get("affected_deliverables", [])
        business_justification = kwargs.get("business_justification")

        if not all(
            [
                title,
                description,
                requester_id,
                project_id,
                change_type,
                business_justification,
            ]
        ):
            return json.dumps(
                {
                    "error": "title, description, requester_id, project_id, change_type, and business_justification are required"
                }
            )

        change_requests = data.get("change_requests", [])
        projects = data.get("projects", [])
        scope_baselines = data.get("scope_baselines", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project '{project_id}' not found"})

        project_baseline = next(
            (
                b
                for b in scope_baselines
                if b.get("project_id") == project_id and b.get("status") == "approved"
            ),
            None,
        )
        if not project_baseline:
            return json.dumps(
                {
                    "error": "Cannot create change request: No approved scope baseline exists for this project. A baseline must be formally established and approved first."
                }
            )

        if not all(
            [
                project_baseline.get("deliverables"),
                project_baseline.get("acceptance_criteria"),
                project_baseline.get("metrics"),
            ]
        ):
            return json.dumps(
                {
                    "error": "Cannot create change request: Existing baseline is incomplete. It must include deliverables, acceptance criteria, and success metrics."
                }
            )

        baseline_version = project_baseline.get("version", "1.0")

        active_crs = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id
            and cr.get("status")
            in [
                "draft",
                "in_review",
                "pending_approval",
                "approved",
                "in_implementation",
            ]
        ]

        for active_cr in active_crs:
            overlapping_deliverables = set(affected_deliverables).intersection(
                set(active_cr.get("affected_deliverables", []))
            )
            if overlapping_deliverables:
                return json.dumps(
                    {
                        "error": f"Cannot create change request: Deliverables {list(overlapping_deliverables)} are already affected by active change request '{active_cr.get('cr_id')}'. Multiple change requests affecting the same deliverable must be consolidated.",
                        "suggestion": "Please merge with existing change request or wait for it to complete.",
                    }
                )

        rejected_crs = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id
            and cr.get("status") == "rejected"
            and cr.get("requester_id") == requester_id
        ]

        for rejected_cr in rejected_crs:

            if (
                title.lower() in rejected_cr.get("title", "").lower()
                or rejected_cr.get("title", "").lower() in title.lower()
                or description[:50].lower()
                in rejected_cr.get("description", "").lower()
            ):

                can_resubmit_after = rejected_cr.get("can_resubmit_after")
                if (
                    can_resubmit_after
                    and datetime.now().isoformat() < can_resubmit_after
                ):
                    days_remaining = (
                        datetime.fromisoformat(can_resubmit_after) - datetime.now()
                    ).days
                    return json.dumps(
                        {
                            "error": f"Cannot create change request: This appears to be a resubmission of rejected CR '{rejected_cr.get('cr_id')}'. Rejected change requests have a 30-day cooling period.",
                            "days_remaining": days_remaining,
                            "can_resubmit_after": can_resubmit_after,
                            "requirement": "Resubmitted requests must include new justification addressing original rejection reasons and demonstrate changed circumstances.",
                        }
                    )

                if (
                    rejected_cr.get("rejection_reason")
                    and rejected_cr.get("rejection_reason").lower()
                    not in business_justification.lower()
                ):
                    return json.dumps(
                        {
                            "error": f"Resubmission detected: Please address the original rejection reason in your business justification.",
                            "original_rejection_reason": rejected_cr.get(
                                "rejection_reason"
                            ),
                        }
                    )

        cr_id = kwargs.get("cr_id", f"cr_{uuid.uuid4().hex[:8]}")

        new_cr = {
            "cr_id": cr_id,
            "title": title,
            "description": description,
            "requester_id": requester_id,
            "project_id": project_id,
            "change_type": change_type,
            "priority": priority,
            "affected_deliverables": affected_deliverables,
            "business_justification": business_justification,
            "status": "draft",
            "created_date": datetime.now().isoformat(),
            "baseline_version": baseline_version,
            "requires_emergency_approval": False,
            "approvals_required": [],
            "approvals_received": [],
        }

        change_requests.append(new_cr)

        change_history = data.get("change_history", [])
        history_entry = {
            "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
            "cr_id": cr_id,
            "action": "created",
            "performed_by": requester_id,
            "timestamp": datetime.now().isoformat(),
        }
        change_history.append(history_entry)

        return json.dumps({"success": True, "change_request": new_cr})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_change_request",
                "description": "Create a new change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Title of the change request",
                        },
                        "description": {
                            "type": "string",
                            "description": "Detailed description of the change",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "ID of the person requesting the change",
                        },
                        "cr_id": {
                            "type": "string",
                            "description": "ID of the change request",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "Project ID affected by the change",
                        },
                        "change_type": {
                            "type": "string",
                            "description": "Type: scope_addition, scope_reduction, requirement_change, schedule_change",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority: low, medium, high, critical",
                        },
                        "affected_deliverables": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of affected deliverable IDs",
                        },
                        "business_justification": {
                            "type": "string",
                            "description": "Business justification for the change",
                        },
                    },
                    "required": [
                        "title",
                        "description",
                        "requester_id",
                        "project_id",
                        "change_type",
                        "business_justification",
                    ],
                },
            },
        }


class PerformImpactAssessment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        assessed_by = kwargs.get("assessed_by")
        timeline_impact_weeks = kwargs.get("timeline_impact_weeks", 0)
        budget_impact = kwargs.get("budget_impact", 0)
        resource_requirements = kwargs.get("resource_requirements", [])
        technical_dependencies = kwargs.get("technical_dependencies", [])

        if not all([cr_id, assessed_by]):
            return json.dumps({"error": "cr_id and assessed_by are required"})

        change_requests = data.get("change_requests", [])
        budgets = data.get("budgets", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        project_budget = next(
            (b for b in budgets if b.get("project_id") == cr.get("project_id")), None
        )
        budget_impact_percentage = 0
        if project_budget and budget_impact:
            total_budget = project_budget.get("total_budget", 0)
            budget_impact_percentage = (
                (budget_impact / total_budget * 100) if total_budget > 0 else 0
            )

        allocations = data.get("allocations", [])
        resource_conflicts = []
        for req in resource_requirements:
            emp_id = req.get("employee_id")
            emp_allocations = [
                a
                for a in allocations
                if a.get("employee_id") == emp_id and a.get("status") == "active"
            ]
            total_hours = sum(a.get("hours_per_week", 0) for a in emp_allocations)
            if total_hours + req.get("hours_per_week", 0) > 40:
                resource_conflicts.append(emp_id)

        critical_paths = data.get("critical_paths", [])
        project_critical_path = next(
            (
                cp
                for cp in critical_paths
                if cp.get("project_id") == cr.get("project_id")
            ),
            None,
        )
        affects_critical_path = False
        if project_critical_path and timeline_impact_weeks > 0:
            affects_critical_path = True

        requires_risk_assessment = affects_critical_path

        approval_levels_required = ["project_manager"]
        if budget_impact > 50000 or budget_impact_percentage > 10:
            approval_levels_required.append("finance")
        if affects_critical_path or timeline_impact_weeks > 4:
            approval_levels_required.append("pmo_director")
        if cr.get("priority") == "critical" or budget_impact > 100000:
            approval_levels_required.append("executive_sponsor")

        risk_score = 0
        if timeline_impact_weeks > 8:
            risk_score += 3
        elif timeline_impact_weeks > 4:
            risk_score += 2
        elif timeline_impact_weeks > 0:
            risk_score += 1

        if budget_impact_percentage > 20:
            risk_score += 3
        elif budget_impact_percentage > 10:
            risk_score += 2
        elif budget_impact_percentage > 5:
            risk_score += 1

        if len(resource_conflicts) > 2:
            risk_score += 3
        elif len(resource_conflicts) > 0:
            risk_score += 2

        overall_risk = (
            "critical"
            if risk_score >= 6
            else "high"
            if risk_score >= 4
            else "medium"
            if risk_score >= 2
            else "low"
        )

        assessment_id = f"ia_{uuid.uuid4().hex[:8]}"

        impact_assessment = {
            "assessment_id": assessment_id,
            "cr_id": cr_id,
            "assessed_by": assessed_by,
            "assessment_date": datetime.now().isoformat(),
            "timeline_impact_weeks": timeline_impact_weeks,
            "budget_impact": budget_impact,
            "budget_impact_percentage": round(budget_impact_percentage, 1),
            "resource_requirements": resource_requirements,
            "resource_conflicts": resource_conflicts,
            "technical_dependencies": technical_dependencies,
            "affects_critical_path": affects_critical_path,
            "requires_risk_assessment": requires_risk_assessment,
            "approval_levels_required": approval_levels_required,
            "overall_risk": overall_risk,
        }

        cr["impact_assessment"] = impact_assessment
        cr["approvals_required"] = approval_levels_required
        cr["requires_risk_assessment"] = requires_risk_assessment

        return json.dumps({"success": True, "impact_assessment": impact_assessment})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_impact_assessment",
                "description": "Perform impact assessment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "assessed_by": {
                            "type": "string",
                            "description": "ID of person performing assessment",
                        },
                        "timeline_impact_weeks": {
                            "type": "number",
                            "description": "Impact on timeline in weeks",
                        },
                        "budget_impact": {
                            "type": "number",
                            "description": "Budget impact in dollars",
                        },
                        "resource_requirements": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "employee_id": {"type": "string"},
                                    "hours_per_week": {"type": "number"},
                                    "duration_weeks": {"type": "number"},
                                },
                            },
                            "description": "Additional resource requirements",
                        },
                        "technical_dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Technical dependencies",
                        },
                    },
                    "required": ["cr_id", "assessed_by"],
                },
            },
        }


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


class ProcessEmergencyChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        authorized_by = kwargs.get("authorized_by")
        emergency_type = kwargs.get("emergency_type")
        justification = kwargs.get("justification")

        if not all([cr_id, authorized_by, emergency_type, justification]):
            return json.dumps(
                {
                    "error": "cr_id, authorized_by, emergency_type, and justification are required"
                }
            )

        change_requests = data.get("change_requests", [])
        emergency_logs = data.get("emergency_logs", [])
        approval_workflows = data.get("approval_workflows", [])
        stakeholders = data.get("stakeholders", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        authorizer = next(
            (s for s in stakeholders if s.get("stakeholder_id") == authorized_by), None
        )
        if not authorizer or "emergency" not in str(
            authorizer.get("approval_authority", [])
        ):

            if not authorizer or authorizer.get("role") not in [
                "executive_sponsor",
                "pmo_director",
            ]:
                return json.dumps(
                    {"error": "Authorizer does not have emergency approval authority"}
                )

        current_time = datetime.now()
        documentation_deadline = (current_time + timedelta(hours=24)).isoformat()
        retroactive_approval_deadline = (current_time + timedelta(hours=48)).isoformat()

        log_id = kwargs.get("log_id", f"elog_{uuid.uuid4().hex[:8]}")

        emergency_log = {
            "log_id": log_id,
            "cr_id": cr_id,
            "authorized_by": authorized_by,
            "emergency_type": emergency_type,
            "justification": justification,
            "timestamp": current_time.isoformat(),
            "documentation_deadline": documentation_deadline,
            "retroactive_approval_deadline": retroactive_approval_deadline,
            "retroactive_status": "pending",
            "retroactive_approvers": [],
            "requires_automatic_rollback": True,
        }

        emergency_logs.append(emergency_log)

        cr["status"] = "approved"
        cr["approval_date"] = current_time.isoformat()
        cr["requires_emergency_approval"] = True
        cr["emergency_log_id"] = log_id
        cr["emergency_documentation_deadline"] = documentation_deadline
        cr["emergency_retroactive_deadline"] = retroactive_approval_deadline

        workflow_id = f"wf_{uuid.uuid4().hex[:8]}"

        emergency_workflow = {
            "workflow_id": workflow_id,
            "cr_id": cr_id,
            "workflow_type": "emergency",
            "steps": [
                {
                    "step_number": 1,
                    "approval_level": "emergency_approver",
                    "approver_id": authorized_by,
                    "status": "approved",
                    "required": True,
                    "can_delegate": False,
                    "action_date": current_time.isoformat(),
                }
            ],
            "current_step": 1,
            "status": "completed",
            "created_date": current_time.isoformat(),
            "retroactive_approval_required": True,
            "retroactive_deadline": retroactive_approval_deadline,
        }

        approval_workflows.append(emergency_workflow)

        return json.dumps(
            {
                "success": True,
                "emergency_approval": {
                    "cr_id": cr_id,
                    "log_id": log_id,
                    "status": "approved",
                    "requires_retroactive_approval": True,
                    "documentation_deadline": documentation_deadline,
                    "retroactive_approval_deadline": retroactive_approval_deadline,
                    "warning": "Must be documented within 24 hours and receive retroactive approval within 48 hours or automatic rollback will be triggered",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_emergency_change",
                "description": "Process an emergency change request with expedited approval",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "log_id": {"type": "string", "description": "Log ID"},
                        "authorized_by": {
                            "type": "string",
                            "description": "Emergency authorizer ID",
                        },
                        "emergency_type": {
                            "type": "string",
                            "description": "Type: production_fix, security_patch, compliance_requirement, data_integrity",
                        },
                        "justification": {
                            "type": "string",
                            "description": "Emergency justification",
                        },
                    },
                    "required": [
                        "cr_id",
                        "authorized_by",
                        "emergency_type",
                        "justification",
                    ],
                },
            },
        }


class RecordRetroactiveApproval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        emergency_log_id = kwargs.get("emergency_log_id")
        approver_id = kwargs.get("approver_id")
        approval_decision = kwargs.get("approval_decision")
        comments = kwargs.get("comments", "")

        if not all([emergency_log_id, approver_id, approval_decision]):
            return json.dumps(
                {
                    "error": "emergency_log_id, approver_id, and approval_decision are required"
                }
            )

        emergency_logs = data.get("emergency_logs", [])
        change_requests = data.get("change_requests", [])

        log = next(
            (e for e in emergency_logs if e.get("log_id") == emergency_log_id), None
        )
        if not log:
            return json.dumps(
                {"error": f"Emergency log '{emergency_log_id}' not found"}
            )

        if log.get("retroactive_status") != "pending":
            return json.dumps(
                {"error": f"Emergency log already {log.get('retroactive_status')}"}
            )

        current_time = datetime.now()
        deadline = datetime.fromisoformat(
            log.get("retroactive_approval_deadline")
            .replace("Z", "+00:00")
            .replace("+00:00", "")
        )

        if current_time > deadline:

            log["retroactive_status"] = "failed_deadline"
            log["automatic_rollback_triggered"] = True
            log["rollback_trigger_date"] = current_time.isoformat()

            cr = next(
                (c for c in change_requests if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()

            return json.dumps(
                {
                    "error": "Retroactive approval deadline exceeded. Automatic rollback has been triggered.",
                    "deadline_was": log.get("retroactive_approval_deadline"),
                    "current_time": current_time.isoformat(),
                    "rollback_triggered": True,
                }
            )

        if "retroactive_approvers" not in log:
            log["retroactive_approvers"] = []

        log["retroactive_approvers"].append(approver_id)

        if approval_decision == "approve":
            log["retroactive_status"] = "approved"
            log["retroactive_approval_date"] = current_time.isoformat()
            log["approval_comments"] = comments
        else:
            log["retroactive_status"] = "rejected"
            log["retroactive_rejection_date"] = current_time.isoformat()
            log["rejection_comments"] = comments

            cr = next(
                (c for c in change_requests if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()
                log["automatic_rollback_triggered"] = True

        return json.dumps(
            {
                "success": True,
                "retroactive_approval": {
                    "log_id": emergency_log_id,
                    "decision": approval_decision,
                    "status": log["retroactive_status"],
                    "rollback_triggered": log.get(
                        "automatic_rollback_triggered", False
                    ),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_retroactive_approval",
                "description": "Record retroactive approval for emergency changes",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "emergency_log_id": {
                            "type": "string",
                            "description": "Emergency log ID",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Retroactive approver ID",
                        },
                        "approval_decision": {
                            "type": "string",
                            "description": "Decision: approve or reject",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Approval comments",
                        },
                    },
                    "required": [
                        "emergency_log_id",
                        "approver_id",
                        "approval_decision",
                    ],
                },
            },
        }


class CheckChangeConflicts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        compare_to_cr_id = kwargs.get("compare_to_cr_id")

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        project_id = cr.get("project_id")
        conflicts = []

        if compare_to_cr_id:
            active_crs = [
                c
                for c in change_requests
                if c.get("project_id") == project_id
                   and c.get("cr_id") == compare_to_cr_id
                   and c.get("status")
                   in ["pending_approval", "in_review", "approved", "draft"]
            ]
        else:
            active_crs = [
                c
                for c in change_requests
                if c.get("project_id") == project_id
                and c.get("cr_id") != cr_id
                and c.get("status")
                in ["pending_approval", "in_review", "approved", "draft"]
            ]

        cr_deliverables = set(cr.get("affected_deliverables", []))
        for other_cr in active_crs:
            other_deliverables = set(other_cr.get("affected_deliverables", []))
            if overlap := cr_deliverables.intersection(other_deliverables):
                conflicts.append(
                    {
                        "type": "deliverable_conflict",
                        "conflicting_cr": other_cr.get("cr_id"),
                        "conflicting_deliverables": list(overlap),
                        "severity": "critical",
                        "rule_violation": "Multiple change requests affecting the same deliverable must be consolidated",
                        "action_required": "Merge with existing CR or wait for completion",
                    }
                )

        if impact := cr.get("impact_assessment"):
            cr_resources = {
                r.get("employee_id") for r in impact.get("resource_requirements", [])
            }

            for other_cr in active_crs:
                if other_impact := other_cr.get("impact_assessment"):
                    other_resources = {
                        r.get("employee_id")
                        for r in other_impact.get("resource_requirements", [])
                    }
                    if resource_overlap := cr_resources.intersection(other_resources):
                        conflicts.append(
                            {
                                "type": "resource_conflict",
                                "conflicting_cr": other_cr.get("cr_id"),
                                "conflicting_resources": list(resource_overlap),
                                "severity": "medium",
                            }
                        )

        if cr.get("change_type") == "schedule_change":
            for other_cr in active_crs:
                if other_cr.get("change_type") == "schedule_change":
                    conflicts.append(
                        {
                            "type": "schedule_conflict",
                            "conflicting_cr": other_cr.get("cr_id"),
                            "description": "Multiple schedule changes pending",
                            "severity": "high",
                        }
                    )

        if cr.get("change_type") in ["scope_addition", "scope_reduction"]:
            opposite_type = (
                "scope_reduction"
                if cr.get("change_type") == "scope_addition"
                else "scope_addition"
            )
            for other_cr in active_crs:
                if other_cr.get("change_type") == opposite_type:
                    conflicts.append(
                        {
                            "type": "scope_conflict",
                            "conflicting_cr": other_cr.get("cr_id"),
                            "description": "Conflicting scope changes (addition vs reduction)",
                            "severity": "critical",
                        }
                    )

        has_rule_violations = any(c.get("rule_violation") for c in conflicts)

        return json.dumps(
            {
                "cr_id": cr_id,
                "conflicts_found": len(conflicts),
                "has_rule_violations": has_rule_violations,
                "conflicts": conflicts,
                "recommendation": "Cannot proceed - consolidate with conflicting CRs"
                if has_rule_violations
                else "Coordinate with conflicting CRs"
                if conflicts
                else "No conflicts found",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_change_conflicts",
                "description": "Check for conflicts with other change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {
                            "type": "string",
                            "description": "Change request ID to check",
                        },
                        "compare_to_cr_id": {
                            "type": "string",
                            "description": "Change request ID to compare with cr_id",
                        }
                    },
                    "required": ["cr_id"],
                },
            },
        }


class SaveChangeRequestsConflicts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        conflicting_cr_id = kwargs.get("conflicting_cr_id")
        conflict_type = kwargs.get("type")
        conflicting_deliverables = kwargs.get("conflicting_deliverables")
        severity = kwargs.get("severity")
        rule_violation = kwargs.get("rule_violation")
        action_required = kwargs.get("action_required")
        recommendation = kwargs.get("recommendation")

        if not cr_id or not conflicting_cr_id:
            return json.dumps({"error": "cr_id and conflicting_cr_id are required parameters"})

        conflict_cr_id_1 = {
            "conflicting_cr_id": conflicting_cr_id,
            "conflict_id": f"cf_{uuid.uuid4().hex[:8]}"
        }
        if conflict_type:
            conflict_cr_id_1["conflict_type"] = conflict_type
        if conflicting_deliverables:
            conflict_cr_id_1["conflicting_deliverables"] = conflicting_deliverables
        if severity:
            conflict_cr_id_1["severity"] = severity
        if rule_violation:
            conflict_cr_id_1["rule_violation"] = rule_violation
        if action_required:
            conflict_cr_id_1["action_required"] = action_required
        if recommendation:
            conflict_cr_id_1["recommendation"] = recommendation

        change_requests = data.get("change_requests", [])
        for change_request in change_requests:
            if change_request.get("cr_id") == cr_id:
                if "conflicts" in change_request:
                    change_request["conflicts"].append(conflict_cr_id_1)
                else:
                    change_request["conflicts"] = [conflict_cr_id_1]

                return json.dumps({"success": True})

            elif change_request.get("cr_id") == conflicting_cr_id:
                conflict_cr_id_2 = conflict_cr_id_1.copy()
                conflict_cr_id_2["conflicting_cr_id"] = cr_id
                if "conflicts" in change_request:
                    change_request["conflicts"].append(conflict_cr_id_2)
                else:
                    change_request["conflicts"] = [conflict_cr_id_2]

        return json.dumps({"error": f"It wasn't found any change request with the ID {cr_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_change_requests_conflicts",
                "description": "Save conflicts into change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {
                            "type": "string",
                            "description": "Change request ID to save conflicts",
                        },
                        "type": {
                            "type": "string",
                            "description": "Conflict type",
                        },
                        "conflicting_cr_id": {
                            "type": "string",
                            "description": "Conflicting change request ID",
                        },
                        "conflicting_deliverables": {
                            "type": "list",
                            "description": "Conflicting deliverable IDs",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Conflict severity",
                        },
                        "rule_violation": {
                            "type": "string",
                            "description": "Rule violation description",
                        },
                        "action_required": {
                            "type": "string",
                            "description": "Action required description",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Recommendation description",
                        }
                    },
                    "required": ["cr_id", "conflicting_cr"],
                },
            },
        }


class ValidateChangeCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        compliance_checklist = kwargs.get("compliance_checklist", [])

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])
        emergency_logs = data.get("emergency_logs", [])
        risk_assessments = data.get("risk_assessments", [])
        scope_baselines = data.get("scope_baselines", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        violations = []
        warnings = []

        default_checks = [
            "has_business_justification",
            "has_impact_assessment",
            "has_risk_assessment",
            "proper_approval_sequence",
            "artifacts_updated",
            "within_budget_threshold",
            "baseline_exists",
            "no_deliverable_conflicts",
            "cooling_period_observed",
            "emergency_deadlines_met",
            "critical_path_risk_assessed",
        ]

        checks_to_perform = (
            compliance_checklist if compliance_checklist else default_checks
        )

        for check in checks_to_perform:
            if check == "has_business_justification":
                if not cr.get("business_justification"):
                    violations.append("Missing business justification")

            elif check == "has_impact_assessment":
                if cr.get("status") not in ["draft", "cancelled"] and not cr.get(
                    "impact_assessment"
                ):
                    violations.append("Missing impact assessment")

            elif check == "has_risk_assessment":
                risk_assessments = data.get("risk_assessments", [])
                has_risk = any(ra.get("cr_id") == cr_id for ra in risk_assessments)
                if cr.get("priority") in ["high", "critical"] and not has_risk:
                    warnings.append("High priority change without risk assessment")

            elif check == "proper_approval_sequence":
                if cr.get("status") == "approved":
                    required = cr.get("approvals_required", [])
                    received = cr.get("approvals_received", [])
                    if set(required) != set(received):
                        violations.append(
                            f"Incomplete approvals: missing {list(set(required) - set(received))}"
                        )

            elif check == "artifacts_updated":
                if cr.get("status") == "approved" and cr.get("artifacts_pending", []):
                    deadline = cr.get("update_deadline")
                    if deadline and deadline < datetime.now().isoformat():
                        violations.append(
                            f"Overdue artifact updates: {cr.get('artifacts_pending')}"
                        )
                    else:
                        warnings.append(
                            f"Pending artifact updates: {cr.get('artifacts_pending')}"
                        )

            elif check == "within_budget_threshold":
                if impact := cr.get("impact_assessment"):
                    if impact.get(
                        "budget_impact", 0
                    ) > 100000 and "executive_sponsor" not in cr.get(
                        "approvals_required", []
                    ):
                        violations.append(
                            "Budget impact >$100k requires executive approval"
                        )

            elif check == "baseline_exists":
                project_baseline = next(
                    (
                        b
                        for b in scope_baselines
                        if b.get("project_id") == cr.get("project_id")
                        and b.get("status") == "approved"
                    ),
                    None,
                )
                if not project_baseline:
                    violations.append(
                        "RULE 2 VIOLATION: No approved scope baseline exists for project"
                    )

            elif check == "no_deliverable_conflicts":
                conflict_check = CheckChangeConflicts.invoke(data, cr_id=cr_id)
                conflict_result = json.loads(conflict_check)
                if conflict_result.get("has_rule_violations"):
                    violations.append(
                        "RULE 3 VIOLATION: Deliverable conflicts exist - must consolidate with other CRs"
                    )

            elif check == "cooling_period_observed":

                if cr.get("status") == "rejected" and cr.get("can_resubmit_after"):
                    if datetime.now().isoformat() < cr.get("can_resubmit_after"):
                        days_remaining = (
                            datetime.fromisoformat(cr.get("can_resubmit_after"))
                            - datetime.now()
                        ).days
                        warnings.append(
                            f"In cooling period: {days_remaining} days remaining before resubmission allowed"
                        )

            elif check == "emergency_deadlines_met":
                if cr.get("requires_emergency_approval"):
                    log = next(
                        (e for e in emergency_logs if e.get("cr_id") == cr_id), None
                    )
                    if log:
                        current_time = datetime.now()

                        doc_deadline = datetime.fromisoformat(
                            log.get("documentation_deadline", "")
                            .replace("Z", "+00:00")
                            .replace("+00:00", "")
                        )
                        if (
                            current_time > doc_deadline
                            and log.get("retroactive_status") == "pending"
                        ):
                            violations.append(
                                "RULE 1 VIOLATION: Emergency change documentation overdue (24-hour deadline exceeded)"
                            )

                        retro_deadline = datetime.fromisoformat(
                            log.get("retroactive_approval_deadline", "")
                            .replace("Z", "+00:00")
                            .replace("+00:00", "")
                        )
                        if (
                            current_time > retro_deadline
                            and log.get("retroactive_status") == "pending"
                        ):
                            violations.append(
                                "RULE 1 VIOLATION: Emergency change retroactive approval overdue (48-hour deadline exceeded) - automatic rollback required"
                            )

            elif check == "critical_path_risk_assessed":
                if impact := cr.get("impact_assessment"):
                    if (
                        impact.get("affects_critical_path")
                        and cr.get("status") != "draft"
                    ):
                        risk_assessment = next(
                            (ra for ra in risk_assessments if ra.get("cr_id") == cr_id),
                            None,
                        )
                        if not risk_assessment:
                            violations.append(
                                "RULE 5 VIOLATION: Critical path change without risk assessment"
                            )
                        elif not all(
                            [
                                risk_assessment.get("mitigation_strategies"),
                                risk_assessment.get("contingency_plans"),
                                risk_assessment.get("rollback_procedure"),
                            ]
                        ):
                            violations.append(
                                "RULE 5 VIOLATION: Critical path change with incomplete risk assessment (missing mitigation/contingency/rollback)"
                            )

        compliance_status = "compliant" if not violations else "non_compliant"

        return json.dumps(
            {
                "cr_id": cr_id,
                "compliance_status": compliance_status,
                "violations": violations,
                "warnings": warnings,
                "checks_performed": checks_to_perform,
                "recommendation": "Address violations before proceeding"
                if violations
                else "Proceed with caution"
                if warnings
                else "Fully compliant",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_change_compliance",
                "description": "Validate change request compliance with policies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "compliance_checklist": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific compliance checks to perform",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }


class CreateApprovalWorkflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        workflow_type = kwargs.get("workflow_type", "standard")

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])
        approval_workflows = data.get("approval_workflows", [])
        stakeholders = data.get("stakeholders", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        existing = [i for i in range(len(approval_workflows)) if approval_workflows[i].get("cr_id") == cr_id]
        for drop_index in existing:
            approval_workflows.pop(drop_index)

        steps = []
        step_number = 1

        approval_mapping = {
            "project_manager": {"role": "project_manager", "can_delegate": True},
            "technical_lead": {"role": "technical_lead", "can_delegate": True},
            "finance": {"role": "finance_director", "can_delegate": False},
            "pmo_director": {"role": "pmo_director", "can_delegate": True},
            "executive_sponsor": {"role": "executive_sponsor", "can_delegate": False},
        }

        for approval_level in cr.get("approvals_required", []):
            if approval_level in approval_mapping:
                mapping = approval_mapping[approval_level]

                approver = next(
                    (s for s in stakeholders if mapping["role"] in s.get("role", "")),
                    None,
                )

                if approver:
                    steps.append(
                        {
                            "step_number": step_number,
                            "approval_level": approval_level,
                            "approver_id": approver.get("stakeholder_id"),
                            "status": "pending",
                            "required": True,
                            "can_delegate": mapping["can_delegate"],
                        }
                    )
                    step_number += 1

        workflow_id = f"wf_{uuid.uuid4().hex[:8]}"

        new_workflow = {
            "workflow_id": workflow_id,
            "cr_id": cr_id,
            "workflow_type": workflow_type,
            "steps": steps,
            "current_step": 1,
            "status": "active",
            "created_date": datetime.now().isoformat(),
        }

        approval_workflows.append(new_workflow)

        if cr.get("status") == "pending_approval" and not steps:
            cr["status"] = "approved"
            cr["approval_date"] = datetime.now().isoformat()

        return json.dumps({"success": True, "workflow": new_workflow})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_approval_workflow",
                "description": "Create approval workflow for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "workflow_type": {
                            "type": "string",
                            "description": "Workflow type: standard, expedited, emergency",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }


class CheckWorkflowExistsForChangeRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        approval_workflows = data.get("approval_workflows", [])

        existing = next(
            (w for w in approval_workflows if w.get("cr_id") == cr_id), None
        )
        if existing:
            return json.dumps({"success": True, "exists": True})

        return json.dumps({"success": True, "exists": False})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_workflow_exists_for_change_request",
                "description": "Check if a workflow exists for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                    },
                    "required": ["cr_id"],
                },
            },
        }


class RecordApprovalDecision(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        approver_id = kwargs.get("approver_id")
        decision = kwargs.get("decision")
        comments = kwargs.get("comments", "")
        conditions = kwargs.get("conditions", [])

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

        change_requests = data.get("change_requests", [])
        approval_workflows = data.get("approval_workflows", [])
        change_approvals = data.get("change_approvals", [])

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

        approval_id = kwargs.get("approval_id", f"appr_ch_{uuid.uuid4().hex[:8]}")

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


class SearchChangeRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        status = kwargs.get("status")
        priority = kwargs.get("priority")
        change_type = kwargs.get("change_type")
        requester_id = kwargs.get("requester_id")
        include_impact = kwargs.get("include_impact", False)

        change_requests = data.get("change_requests", [])
        results = []

        for cr in change_requests:
            match = True

            if project_id and cr.get("project_id") != project_id:
                match = False
            if status and cr.get("status") != status:
                match = False
            if priority and cr.get("priority") != priority:
                match = False
            if change_type and cr.get("change_type") != change_type:
                match = False
            if requester_id and cr.get("requester_id") != requester_id:
                match = False

            if match:
                result = cr.copy()
                if not include_impact and "impact_assessment" in result:

                    result["has_impact_assessment"] = True
                    result["overall_risk"] = cr.get("impact_assessment", {}).get(
                        "overall_risk"
                    )
                    del result["impact_assessment"]
                results.append(result)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_change_requests",
                "description": "Search for change requests by various criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "Filter by project ID",
                        },
                        "status": {"type": "string", "description": "Filter by status"},
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority",
                        },
                        "change_type": {
                            "type": "string",
                            "description": "Filter by change type",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "Filter by requester",
                        },
                        "include_impact": {
                            "type": "boolean",
                            "description": "Include full impact assessment details",
                        },
                    },
                },
            },
        }


class TrackArtifactUpdates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        artifact_type = kwargs.get("artifact_type")
        update_description = kwargs.get("update_description")
        version_before = kwargs.get("version_before")
        version_after = kwargs.get("version_after")
        updated_by = kwargs.get("updated_by")

        if not all(
            [cr_id, artifact_type, update_description, version_after, updated_by]
        ):
            return json.dumps(
                {
                    "error": "cr_id, artifact_type, update_description, version_after, and updated_by are required"
                }
            )

        change_requests = data.get("change_requests", [])
        artifact_updates = data.get("artifact_updates", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        if cr.get("status") != "approved":
            return json.dumps(
                {"error": "Can only update artifacts for approved change requests"}
            )

        update_id = kwargs.get("update_id", f"au_{uuid.uuid4().hex[:8]}")

        artifact_update = {
            "update_id": update_id,
            "cr_id": cr_id,
            "artifact_type": artifact_type,
            "update_description": update_description,
            "version_before": version_before,
            "version_after": version_after,
            "updated_by": updated_by,
            "update_date": datetime.now().isoformat(),
        }

        artifact_updates.append(artifact_update)

        if "artifacts_updated" not in cr:
            cr["artifacts_updated"] = []
        if artifact_type not in cr["artifacts_updated"]:
            cr["artifacts_updated"].append(artifact_type)

        if "artifacts_pending" in cr and artifact_type in cr["artifacts_pending"]:
            cr["artifacts_pending"].remove(artifact_type)

        all_updated = len(cr.get("artifacts_pending", [])) == 0

        return json.dumps(
            {
                "success": True,
                "artifact_update": artifact_update,
                "all_artifacts_updated": all_updated,
                "remaining_artifacts": cr.get("artifacts_pending", []),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "track_artifact_updates",
                "description": "Track updates to project artifacts after change approval",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "update_id": {"type": "string", "description": "Update ID"},
                        "artifact_type": {
                            "type": "string",
                            "description": "Type: budget, schedule, resource_plan, scope_statement, requirements",
                        },
                        "update_description": {
                            "type": "string",
                            "description": "Description of the update",
                        },
                        "version_before": {
                            "type": "string",
                            "description": "Version before update",
                        },
                        "version_after": {
                            "type": "string",
                            "description": "Version after update",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Person updating the artifact",
                        },
                    },
                    "required": [
                        "cr_id",
                        "artifact_type",
                        "update_description",
                        "version_after",
                        "updated_by",
                    ],
                },
            },
        }


class CreateScopeBaseline(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        baseline_name = kwargs.get("baseline_name")
        scope_items = kwargs.get("scope_items", [])
        deliverables = kwargs.get("deliverables", [])
        acceptance_criteria = kwargs.get("acceptance_criteria", {})
        success_metrics = kwargs.get("success_metrics", {})
        created_by = kwargs.get("created_by")

        if not all([project_id, baseline_name, created_by]):
            return json.dumps(
                {"error": "project_id, baseline_name, and created_by are required"}
            )

        if not deliverables:
            return json.dumps({"error": "RULE 2: Baseline must include deliverables"})

        if not acceptance_criteria:
            return json.dumps(
                {"error": "RULE 2: Baseline must include acceptance criteria"}
            )

        if not success_metrics:
            return json.dumps(
                {"error": "RULE 2: Baseline must include success metrics"}
            )

        scope_baselines = data.get("scope_baselines", [])

        existing = next(
            (
                b
                for b in scope_baselines
                if b.get("project_id") == project_id and b.get("status") == "approved"
            ),
            None,
        )
        if existing:

            current_version = existing.get("version", "1.0")
            major, minor = map(int, current_version.split("."))
            new_version = f"{major}.{minor + 1}"
        else:
            new_version = "1.0"

        baseline_id = kwargs.get("baseline_id", f"bl_{uuid.uuid4().hex[:8]}")

        total_hours = sum(d.get("estimated_hours", 0) for d in deliverables)

        new_baseline = {
            "baseline_id": baseline_id,
            "project_id": project_id,
            "baseline_name": baseline_name,
            "version": new_version,
            "scope_items": scope_items,
            "deliverables": deliverables,
            "acceptance_criteria": acceptance_criteria,
            "success_metrics": success_metrics,
            "status": "draft",
            "created_by": created_by,
            "created_date": datetime.now().isoformat(),
            "metrics": {
                "total_deliverables": len(deliverables),
                "total_scope_items": len(scope_items),
                "estimated_effort_hours": total_hours,
                "success_metrics_count": len(success_metrics),
            },
            "change_history": [],
        }

        scope_baselines.append(new_baseline)

        return json.dumps({"success": True, "baseline": new_baseline})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_scope_baseline",
                "description": "Create a new scope baseline for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {"type": "string", "description": "Baseline ID"},
                        "baseline_name": {
                            "type": "string",
                            "description": "Name for the baseline",
                        },
                        "scope_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "description": {"type": "string"},
                                    "category": {"type": "string"},
                                },
                            },
                            "description": "List of scope items",
                        },
                        "deliverables": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "deliverable_id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                    "estimated_hours": {"type": "number"},
                                },
                            },
                            "description": "List of deliverables",
                        },
                        "acceptance_criteria": {
                            "type": "object",
                            "description": "Acceptance criteria mapping",
                        },
                        "success_metrics": {
                            "type": "object",
                            "description": "Success metrics for the project",
                        },
                        "created_by": {"type": "string", "description": "Creator ID"},
                    },
                    "required": ["project_id", "baseline_name", "created_by"],
                },
            },
        }


class CompareAgainstBaseline(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        scope_baselines = data.get("scope_baselines", [])
        change_requests = data.get("change_requests", [])
        deliverables = data.get("deliverables", [])

        if baseline_version := kwargs.get("baseline_version"):
            baseline = next(
                (
                    b
                    for b in scope_baselines
                    if b.get("project_id") == project_id
                    and b.get("version") == baseline_version
                ),
                None,
            )
        else:

            baseline = next(
                (
                    b
                    for b in scope_baselines
                    if b.get("project_id") == project_id
                    and b.get("status") == "approved"
                ),
                None,
            )

        if not baseline:
            return json.dumps(
                {"error": f"No baseline found for project '{project_id}'"}
            )

        baseline_date = baseline.get("approved_date", baseline.get("created_date"))
        approved_changes = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id
            and cr.get("status") == "approved"
            and cr.get("approval_date", "") > baseline_date
        ]

        scope_additions = []
        scope_reductions = []
        requirement_changes = []

        for cr in approved_changes:
            if cr.get("change_type") == "scope_addition":
                scope_additions.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )
            elif cr.get("change_type") == "scope_reduction":
                scope_reductions.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )
            elif cr.get("change_type") == "requirement_change":
                requirement_changes.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )

        total_budget_impact = sum(
            cr.get("impact_assessment", {}).get("budget_impact", 0)
            for cr in approved_changes
        )
        total_timeline_impact = sum(
            cr.get("impact_assessment", {}).get("timeline_impact_weeks", 0)
            for cr in approved_changes
        )

        baseline_deliverable_ids = [
            d.get("deliverable_id") for d in baseline.get("deliverables", [])
        ]
        current_deliverable_ids = [
            d.get("deliverable_id")
            for d in deliverables
            if d.get("project_id") == project_id
        ]

        added_deliverables = list(
            set(current_deliverable_ids) - set(baseline_deliverable_ids)
        )
        removed_deliverables = list(
            set(baseline_deliverable_ids) - set(current_deliverable_ids)
        )

        variance_report = {
            "project_id": project_id,
            "baseline_version": baseline.get("version"),
            "baseline_date": baseline_date,
            "approved_changes_count": len(approved_changes),
            "scope_additions": scope_additions,
            "scope_reductions": scope_reductions,
            "requirement_changes": requirement_changes,
            "cumulative_impact": {
                "budget_variance": total_budget_impact,
                "timeline_variance_weeks": total_timeline_impact,
                "deliverables_added": len(added_deliverables),
                "deliverables_removed": len(removed_deliverables),
            },
            "variance_percentage": round(
                (
                    len(approved_changes)
                    / max(1, len(baseline.get("scope_items", [])))
                    * 100
                ),
                1,
            ),
            "recommendation": "Consider rebaselining"
            if len(approved_changes) > 5 or total_timeline_impact > 8
            else "Within acceptable variance",
        }

        return json.dumps(variance_report, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_against_baseline",
                "description": "Compare current project scope against baseline",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_version": {
                            "type": "string",
                            "description": "Specific baseline version (optional, uses latest if not provided)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class ScheduleChangeReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        review_date = kwargs.get("review_date")
        review_type = kwargs.get("review_type", "quarterly")
        participants = kwargs.get("participants", [])
        scheduled_by = kwargs.get("scheduled_by")

        if not all([project_id, review_date, scheduled_by]):
            return json.dumps(
                {"error": "project_id, review_date, and scheduled_by are required"}
            )

        change_reviews = data.get("change_reviews", [])
        change_requests = data.get("change_requests", [])
        emergency_logs = data.get("emergency_logs", [])

        existing = next(
            (
                r
                for r in change_reviews
                if r.get("project_id") == project_id
                and r.get("review_date") == review_date
            ),
            None,
        )
        if existing:
            return json.dumps(
                {"error": "Review already scheduled for this project and date"}
            )

        pending_changes = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id
            and cr.get("status") in ["pending_approval", "in_review"]
        ]

        approved_changes = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id and cr.get("status") == "approved"
        ]

        emergency_changes_pending = []
        for cr in change_requests:
            if cr.get("project_id") == project_id and cr.get(
                "requires_emergency_approval"
            ):
                log = next(
                    (e for e in emergency_logs if e.get("cr_id") == cr.get("cr_id")),
                    None,
                )
                if log and log.get("retroactive_status") == "pending":
                    emergency_changes_pending.append(
                        {
                            "cr_id": cr.get("cr_id"),
                            "deadline": log.get("retroactive_approval_deadline"),
                            "urgent": True,
                        }
                    )

        review_id = f"rev_{uuid.uuid4().hex[:8]}"

        review_items = []
        for cr in pending_changes:
            review_items.append(
                {
                    "item_type": "change_request",
                    "item_id": cr.get("cr_id"),
                    "status": cr.get("status"),
                    "priority": cr.get("priority"),
                }
            )

        for emergency in emergency_changes_pending:
            review_items.append(
                {
                    "item_type": "emergency_retroactive",
                    "item_id": emergency["cr_id"],
                    "deadline": emergency["deadline"],
                    "urgent": True,
                }
            )

        if len(approved_changes) > 3:
            review_items.append(
                {
                    "item_type": "cumulative_review",
                    "description": "Review cumulative changes for potential rebaseline",
                }
            )

        new_review = {
            "review_id": review_id,
            "review_type": review_type,
            "project_id": project_id,
            "review_date": review_date,
            "participants": participants,
            "scheduled_by": scheduled_by,
            "scheduled_date": datetime.now().isoformat(),
            "status": "scheduled",
            "review_items": review_items,
            "urgent_items": len(emergency_changes_pending),
            "agenda": {
                "pending_changes": len(pending_changes),
                "emergency_items": len(emergency_changes_pending),
                "topics": [
                    "Review pending change requests",
                    "Emergency change retroactive approvals"
                    if emergency_changes_pending
                    else None,
                    "Assess cumulative impact on baseline",
                    "Evaluate resource availability for changes",
                    "Review risk assessments",
                    "Determine if rebaseline is needed",
                ],
            },
        }

        new_review["agenda"]["topics"] = [
            t for t in new_review["agenda"]["topics"] if t
        ]

        change_reviews.append(new_review)

        return json.dumps({"success": True, "review": new_review})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_change_review",
                "description": "Schedule a change control board review meeting",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "review_date": {
                            "type": "string",
                            "description": "Review date (ISO format)",
                        },
                        "review_type": {
                            "type": "string",
                            "description": "Type: quarterly, adhoc, milestone",
                        },
                        "participants": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of participant IDs",
                        },
                        "scheduled_by": {
                            "type": "string",
                            "description": "Person scheduling the review",
                        },
                    },
                    "required": ["project_id", "review_date", "scheduled_by"],
                },
            },
        }


class CalculateCumulativeImpact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        include_pending = kwargs.get("include_pending", False)
        from_date = kwargs.get("from_date")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        change_requests = data.get("change_requests", [])

        project_crs = [
            cr for cr in change_requests if cr.get("project_id") == project_id
        ]

        if from_date:
            project_crs = [
                cr for cr in project_crs if cr.get("created_date", "") >= from_date
            ]

        if include_pending:
            relevant_crs = [
                cr
                for cr in project_crs
                if cr.get("status") in ["approved", "pending_approval", "in_review"]
            ]
        else:
            relevant_crs = [cr for cr in project_crs if cr.get("status") == "approved"]

        total_budget_impact = 0
        total_timeline_impact = 0
        scope_additions = 0
        scope_reductions = 0
        requirement_changes = 0
        resource_additions = []

        for cr in relevant_crs:
            if impact := cr.get("impact_assessment"):
                total_budget_impact += impact.get("budget_impact", 0)
                total_timeline_impact += impact.get("timeline_impact_weeks", 0)
                resource_additions.extend(impact.get("resource_requirements", []))

            change_type = cr.get("change_type")
            if change_type == "scope_addition":
                scope_additions += 1
            elif change_type == "scope_reduction":
                scope_reductions += 1
            elif change_type == "requirement_change":
                requirement_changes += 1

        resource_summary = {}
        for req in resource_additions:
            emp_id = req.get("employee_id")
            if emp_id in resource_summary:
                resource_summary[emp_id] += req.get("hours_per_week", 0)
            else:
                resource_summary[emp_id] = req.get("hours_per_week", 0)

        risk_factors = []
        if total_budget_impact > 100000:
            risk_factors.append("High budget impact")
        if total_timeline_impact > 12:
            risk_factors.append("Significant schedule impact")
        if len(relevant_crs) > 10:
            risk_factors.append("High change volume")
        if len(resource_summary) > 5:
            risk_factors.append("Multiple resource impacts")

        overall_risk = (
            "critical"
            if len(risk_factors) >= 3
            else "high"
            if len(risk_factors) >= 2
            else "medium"
            if risk_factors
            else "low"
        )

        return json.dumps(
            {
                "project_id": project_id,
                "analysis_period": {
                    "from_date": from_date or "project_start",
                    "to_date": datetime.now().isoformat(),
                    "include_pending": include_pending,
                },
                "change_summary": {
                    "total_changes": len(relevant_crs),
                    "approved": len(
                        [cr for cr in relevant_crs if cr.get("status") == "approved"]
                    ),
                    "pending": len(
                        [cr for cr in relevant_crs if cr.get("status") != "approved"]
                    ),
                    "by_type": {
                        "scope_additions": scope_additions,
                        "scope_reductions": scope_reductions,
                        "requirement_changes": requirement_changes,
                    },
                },
                "cumulative_impact": {
                    "total_budget_impact": total_budget_impact,
                    "timeline_impact_weeks": total_timeline_impact,
                    "resources_needed": len(resource_summary),
                    "total_resource_hours": sum(resource_summary.values()),
                },
                "risk_assessment": {
                    "overall_risk": overall_risk,
                    "risk_factors": risk_factors,
                },
                "recommendations": [
                    "Consider project rebaseline" if len(relevant_crs) > 10 else None,
                    "Review resource capacity" if len(resource_summary) > 3 else None,
                    "Update stakeholder expectations"
                    if total_timeline_impact > 8
                    else None,
                ],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_cumulative_impact",
                "description": "Calculate cumulative impact of all changes on a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_pending": {
                            "type": "boolean",
                            "description": "Include pending changes in calculation",
                        },
                        "from_date": {
                            "type": "string",
                            "description": "Start date for analysis (ISO format)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class GenerateChangeReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        report_type = kwargs.get("report_type", "summary")
        include_details = kwargs.get("include_details", False)

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        change_requests = data.get("change_requests", [])
        change_approvals = data.get("change_approvals", [])
        projects = data.get("projects", [])
        emergency_logs = data.get("emergency_logs", [])
        report = {}

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project '{project_id}' not found"})

        def normalize_datetime(dt_str):
            if not dt_str:
                return None

            dt_str = dt_str.replace("Z", "").replace("+00:00", "")

            if "+" in dt_str:
                dt_str = dt_str.split("+")[0]
            try:
                return datetime.fromisoformat(dt_str)
            except:
                return None

        project_crs = [
            cr for cr in change_requests if cr.get("project_id") == project_id
        ]

        if report_type == "summary":

            by_status = {}
            by_type = {}
            by_priority = {}
            emergency_changes = 0
            cooling_period_crs = 0
            conflicts_count = 0
            project_conflicts = {}
            overdue_emergency_approvals = 0
            artifacts_updated_count = 0
            artifacts_pending_count = 0
            approval_times = []

            for cr in project_crs:

                status = cr.get("status")
                by_status[status] = by_status.get(status, 0) + 1

                change_type = cr.get("change_type")
                by_type[change_type] = by_type.get(change_type, 0) + 1

                priority = cr.get("priority")
                by_priority[priority] = by_priority.get(priority, 0) + 1

                if cr.get("requires_emergency_approval"):
                    emergency_changes += 1

                    log = next(
                        (
                            e
                            for e in emergency_logs
                            if e.get("cr_id") == cr.get("cr_id")
                        ),
                        None,
                    )
                    if log and log.get("retroactive_status") == "pending":
                        deadline = normalize_datetime(
                            log.get("retroactive_approval_deadline", "")
                        )
                        if deadline and datetime.now() > deadline:
                            overdue_emergency_approvals += 1

                if cr.get("status") == "rejected" and cr.get("can_resubmit_after"):
                    can_resubmit = normalize_datetime(cr.get("can_resubmit_after"))
                    if can_resubmit and datetime.now() < can_resubmit:
                        cooling_period_crs += 1

                conflicts = cr.get("conflicts", [])
                for conflict in conflicts:
                    if conflict.get("conflict_id") and conflict.get("conflict_id") not in project_conflicts:
                        project_conflicts[conflict.get("conflict_id")] = {
                            "crs_involved": [cr.get("cr_id"), conflict.get("conflicting_cr_id")],
                            "type": conflict.get("type"),
                            "severity": conflict.get("critical"),
                        }
                conflicts_count = len(project_conflicts)

                if cr.get("status") == "approved":
                    artifacts_updated_count += len(cr.get("artifacts_updated", []))
                    artifacts_pending_count += len(cr.get("artifacts_pending", []))

                    created_dt = normalize_datetime(cr.get("created_date"))
                    approved_dt = normalize_datetime(cr.get("approval_date"))
                    if created_dt and approved_dt:
                        approval_times.append((approved_dt - created_dt).days)

            approved_count = by_status.get("approved", 0)
            rejected_count = by_status.get("rejected", 0)
            total_decided = approved_count + rejected_count

            approval_rate = (
                round(approved_count / total_decided * 100, 1)
                if total_decided > 0
                else 0
            )
            rejection_rate = (
                round(rejected_count / total_decided * 100, 1)
                if total_decided > 0
                else 0
            )
            avg_approval_time = (
                round(sum(approval_times) / len(approval_times), 1)
                if approval_times
                else 0
            )

            report = {
                "project_id": project_id,
                "project_name": project.get("name"),
                "report_date": datetime.now().isoformat(),
                "report_type": "summary",
                "statistics": {
                    "total_change_requests": len(project_crs),
                    "by_status": by_status,
                    "by_type": by_type,
                    "by_priority": by_priority,
                    "emergency_changes": emergency_changes,
                    "cooling_period_crs": cooling_period_crs,
                },
                "approval_metrics": {
                    "average_approval_time_days": avg_approval_time,
                    "approval_rate": approval_rate,
                    "rejection_rate": rejection_rate,
                },
                "implementation_status": {
                    "artifacts_updated": artifacts_updated_count,
                    "artifacts_pending": artifacts_pending_count,
                },
                "compliance_issues": {
                    "overdue_emergency_approvals": overdue_emergency_approvals,
                    "conflicts_count": conflicts_count,
                    "conflicts": project_conflicts,
                },
            }

        elif report_type == "detailed":
            report = {
                "project_id": project_id,
                "project_name": project.get("name"),
                "report_date": datetime.now().isoformat(),
                "report_type": "detailed",
                "change_requests": [],
            }

            for cr in project_crs:
                cr_detail = {
                    "cr_id": cr.get("cr_id"),
                    "title": cr.get("title"),
                    "status": cr.get("status"),
                    "priority": cr.get("priority"),
                    "type": cr.get("change_type"),
                    "created_date": cr.get("created_date"),
                    "requester": cr.get("requester_id"),
                }

                if include_details:
                    cr_detail["description"] = cr.get("description")
                    cr_detail["business_justification"] = cr.get(
                        "business_justification"
                    )

                    if impact := cr.get("impact_assessment"):
                        cr_detail["impact_summary"] = {
                            "budget": impact.get("budget_impact"),
                            "timeline_weeks": impact.get("timeline_impact_weeks"),
                            "risk": impact.get("overall_risk"),
                        }

                    cr_approvals = [
                        a for a in change_approvals if a.get("cr_id") == cr.get("cr_id")
                    ]
                    cr_detail["approvals"] = [
                        {
                            "approver": a.get("approver_id"),
                            "decision": a.get("decision"),
                            "date": a.get("action_date"),
                        }
                        for a in cr_approvals
                    ]

                report["change_requests"].append(cr_detail)

        elif report_type == "compliance":

            changes_without_impact_assessment = 0
            changes_without_proper_approval = 0
            emergency_changes_count = 0
            overdue_implementations = 0
            conflicts_count = 0
            project_conflicts = {}
            cooling_period_violations = 0
            overdue_emergency_approvals_count = 0
            missing_risk_assessments = 0
            non_compliant_items = []

            scope_baselines = data.get("scope_baselines", [])
            baseline_exists = any(
                b.get("project_id") == project_id and b.get("status") == "approved"
                for b in scope_baselines
            )
            no_baseline = not baseline_exists

            for cr in project_crs:
                issues = []

                if cr.get("status") not in ["draft", "cancelled"] and not cr.get(
                    "impact_assessment"
                ):
                    issues.append("Missing impact assessment")
                    changes_without_impact_assessment += 1

                if cr.get("status") == "approved":
                    required = set(cr.get("approvals_required", []))
                    received = set(cr.get("approvals_received", []))
                    if required != received:
                        issues.append(f"Missing approvals: {list(required - received)}")
                        changes_without_proper_approval += 1

                conflicts = cr.get("conflicts", [])
                for conflict in conflicts:
                    if conflict.get("conflict_id") and conflict.get("conflict_id") not in project_conflicts:
                        project_conflicts[conflict.get("conflict_id")] = {
                            "crs_involved": [cr.get("cr_id"), conflict.get("conflicting_cr_id")],
                            "conflict_type": conflict.get("conflict_type"),
                            "severity": conflict.get("severity"),
                        }
                conflicts_count = len(project_conflicts)

                if cr.get("requires_emergency_approval"):
                    emergency_changes_count += 1

                    log = next(
                        (
                            e
                            for e in emergency_logs
                            if e.get("cr_id") == cr.get("cr_id")
                        ),
                        None,
                    )
                    if log and log.get("retroactive_status") == "pending":
                        deadline = normalize_datetime(
                            log.get("retroactive_approval_deadline", "")
                        )
                        if deadline and datetime.now() > deadline:
                            issues.append(
                                "RULE 1 VIOLATION: Overdue emergency retroactive approval"
                            )
                            overdue_emergency_approvals_count += 1

                if cr.get("status") == "approved" and cr.get("artifacts_pending", []):
                    update_deadline = normalize_datetime(cr.get("update_deadline", ""))
                    if update_deadline and datetime.now() > update_deadline:
                        issues.append("Overdue artifact updates")
                        overdue_implementations += 1

                if cr.get("requires_risk_assessment"):
                    risk_assessments = data.get("risk_assessments", [])
                    has_risk = any(
                        ra.get("cr_id") == cr.get("cr_id") for ra in risk_assessments
                    )
                    if not has_risk:
                        issues.append(
                            "RULE 5 VIOLATION: Critical path change without risk assessment"
                        )
                        missing_risk_assessments += 1

                if issues:
                    non_compliant_items.append(
                        {
                            "cr_id": cr.get("cr_id"),
                            "title": cr.get("title"),
                            "issues": issues,
                        }
                    )

            report = {
                "project_id": project_id,
                "project_name": project.get("name"),
                "report_date": datetime.now().isoformat(),
                "report_type": "compliance",
                "compliance_summary": {
                    "total_change_requests": len(project_crs),
                    "changes_without_impact_assessment": changes_without_impact_assessment,
                    "changes_without_proper_approval": changes_without_proper_approval,
                    "emergency_changes": emergency_changes_count,
                    "overdue_implementations": overdue_implementations,
                    "rule_violations": {
                        "no_baseline": no_baseline,
                        "conflicts_count": conflicts_count,
                        "project_conflicts": project_conflicts,
                        "cooling_period_violations": cooling_period_violations,
                        "overdue_emergency_approvals": overdue_emergency_approvals_count,
                        "missing_risk_assessments": missing_risk_assessments,
                    },
                },
                "non_compliant_items": non_compliant_items,
            }

        cr_reports = data.get("change_request_reports", [])
        cr_reports.append({
            "report_id": f"rp_{uuid.uuid4().hex[:8]}",
            "project_id": project_id,
            "report_type": report_type,
            "content": report,
        })

        return json.dumps(report, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_change_report",
                "description": "Generate various reports for change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "report_type": {
                            "type": "string",
                            "description": "Type: summary, detailed, compliance",
                        },
                        "include_details": {
                            "type": "boolean",
                            "description": "Include detailed information in report",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class CreateRiskAssessment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        assessed_by = kwargs.get("assessed_by")
        risk_categories = kwargs.get("risk_categories", {})
        identified_risks = kwargs.get("identified_risks", [])
        mitigation_strategies = kwargs.get("mitigation_strategies", [])
        contingency_plans = kwargs.get("contingency_plans", {})
        rollback_procedure = kwargs.get("rollback_procedure")

        if not all([cr_id, assessed_by]):
            return json.dumps({"error": "cr_id and assessed_by are required"})

        change_requests = data.get("change_requests", [])
        risk_assessments = data.get("risk_assessments", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        if cr.get("requires_risk_assessment") or (
            cr.get("impact_assessment", {}).get("affects_critical_path")
        ):
            if not mitigation_strategies:
                return json.dumps(
                    {
                        "error": "RULE 5: Mitigation strategies are required for critical path changes"
                    }
                )
            if not contingency_plans:
                return json.dumps(
                    {
                        "error": "RULE 5: Contingency plans are required for critical path changes"
                    }
                )
            if not rollback_procedure:
                return json.dumps(
                    {
                        "error": "RULE 5: Rollback procedure is required for critical path changes"
                    }
                )

        risk_scores = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        total_score = sum(
            risk_scores.get(level, 0) for level in risk_categories.values()
        )
        avg_score = total_score / max(len(risk_categories), 1)

        overall_risk_level = (
            "critical"
            if avg_score >= 3.5
            else "high"
            if avg_score >= 2.5
            else "medium"
            if avg_score >= 1.5
            else "low"
        )

        requires_contingency_budget = (
            overall_risk_level in ["critical", "high"]
            or cr.get("priority") == "critical"
        )

        monitoring_frequency = (
            "continuous"
            if overall_risk_level == "critical"
            else "daily"
            if overall_risk_level == "high"
            else "weekly"
            if overall_risk_level == "medium"
            else "bi-weekly"
        )

        assessment_id = f"ra_{uuid.uuid4().hex[:8]}"

        risk_assessment = {
            "assessment_id": assessment_id,
            "cr_id": cr_id,
            "assessed_by": assessed_by,
            "assessment_date": datetime.now().isoformat(),
            "risk_categories": risk_categories,
            "overall_risk_level": overall_risk_level,
            "identified_risks": identified_risks,
            "mitigation_strategies": mitigation_strategies,
            "contingency_plans": contingency_plans,
            "rollback_procedure": rollback_procedure,
            "requires_contingency_budget": requires_contingency_budget,
            "monitoring_frequency": monitoring_frequency,
        }

        risk_assessments.append(risk_assessment)

        if cr.get("status") == "in_review":
            cr["risk_assessment_id"] = assessment_id
            cr["risk_level"] = overall_risk_level

        return json.dumps({"success": True, "risk_assessment": risk_assessment})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_risk_assessment",
                "description": "Create risk assessment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "assessed_by": {
                            "type": "string",
                            "description": "Risk assessor ID",
                        },
                        "risk_categories": {
                            "type": "object",
                            "description": "Risk levels by category (technical, schedule, resource, quality, stakeholder): low/medium/high/critical",
                        },
                        "identified_risks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of identified risks",
                        },
                        "mitigation_strategies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Risk mitigation strategies",
                        },
                        "contingency_plans": {
                            "type": "object",
                            "description": "Contingency plans mapping",
                        },
                        "rollback_procedure": {
                            "type": "string",
                            "description": "Rollback procedure if change fails",
                        },
                    },
                    "required": ["cr_id", "assessed_by"],
                },
            },
        }


class LinkChangeToMilestone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        milestone_id = kwargs.get("milestone_id")
        impact_type = kwargs.get("impact_type", "schedule")

        if not all([cr_id, milestone_id]):
            return json.dumps({"error": "cr_id and milestone_id are required"})

        change_requests = data.get("change_requests", [])
        milestones = data.get("milestones", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )

        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})
        if not milestone:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        if cr.get("project_id") != milestone.get("project_id"):
            return json.dumps(
                {"error": "Change request and milestone must be in the same project"}
            )

        if "linked_milestones" not in cr:
            cr["linked_milestones"] = []

        link_info = {
            "milestone_id": milestone_id,
            "milestone_name": milestone.get("milestone_name"),
            "impact_type": impact_type,
            "linked_date": datetime.now().isoformat(),
        }

        cr["linked_milestones"].append(link_info)

        if cr.get("status") == "approved" and cr.get("impact_assessment"):
            impact = cr["impact_assessment"]
            if impact_type == "schedule" and impact.get("timeline_impact_weeks", 0) > 0:

                milestone["change_impact_weeks"] = (
                    milestone.get("change_impact_weeks", 0)
                    + impact["timeline_impact_weeks"]
                )
                milestone["impacted_by_changes"] = milestone.get(
                    "impacted_by_changes", []
                )
                milestone["impacted_by_changes"].append(cr_id)

        return json.dumps(
            {
                "success": True,
                "link_created": {
                    "cr_id": cr_id,
                    "milestone_id": milestone_id,
                    "impact_type": impact_type,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_change_to_milestone",
                "description": "Link a change request to affected project milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "impact_type": {
                            "type": "string",
                            "description": "Type of impact: schedule, scope, resource",
                        },
                    },
                    "required": ["cr_id", "milestone_id"],
                },
            },
        }


class ApproveBaselineUpdate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        baseline_id = kwargs.get("baseline_id")
        approved_by = kwargs.get("approved_by")
        approval_notes = kwargs.get("approval_notes", "")

        if not all([baseline_id, approved_by]):
            return json.dumps({"error": "baseline_id and approved_by are required"})

        scope_baselines = data.get("scope_baselines", [])

        baseline = next(
            (b for b in scope_baselines if b.get("baseline_id") == baseline_id), None
        )
        if not baseline:
            return json.dumps({"error": f"Baseline '{baseline_id}' not found"})

        if baseline.get("status") != "draft":
            return json.dumps(
                {"error": f"Baseline is already {baseline.get('status')}"}
            )

        if not all(
            [
                baseline.get("deliverables"),
                baseline.get("acceptance_criteria"),
                baseline.get("success_metrics"),
            ]
        ):
            return json.dumps(
                {
                    "error": "RULE 2: Cannot approve incomplete baseline. Must include deliverables, acceptance criteria, and success metrics."
                }
            )

        project_id = baseline.get("project_id")
        existing_approved = next(
            (
                b
                for b in scope_baselines
                if b.get("project_id") == project_id
                and b.get("status") == "approved"
                and b.get("baseline_id") != baseline_id
            ),
            None,
        )

        if existing_approved:

            existing_approved["status"] = "superseded"
            existing_approved["superseded_by"] = baseline_id
            existing_approved["superseded_date"] = datetime.now().isoformat()

        baseline["status"] = "approved"
        baseline["approved_by"] = approved_by
        baseline["approved_date"] = datetime.now().isoformat()
        baseline["approval_notes"] = approval_notes

        if "change_history" not in baseline:
            baseline["change_history"] = []

        baseline["change_history"].append(
            {
                "action": "approved",
                "performed_by": approved_by,
                "date": datetime.now().isoformat(),
                "notes": approval_notes,
            }
        )

        change_requests = data.get("change_requests", [])
        for cr in change_requests:
            if cr.get("project_id") == project_id and cr.get("status") in [
                "completed",
                "approved",
            ]:
                cr["included_in_baseline"] = baseline.get("version")

        return json.dumps(
            {
                "success": True,
                "baseline": {
                    "baseline_id": baseline_id,
                    "version": baseline.get("version"),
                    "status": "approved",
                    "superseded_baseline": existing_approved.get("baseline_id")
                    if existing_approved
                    else None,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_baseline_update",
                "description": "Approve a new scope baseline, superseding the previous one",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "baseline_id": {
                            "type": "string",
                            "description": "Baseline ID to approve",
                        },
                        "approved_by": {"type": "string", "description": "Approver ID"},
                        "approval_notes": {
                            "type": "string",
                            "description": "Approval notes",
                        },
                    },
                    "required": ["baseline_id", "approved_by"],
                },
            },
        }


class EscalateChangeRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        escalate_to_level = kwargs.get("escalate_to_level")
        escalated_by = kwargs.get("escalated_by")

        if not all([cr_id, escalate_to_level, escalated_by]):
            return json.dumps(
                {
                    "error": "cr_id, escalate_to_level, and escalated_by are required"
                }
            )

        change_requests = data.get("change_requests", [])
        approval_workflows = data.get("approval_workflows", [])
        change_history = data.get("change_history", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        old_priority = cr.get("priority")
        if escalate_to_level in ["executive", "critical"]:
            cr["priority"] = "critical"
        elif old_priority != "critical":
            cr["priority"] = "high"

        cr["escalated"] = True
        cr["escalation_date"] = datetime.now().isoformat()
        cr["escalated_to"] = escalate_to_level

        workflow = next(
            (
                w
                for w in approval_workflows
                if w.get("cr_id") == cr_id and w.get("status") == "active"
            ),
            None,
        )
        if workflow:

            if escalate_to_level == "executive":
                new_step = {
                    "step_number": len(workflow.get("steps", [])) + 1,
                    "approval_level": "executive_sponsor",
                    "approver_id": None,
                    "status": "pending",
                    "required": True,
                    "can_delegate": False,
                    "escalated": True,
                }
                workflow["steps"].append(new_step)

                if "executive_sponsor" not in cr.get("approvals_required", []):
                    cr["approvals_required"].append("executive_sponsor")

        history_entry = {
            "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
            "cr_id": cr_id,
            "action": "escalated",
            "performed_by": escalated_by,
            "escalation_level": escalate_to_level,
            "priority_change": f"{old_priority} -> {cr.get('priority')}",
            "timestamp": datetime.now().isoformat(),
        }
        change_history.append(history_entry)

        return json.dumps(
            {
                "success": True,
                "escalation": {
                    "cr_id": cr_id,
                    "escalated_to": escalate_to_level,
                    "new_priority": cr.get("priority"),
                    "workflow_updated": workflow is not None,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_change_request",
                "description": "Escalate a change request to higher management",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "escalate_to_level": {
                            "type": "string",
                            "description": "Level to escalate to: senior_management, executive, critical",
                        },
                        "escalated_by": {
                            "type": "string",
                            "description": "Person escalating the request",
                        },
                    },
                    "required": [
                        "cr_id",
                        "escalate_to_level",
                        "escalated_by",
                    ],
                },
            },
        }


class MergeChangeRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        primary_cr_id = kwargs.get("primary_cr_id")
        secondary_cr_ids = kwargs.get("secondary_cr_ids", [])
        merged_by = kwargs.get("merged_by")

        if not all([primary_cr_id, secondary_cr_ids, merged_by]):
            return json.dumps(
                {
                    "error": "primary_cr_id, secondary_cr_ids, and merged_by are required"
                }
            )

        change_requests = data.get("change_requests", [])
        change_history = data.get("change_history", [])

        primary_cr = next(
            (c for c in change_requests if c.get("cr_id") == primary_cr_id), None
        )
        if not primary_cr:
            return json.dumps(
                {"error": f"Primary change request '{primary_cr_id}' not found"}
            )

        project_id = primary_cr.get("project_id")
        merged_deliverables = set(primary_cr.get("affected_deliverables", []))
        merged_justifications = [primary_cr.get("business_justification")]

        for cr_id in secondary_cr_ids:
            secondary_cr = next(
                (c for c in change_requests if c.get("cr_id") == cr_id), None
            )
            if not secondary_cr:
                return json.dumps(
                    {"error": f"Secondary change request '{cr_id}' not found"}
                )

            if secondary_cr.get("project_id") != project_id:
                return json.dumps(
                    {"error": "All change requests must be for the same project"}
                )

            merged_deliverables.update(secondary_cr.get("affected_deliverables", []))
            merged_justifications.append(secondary_cr.get("business_justification"))

            secondary_cr["status"] = "merged"
            secondary_cr["merged_into"] = primary_cr_id
            secondary_cr["merge_date"] = datetime.now().isoformat()

            history_entry = {
                "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
                "cr_id": cr_id,
                "action": "merged",
                "merged_into": primary_cr_id,
                "performed_by": merged_by,
                "timestamp": datetime.now().isoformat(),
            }
            change_history.append(history_entry)

        primary_cr["affected_deliverables"] = list(merged_deliverables)
        primary_cr[
            "business_justification"
        ] = f"{primary_cr.get('business_justification')}. MERGED: {'; '.join(merged_justifications[1:])}"
        primary_cr["merged_from"] = secondary_cr_ids
        primary_cr["merge_date"] = datetime.now().isoformat()

        if len(secondary_cr_ids) >= 2 and primary_cr.get("priority") == "medium":
            primary_cr["priority"] = "high"

        return json.dumps(
            {
                "success": True,
                "merge_result": {
                    "primary_cr": primary_cr_id,
                    "merged_crs": secondary_cr_ids,
                    "total_affected_deliverables": len(merged_deliverables),
                    "new_priority": primary_cr.get("priority"),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_change_requests",
                "description": "Merge duplicate or related change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "primary_cr_id": {
                            "type": "string",
                            "description": "Primary CR to merge into",
                        },
                        "secondary_cr_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs to merge into primary",
                        },
                        "merged_by": {
                            "type": "string",
                            "description": "Person performing the merge",
                        },
                    },
                    "required": [
                        "primary_cr_id",
                        "secondary_cr_ids",
                        "merged_by",
                    ],
                },
            },
        }


class ArchiveChanges(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        archive_before_date = kwargs.get("archive_before_date")
        archived_by = kwargs.get("archived_by")

        if not all([project_id, archived_by]):
            return json.dumps({"error": "project_id and archived_by are required"})

        change_requests = data.get("change_requests", [])

        if "archived_changes" not in data:
            data["archived_changes"] = []
        archived_changes = data["archived_changes"]

        if not archive_before_date:

            archive_before_date = (datetime.now() - timedelta(days=90)).isoformat()

        to_archive = []
        for cr in change_requests:
            if (
                cr.get("project_id") == project_id
                and cr.get("status") in ["completed", "cancelled", "rejected"]
                and cr.get("updated_date", cr.get("created_date", ""))
                < archive_before_date
            ):

                if cr.get("status") == "completed" or cr.get("status") != "approved":
                    to_archive.append(cr)

        archived_count = 0
        for cr in to_archive:

            archive_entry = cr.copy()
            archive_entry["archived_date"] = datetime.now().isoformat()
            archive_entry["archived_by"] = archived_by

            archived_changes.append(archive_entry)

            cr["archived"] = True
            cr["archive_date"] = datetime.now().isoformat()

            archived_count += 1

        return json.dumps(
            {
                "success": True,
                "archive_summary": {
                    "project_id": project_id,
                    "archived_count": archived_count,
                    "archive_date": datetime.now().isoformat(),
                    "criteria": {
                        "before_date": archive_before_date,
                        "statuses": ["completed", "cancelled", "rejected"],
                    },
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archive_changes",
                "description": "Archive completed, cancelled, or rejected change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "archive_before_date": {
                            "type": "string",
                            "description": "Archive changes before this date (ISO format)",
                        },
                        "archived_by": {
                            "type": "string",
                            "description": "Person performing the archive",
                        },
                    },
                    "required": ["project_id", "archived_by"],
                },
            },
        }


class CreateChangeTemplate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        template_name = kwargs.get("template_name")
        template_type = kwargs.get("template_type")
        standard_fields = kwargs.get("standard_fields", {})
        required_approvals = kwargs.get("required_approvals", [])
        risk_threshold = kwargs.get("risk_threshold", "medium")
        created_by = kwargs.get("created_by")

        if not all([template_name, template_type, created_by]):
            return json.dumps(
                {"error": "template_name, template_type, and created_by are required"}
            )

        if "change_templates" not in data:
            data["change_templates"] = []
        change_templates = data["change_templates"]

        existing = next(
            (t for t in change_templates if t.get("template_name") == template_name),
            None,
        )
        if existing:
            return json.dumps({"error": f"Template '{template_name}' already exists"})

        template_id = f"ct_{uuid.uuid4().hex[:8]}"

        if template_type == "standard_enhancement":
            default_fields = {
                "change_type": "scope_addition",
                "priority": "medium",
                "typical_duration_weeks": 4,
                "typical_resources": 2,
            }
        elif template_type == "emergency_fix":
            default_fields = {
                "change_type": "requirement_change",
                "priority": "critical",
                "typical_duration_weeks": 1,
                "requires_emergency_approval": True,
            }
        elif template_type == "scope_reduction":
            default_fields = {
                "change_type": "scope_reduction",
                "priority": "high",
                "typical_duration_weeks": 2,
            }
        else:
            default_fields = {}

        template_fields = {**default_fields, **standard_fields}

        new_template = {
            "template_id": template_id,
            "template_name": template_name,
            "template_type": template_type,
            "standard_fields": template_fields,
            "required_approvals": required_approvals,
            "risk_threshold": risk_threshold,
            "created_by": created_by,
            "created_date": datetime.now().isoformat(),
            "usage_count": 0,
            "active": True,
        }

        change_templates.append(new_template)

        return json.dumps({"success": True, "template": new_template})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_change_template",
                "description": "Create a template for common change request types",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_name": {
                            "type": "string",
                            "description": "Template name",
                        },
                        "template_type": {
                            "type": "string",
                            "description": "Type: standard_enhancement, emergency_fix, scope_reduction, requirement_update",
                        },
                        "standard_fields": {
                            "type": "object",
                            "description": "Pre-filled fields for this template",
                        },
                        "required_approvals": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Standard approval requirements",
                        },
                        "risk_threshold": {
                            "type": "string",
                            "description": "Default risk level",
                        },
                        "created_by": {"type": "string", "description": "Creator ID"},
                    },
                    "required": ["template_name", "template_type", "created_by"],
                },
            },
        }


class BulkUpdateChangeStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_ids = kwargs.get("cr_ids", [])
        new_status = kwargs.get("new_status")
        updated_by = kwargs.get("updated_by")

        if not all([cr_ids, new_status, updated_by]):
            return json.dumps(
                {"error": "cr_ids, new_status, and updated_by are required"}
            )

        change_requests = data.get("change_requests", [])
        change_history = data.get("change_history", [])

        results = {"successful": [], "failed": []}

        for cr_id in cr_ids:
            cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
            if not cr:
                results["failed"].append(
                    {"cr_id": cr_id}
                )
                continue

            old_status = cr.get("status")

            valid_bulk_transitions = {
                "draft": ["cancelled"],
                "in_review": ["cancelled"],
                "pending_approval": ["on_hold", "cancelled"],
                "on_hold": ["cancelled"],
                "approved": ["in_implementation", "completed"],
                "in_implementation": ["completed"],
            }

            if new_status not in valid_bulk_transitions.get(old_status, []):
                results["failed"].append(
                    {
                        "cr_id": cr_id,
                    }
                )
                continue

            cr["status"] = new_status
            cr["updated_date"] = datetime.now().isoformat()
            cr["bulk_update"] = True

            history_entry = {
                "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
                "cr_id": cr_id,
                "action": "bulk_status_change",
                "from_status": old_status,
                "to_status": new_status,
                "performed_by": updated_by,
                "timestamp": datetime.now().isoformat(),
            }
            change_history.append(history_entry)

            results["successful"].append(
                {"cr_id": cr_id, "old_status": old_status, "new_status": new_status}
            )

        return json.dumps(
            {
                "success": len(results["successful"]) > 0,
                "summary": {
                    "total_requested": len(cr_ids),
                    "successful": len(results["successful"]),
                    "failed": len(results["failed"]),
                },
                "results": results,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_change_status",
                "description": "Update status for multiple change requests at once",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of change request IDs",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to apply",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Person performing the update",
                        },
                    },
                    "required": ["cr_ids", "new_status", "updated_by"],
                },
            },
        }


class CalculateChangeROI(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        expected_benefits = kwargs.get("expected_benefits", {})
        benefit_timeframe_months = kwargs.get("benefit_timeframe_months", 12)

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        impact = cr.get("impact_assessment", {})
        total_cost = impact.get("budget_impact", 0)

        for resource in impact.get("resource_requirements", []):
            hours = resource.get("hours_per_week", 0) * resource.get(
                "duration_weeks", 0
            )

            total_cost += hours * 150

        total_benefits = 0
        benefit_breakdown = {}

        for benefit_type, value in expected_benefits.items():
            if benefit_type == "cost_savings_monthly":
                total_value = value * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown[benefit_type] = total_value
            elif benefit_type == "productivity_gain_percentage":

                monthly_cost = 10 * 150 * 160
                monthly_savings = monthly_cost * (value / 100)
                total_value = monthly_savings * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown["productivity_savings"] = total_value
            elif benefit_type == "revenue_increase_monthly":
                total_value = value * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown[benefit_type] = total_value
            else:

                total_benefits += value
                benefit_breakdown[benefit_type] = value

        roi_percentage = (
            ((total_benefits - total_cost) / total_cost * 100) if total_cost > 0 else 0
        )
        payback_period_months = (
            (total_cost / (total_benefits / benefit_timeframe_months))
            if total_benefits > 0
            else None
        )

        if roi_percentage > 50:
            recommendation = "Strongly recommended - High ROI"
        elif roi_percentage > 20:
            recommendation = "Recommended - Positive ROI"
        elif roi_percentage > 0:
            recommendation = "Consider with caution - Low ROI"
        else:
            recommendation = "Not recommended - Negative ROI"

        return json.dumps(
            {
                "cr_id": cr_id,
                "financial_analysis": {
                    "total_cost": total_cost,
                    "total_benefits": total_benefits,
                    "benefit_breakdown": benefit_breakdown,
                    "roi_percentage": round(roi_percentage, 1),
                    "payback_period_months": round(payback_period_months, 1)
                    if payback_period_months
                    else None,
                    "benefit_timeframe_months": benefit_timeframe_months,
                },
                "recommendation": recommendation,
                "assumptions": {
                    "hourly_rate": "$150/hour",
                    "working_hours_per_month": 160,
                },
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_change_roi",
                "description": "Calculate return on investment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "expected_benefits": {
                            "type": "object",
                            "description": "Expected benefits mapping (e.g., cost_savings_monthly, productivity_gain_percentage, revenue_increase_monthly)",
                        },
                        "benefit_timeframe_months": {
                            "type": "number",
                            "description": "Timeframe for benefits calculation in months",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }


class TrackChangeDependencies(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        depends_on = kwargs.get("depends_on", [])
        blocks = kwargs.get("blocks", [])

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        for dep_id in depends_on:
            if not any(c.get("cr_id") == dep_id for c in change_requests):
                return json.dumps({"error": f"Dependency CR '{dep_id}' not found"})

        for block_id in blocks:
            if not any(c.get("cr_id") == block_id for c in change_requests):
                return json.dumps({"error": f"Blocked CR '{block_id}' not found"})

        def has_circular_dependency(start_id, check_id, visited=None):
            if visited is None:
                visited = set()
            if start_id in visited:
                return True
            visited.add(start_id)

            cr_to_check = next(
                (c for c in change_requests if c.get("cr_id") == start_id), None
            )
            if not cr_to_check:
                return False

            for dep_id in cr_to_check.get("depends_on", []):
                if dep_id == check_id:
                    return True
                if has_circular_dependency(dep_id, check_id, visited):
                    return True
            return False

        for dep_id in depends_on:
            if has_circular_dependency(dep_id, cr_id):
                return json.dumps(
                    {
                        "error": f"Adding dependency on '{dep_id}' would create a circular dependency"
                    }
                )

        if "depends_on" not in cr:
            cr["depends_on"] = []
        if "blocks" not in cr:
            cr["blocks"] = []

        cr["depends_on"].extend([d for d in depends_on if d not in cr["depends_on"]])
        cr["blocks"].extend([b for b in blocks if b not in cr["blocks"]])

        for block_id in blocks:
            blocked_cr = next(
                (c for c in change_requests if c.get("cr_id") == block_id), None
            )
            if blocked_cr:
                if "blocked_by" not in blocked_cr:
                    blocked_cr["blocked_by"] = []
                if cr_id not in blocked_cr["blocked_by"]:
                    blocked_cr["blocked_by"].append(cr_id)

                if (
                    blocked_cr.get("status") == "pending_approval"
                    and cr.get("status") != "completed"
                ):
                    blocked_cr["dependency_hold"] = True

        can_proceed = True
        blocking_crs = []
        for dep_id in cr.get("depends_on", []):
            dep_cr = next(
                (c for c in change_requests if c.get("cr_id") == dep_id), None
            )
            if dep_cr and dep_cr.get("status") not in [
                "completed",
                "approved",
                "in_implementation",
            ]:
                can_proceed = False
                blocking_crs.append({"cr_id": dep_id, "status": dep_cr.get("status")})

        return json.dumps(
            {
                "success": True,
                "dependencies": {
                    "cr_id": cr_id,
                    "depends_on": cr.get("depends_on", []),
                    "blocks": cr.get("blocks", []),
                    "can_proceed": can_proceed,
                    "blocking_crs": blocking_crs,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "track_change_dependencies",
                "description": "Track dependencies between change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "depends_on": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs this change depends on",
                        },
                        "blocks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs blocked by this change",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }


class GenerateAuditTrail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        include_approvals = kwargs.get("include_approvals", True)
        include_artifacts = kwargs.get("include_artifacts", True)

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])
        change_history = data.get("change_history", [])
        change_approvals = data.get("change_approvals", [])
        artifact_updates = data.get("artifact_updates", [])
        risk_assessments = data.get("risk_assessments", [])
        emergency_logs = data.get("emergency_logs", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        audit_trail = {
            "cr_id": cr_id,
            "title": cr.get("title"),
            "current_status": cr.get("status"),
            "created_date": cr.get("created_date"),
            "timeline": [],
        }

        audit_trail["timeline"].append(
            {
                "timestamp": cr.get("created_date"),
                "event_type": "created",
                "description": f"Change request created by {cr.get('requester_id')}",
                "actor": cr.get("requester_id"),
            }
        )

        cr_history = [h for h in change_history if h.get("cr_id") == cr_id]
        for event in sorted(cr_history, key=lambda x: x.get("timestamp", "")):
            audit_trail["timeline"].append(
                {
                    "timestamp": event.get("timestamp"),
                    "event_type": event.get("action"),
                    "description": f"{event.get('action')}: {event.get('from_status', '')} -> {event.get('to_status', '')}",
                    "actor": event.get("performed_by"),
                    "details": event,
                }
            )

        if impact := cr.get("impact_assessment"):
            audit_trail["timeline"].append(
                {
                    "timestamp": impact.get("assessment_date"),
                    "event_type": "impact_assessed",
                    "description": f"Impact assessment completed - Risk: {impact.get('overall_risk')}",
                    "actor": impact.get("assessed_by"),
                    "details": {
                        "budget_impact": impact.get("budget_impact"),
                        "timeline_impact": impact.get("timeline_impact_weeks"),
                        "risk": impact.get("overall_risk"),
                    },
                }
            )

        risk_assessment = next(
            (r for r in risk_assessments if r.get("cr_id") == cr_id), None
        )
        if risk_assessment:
            audit_trail["timeline"].append(
                {
                    "timestamp": risk_assessment.get("assessment_date"),
                    "event_type": "risk_assessed",
                    "description": f"Risk assessment completed - Level: {risk_assessment.get('overall_risk_level')}",
                    "actor": risk_assessment.get("assessed_by"),
                }
            )

        if cr.get("requires_emergency_approval"):
            log = next((e for e in emergency_logs if e.get("cr_id") == cr_id), None)
            if log:
                audit_trail["timeline"].append(
                    {
                        "timestamp": log.get("timestamp"),
                        "event_type": "emergency_approval",
                        "description": f"Emergency approval granted by {log.get('authorized_by')}",
                        "actor": log.get("authorized_by"),
                        "details": {
                            "type": log.get("emergency_type"),
                            "documentation_deadline": log.get("documentation_deadline"),
                            "retroactive_deadline": log.get(
                                "retroactive_approval_deadline"
                            ),
                        },
                    }
                )

        if include_approvals:
            cr_approvals = [a for a in change_approvals if a.get("cr_id") == cr_id]
            for approval in sorted(
                cr_approvals, key=lambda x: x.get("action_date", "")
            ):
                audit_trail["timeline"].append(
                    {
                        "timestamp": approval.get("action_date"),
                        "event_type": "approval_decision",
                        "description": f"{approval.get('approver_role')} {approval.get('decision')}",
                        "actor": approval.get("approver_id"),
                        "details": {
                            "decision": approval.get("decision"),
                            "comments": approval.get("comments"),
                        },
                    }
                )

        if include_artifacts:
            cr_artifacts = [a for a in artifact_updates if a.get("cr_id") == cr_id]
            for artifact in sorted(
                cr_artifacts, key=lambda x: x.get("update_date", "")
            ):
                audit_trail["timeline"].append(
                    {
                        "timestamp": artifact.get("update_date"),
                        "event_type": "artifact_updated",
                        "description": f"{artifact.get('artifact_type')} updated",
                        "actor": artifact.get("updated_by"),
                        "details": {
                            "artifact": artifact.get("artifact_type"),
                            "version": f"{artifact.get('version_before')} -> {artifact.get('version_after')}",
                        },
                    }
                )

        audit_trail["timeline"].sort(key=lambda x: x.get("timestamp", ""))

        audit_trail["summary"] = {
            "total_events": len(audit_trail["timeline"]),
            "days_in_process": None,
            "approval_time_days": None,
            "compliance_flags": [],
        }

        if cr.get("status") == "rejected" and cr.get("can_resubmit_after"):
            if datetime.now().isoformat() < cr.get("can_resubmit_after"):

                audit_trail["summary"]["compliance_flags"].append(
                    f"In cooling period until {cr.get('can_resubmit_after')}"
                )

        if cr.get("requires_emergency_approval"):
            log = next((e for e in emergency_logs if e.get("cr_id") == cr_id), None)
            if log and log.get("retroactive_status") == "pending":
                deadline = log.get("retroactive_approval_deadline", "")
                if deadline and datetime.now().isoformat() > deadline:
                    audit_trail["summary"]["compliance_flags"].append(
                        "OVERDUE: Emergency retroactive approval deadline exceeded"
                    )

        if audit_trail["timeline"]:

            audit_trail["summary"]["days_in_process"] = len(audit_trail["timeline"])

            if cr.get("status") == "approved" and cr.get("approval_date"):

                audit_trail["summary"]["approval_time_days"] = 7

        return json.dumps(audit_trail, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_audit_trail",
                "description": "Generate complete audit trail for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "include_approvals": {
                            "type": "boolean",
                            "description": "Include approval details",
                        },
                        "include_artifacts": {
                            "type": "boolean",
                            "description": "Include artifact update details",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }


TOOLS = [
    CreateChangeRequest(),
    PerformImpactAssessment(),
    UpdateChangeRequestStatus(),
    CreateApprovalWorkflow(),
    CheckWorkflowExistsForChangeRequest(),
    RecordApprovalDecision(),
    SearchChangeRequests(),
    TrackArtifactUpdates(),
    CreateScopeBaseline(),
    CompareAgainstBaseline(),
    ScheduleChangeReview(),
    ProcessEmergencyChange(),
    CalculateCumulativeImpact(),
    GenerateChangeReport(),
    CreateRiskAssessment(),
    LinkChangeToMilestone(),
    ApproveBaselineUpdate(),
    CheckChangeConflicts(),
    EscalateChangeRequest(),
    MergeChangeRequests(),
    ArchiveChanges(),
    ValidateChangeCompliance(),
    CreateChangeTemplate(),
    BulkUpdateChangeStatus(),
    CalculateChangeROI(),
    TrackChangeDependencies(),
    GenerateAuditTrail(),
    RecordRetroactiveApproval(),
    SaveChangeRequestsConflicts()
]
