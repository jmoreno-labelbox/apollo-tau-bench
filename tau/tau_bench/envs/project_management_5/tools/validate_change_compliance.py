# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class CheckChangeConflicts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, compare_to_cr_id) -> str:

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

class ValidateChangeCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, compliance_checklist = []) -> str:

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = list(data.get("change_requests", {}).values())
        emergency_logs = list(data.get("emergency_logs", {}).values())
        risk_assessments = list(data.get("risk_assessments", {}).values())
        scope_baselines = list(data.get("scope_baselines", {}).values())

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
                risk_assessments = list(data.get("risk_assessments", {}).values())
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