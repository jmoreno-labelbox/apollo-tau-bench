from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ValidateChangeCompliance(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str,
        compliance_checklist: list[str] = None
    ) -> str:
        if not cr_id:
            payload = {"error": "cr_id is required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        emergency_logs = data.get("emergency_logs", [])
        risk_assessments = data.get("risk_assessments", [])
        scope_baselines = data.get("scope_baselines", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

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
        payload = {
                "cr_id": cr_id,
                "compliance_status": compliance_status,
                "violations": violations,
                "warnings": warnings,
                "checks_performed": checks_to_perform,
                "recommendation": (
                    "Address violations before proceeding"
                    if violations
                    else "Proceed with caution" if warnings else "Fully compliant"
                ),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateChangeCompliance",
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
