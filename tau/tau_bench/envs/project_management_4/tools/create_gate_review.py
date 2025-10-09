from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateGateReview(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str,
        review_date: str,
        criteria_results: dict[str, str] = {},
        reviewers: list[str] = [],
        conditional_pass: bool = False,
        review_notes: str = "",
        action_items: list[str] = []
    ) -> str:
        if not all([milestone_id, review_date, criteria_results, reviewers]):
            payload = {
                "error": "milestone_id, review_date, criteria_results, and reviewers are required"
            }
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        gate_reviews = data.get("gate_reviews", [])

        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if milestone.get("milestone_type") not in ["phase_gate", "major"]:
            payload = {"error": "Gate reviews are only for phase_gate or major milestones"}
            out = json.dumps(payload)
            return out

        start_date = datetime.fromisoformat(
            milestone.get("start_date").replace("Z", "+00:00")
        )
        review_dt = datetime.fromisoformat(review_date.replace("Z", "+00:00"))

        if not milestone.get("gate_criteria") and review_dt >= start_date:
            payload = {"error": "Gate criteria must be defined before milestone start date"}
            out = json.dumps(payload)
            return out

        failed_criteria = [k for k, v in criteria_results.items() if v == "fail"]
        overall_decision = "fail" if failed_criteria else "pass"

        if failed_criteria and conditional_pass:
            overall_decision = "conditional_pass"

        review_id = f"gate_{uuid.uuid4().hex[:8]}"

        previous_reviews = [
            r for r in gate_reviews if r.get("milestone_id") == milestone_id
        ]
        consecutive_failures = 0

        if previous_reviews and overall_decision == "fail":
            previous_reviews.sort(key=lambda x: x.get("created_date"), reverse=True)

            for review in previous_reviews:
                if review.get("overall_decision") == "fail":
                    consecutive_failures += 1
                else:
                    break

        new_review = {
            "review_id": review_id,
            "milestone_id": milestone_id,
            "review_date": review_date,
            "criteria_results": criteria_results,
            "overall_decision": overall_decision,
            "review_notes": review_notes,
            "reviewers": reviewers,
            "action_items": action_items,
            "consecutive_failures": consecutive_failures
            + (1 if overall_decision == "fail" else 0),
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        gate_reviews.append(new_review)

        if overall_decision == "pass":
            milestone["gate_passed"] = True
        elif overall_decision == "fail":
            milestone["health"] = "red"
            milestone["status"] = "delayed"

            current_target = datetime.fromisoformat(
                milestone.get("target_date").replace("Z", "+00:00")
            )
            new_target = current_target + timedelta(days=10)
            milestone["target_date"] = new_target.isoformat()
            milestone["remediation_period"] = True

            if new_review["consecutive_failures"] >= 3:
                escalations = data.get("escalations", [])
                escalation_id = f"esc_{uuid.uuid4().hex[:8]}"
                escalations.append(
                    {
                        "escalation_id": escalation_id,
                        "milestone_id": milestone_id,
                        "escalation_level": "steering_committee",
                        "created_date": datetime.now(timezone.utc).isoformat(),
                    }
                )

                new_review["escalated_to_steering"] = True
        payload = {
            "success": True,
            "gate_review": new_review,
            "decision": overall_decision,
            "failed_criteria": failed_criteria,
            "consecutive_failures": new_review["consecutive_failures"],
            "escalated": new_review.get("escalated_to_steering", False),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGateReview",
                "description": "Create a gate review for a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "review_date": {
                            "type": "string",
                            "description": "Review date (ISO format)",
                        },
                        "criteria_results": {
                            "type": "object",
                            "description": "Dictionary of criteria names to results (pass/fail)",
                        },
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of reviewer employee IDs",
                        },
                        "review_notes": {
                            "type": "string",
                            "description": "Review notes",
                        },
                        "action_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Action items from the review",
                        },
                        "conditional_pass": {
                            "type": "boolean",
                            "description": "Allow conditional pass despite failures",
                        },
                    },
                    "required": [
                        "milestone_id",
                        "review_date",
                        "criteria_results",
                        "reviewers",
                    ],
                },
            },
        }
