# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
