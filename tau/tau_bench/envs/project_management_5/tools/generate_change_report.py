from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

class GenerateChangeReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        report_type: str = "summary",
        include_details: bool = False
    ) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        change_approvals = data.get("change_approvals", [])
        projects = data.get("projects", [])
        emergency_logs = data.get("emergency_logs", [])
        report = {}

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project '{project_id}' not found"}
            out = json.dumps(payload)
            return out

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
                    if (
                        conflict.get("conflict_id")
                        and conflict.get("conflict_id") not in project_conflicts
                    ):
                        project_conflicts[conflict.get("conflict_id")] = {
                            "crs_involved": [
                                cr.get("cr_id"),
                                conflict.get("conflicting_cr_id"),
                            ],
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
                    if (
                        conflict.get("conflict_id")
                        and conflict.get("conflict_id") not in project_conflicts
                    ):
                        project_conflicts[conflict.get("conflict_id")] = {
                            "crs_involved": [
                                cr.get("cr_id"),
                                conflict.get("conflicting_cr_id"),
                            ],
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
                        pass
        
        out = json.dumps(report)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateChangeReport",
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
