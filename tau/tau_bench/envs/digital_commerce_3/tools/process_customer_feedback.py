from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProcessCustomerFeedback(Tool):
    """Handle and classify customer feedback for enhancement of quality."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, feedback_text: Any, rating: Any = None
    ) -> str:
        contact_id = _idstr(contact_id)
        feedback_text = f"{feedback_text}"
        rating = int(rating) if rating is not None else None

        if not contact_id or not feedback_text:
            return _error("contact_id and feedback_text are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        feedback_entries = data.setdefault("customer_feedback", [])
        feedback_id = f"FB_{len(feedback_entries) + 1:04d}"

        feedback = {
            "feedback_id": feedback_id,
            "contact_id": contact_id,
            "feedback_text": feedback_text,
            "rating": rating,
            "sentiment": "positive",
            "submitted_at": FIXED_NOW,
            "status": "new",
        }
        feedback_entries.append(feedback)

        _append_audit(
            data, "feedback_processed", feedback_id, {"contact_id": contact_id}
        )
        payload = {
                "feedback_id": feedback_id,
                "contact_id": contact_id,
                "sentiment": "positive",
                "rating": rating,
                "status": "processed",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        feedback_text = f"{feedback_text}"
        rating = int(rating) if rating is not None else None

        if not contact_id or not feedback_text:
            return _error("contact_id and feedback_text are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        feedback_entries = data.setdefault("customer_feedback", [])
        feedback_id = f"FB_{len(feedback_entries) + 1:04d}"

        feedback = {
            "feedback_id": feedback_id,
            "contact_id": contact_id,
            "feedback_text": feedback_text,
            "rating": rating,
            "sentiment": "positive",
            "submitted_at": FIXED_NOW,
            "status": "new",
        }
        feedback_entries.append(feedback)

        _append_audit(
            data, "feedback_processed", feedback_id, {"contact_id": contact_id}
        )
        payload = {
                "feedback_id": feedback_id,
                "contact_id": contact_id,
                "sentiment": "positive",
                "rating": rating,
                "status": "processed",
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
                "name": "ProcessCustomerFeedback",
                "description": "Process and categorize customer feedback for quality improvement.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "feedback_text": {"type": "string"},
                        "rating": {"type": "integer"},
                    },
                    "required": ["contact_id", "feedback_text"],
                },
            },
        }
