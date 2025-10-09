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

class CreateChangeRequest(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        title: str,
        description: str,
        requester_id: str,
        project_id: str,
        change_type: str,
        business_justification: str,
        priority: str = "medium",
        affected_deliverables: list = [],
        cr_id: str = None
    ) -> str:
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
            payload = {
                "error": "title, description, requester_id, project_id, change_type, and business_justification are required"
            }
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        projects = data.get("projects", [])
        scope_baselines = data.get("scope_baselines", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project '{project_id}' not found"}
            out = json.dumps(payload)
            return out

        project_baseline = next(
            (
                b
                for b in scope_baselines
                if b.get("project_id") == project_id and b.get("status") == "approved"
            ),
            None,
        )
        if not project_baseline:
            payload = {
                "error": "Cannot create change request: No approved scope baseline exists for this project. A baseline must be formally established and approved first."
            }
            out = json.dumps(payload)
            return out

        if not all(
            [
                project_baseline.get("deliverables"),
                project_baseline.get("acceptance_criteria"),
                project_baseline.get("metrics"),
            ]
        ):
            payload = {
                "error": "Cannot create change request: Existing baseline is incomplete. It must include deliverables, acceptance criteria, and success metrics."
            }
            out = json.dumps(payload)
            return out

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
                payload = {
                    "error": f"Cannot create change request: Deliverables {list(overlapping_deliverables)} are already affected by active change request '{active_cr.get('cr_id')}'. Multiple change requests affecting the same deliverable must be consolidated.",
                    "suggestion": "Please merge with existing change request or wait for it to complete.",
                }
                out = json.dumps(payload)
                return out

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
                if can_resubmit_after and datetime.now().isoformat() < can_resubmit_after:
                    days_remaining = (
                        datetime.fromisoformat(can_resubmit_after) - datetime.now()
                    ).days
                    payload = {
                        "error": f"Cannot create change request: This appears to be a resubmission of rejected CR '{rejected_cr.get('cr_id')}'. Rejected change requests have a 30-day cooling period.",
                        "days_remaining": days_remaining,
                        "can_resubmit_after": can_resubmit_after,
                        "requirement": "Resubmitted requests must include new justification addressing original rejection reasons and demonstrate changed circumstances.",
                    }
                    out = json.dumps(payload)
                    return out

                if (
                    rejected_cr.get("rejection_reason")
                    and rejected_cr.get("rejection_reason", "").lower()
                    not in business_justification.lower()
                ):
                    payload = {
                        "error": "Resubmission detected: Please address the original rejection reason in your business justification.",
                        "original_rejection_reason": rejected_cr.get("rejection_reason"),
                    }
                    out = json.dumps(payload)
                    return out

        cr_id = cr_id or f"cr_{uuid.uuid4().hex[:8]}"

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
        payload = {"success": True, "change_request": new_cr}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateChangeRequest",
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
