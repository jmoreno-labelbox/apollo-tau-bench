from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApproveBaselineUpdate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], baseline_id: str = None, approved_by: str = None, approval_notes: str = "") -> str:
        if not all([baseline_id, approved_by]):
            payload = {"error": "baseline_id and approved_by are required"}
            out = json.dumps(payload)
            return out

        scope_baselines = data.get("scope_baselines", {}).values()

        baseline = next(
            (b for b in scope_baselines.values() if b.get("baseline_id") == baseline_id), None
        )
        if not baseline:
            payload = {"error": f"Baseline '{baseline_id}' not found"}
            out = json.dumps(payload)
            return out

        if baseline.get("status") != "draft":
            payload = {"error": f"Baseline is already {baseline.get('status')}"}
            out = json.dumps(payload)
            return out

        if not all(
            [
                baseline.get("deliverables"),
                baseline.get("acceptance_criteria"),
                baseline.get("success_metrics"),
            ]
        ):
            payload = {
                "error": "RULE 2: Cannot approve incomplete baseline. Must include deliverables, acceptance criteria, and success metrics."
            }
            out = json.dumps(payload)
            return out

        project_id = baseline.get("project_id")
        existing_approved = next(
            (
                b
                for b in scope_baselines.values() if b.get("project_id") == project_id
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

        change_requests = data.get("change_requests", {}).values()
        for cr in change_requests.values():
            if cr.get("project_id") == project_id and cr.get("status") in [
                "completed",
                "approved",
            ]:
                cr["included_in_baseline"] = baseline.get("version")
        payload = {
            "success": True,
            "baseline": {
                "baseline_id": baseline_id,
                "version": baseline.get("version"),
                "status": "approved",
                "superseded_baseline": (
                    existing_approved.get("baseline_id")
                    if existing_approved
                    else None
                ),
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveBaselineUpdate",
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
