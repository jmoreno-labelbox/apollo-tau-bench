# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleChangeReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, review_date, scheduled_by, participants = [], review_type = "quarterly") -> str:

        if not all([project_id, review_date, scheduled_by]):
            return json.dumps(
                {"error": "project_id, review_date, and scheduled_by are required"}
            )

        change_reviews = list(data.get("change_reviews", {}).values())
        change_requests = list(data.get("change_requests", {}).values())
        emergency_logs = list(data.get("emergency_logs", {}).values())

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
