from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class LogAuditTrail(Tool):
    """Records a structured audit event to monitor significant system activities."""

    @staticmethod
    def invoke(data: dict[str, Any], audit_event: str = None, subject_id: str = None, outcome_code: str = None, outcome_details: dict = None) -> str:
        if not all([audit_event, subject_id, outcome_code]):
            payload = {"error": "audit_event, subject_id, and outcome_code are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if "audit_log" not in data:
            data["audit_log"] = []

        log_entry = {
            "event_type": audit_event,
            "subject_id": subject_id,
            "outcome_code": outcome_code,
            "outcome_details": outcome_details,
        }
        data["audit_log"].append(log_entry)
        payload = log_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditTrail",
                "description": "Logs a structured audit event for tracking important system actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_event": {
                            "type": "string",
                            "description": "The type of event being logged (e.g., 'PRODUCT_RISK_AUDIT').",
                        },
                        "subject_id": {
                            "type": "string",
                            "description": "The ID of the primary entity this event relates to (e.g., a SKU or Order ID).",
                        },
                        "outcome_code": {
                            "type": "string",
                            "description": "A fixed code representing the outcome (e.g., 'RISK_IDENTIFIED').",
                        },
                        "outcome_details": {
                            "type": "object",
                            "description": "A dictionary of key-value pairs containing specific data about the outcome.",
                        },
                    },
                    "required": ["audit_event", "subject_id", "outcome_code"],
                },
            },
        }
