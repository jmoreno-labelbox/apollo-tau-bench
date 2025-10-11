# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApproveBaselineUpdate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], approved_by, baseline_id, approval_notes = "") -> str:

        if not all([baseline_id, approved_by]):
            return json.dumps({"error": "baseline_id and approved_by are required"})

        scope_baselines = list(data.get("scope_baselines", {}).values())

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

        change_requests = list(data.get("change_requests", {}).values())
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
