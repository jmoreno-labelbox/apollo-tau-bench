# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogAuditTrail(Tool):
    """Logs a structured audit event for tracking important system actions."""
    @staticmethod
    def invoke(data: Dict[str, Any], audit_event, outcome_code, outcome_details, subject_id) -> str:

        if not all([audit_event, subject_id, outcome_code]):
            return json.dumps({"error": "audit_event, subject_id, and outcome_code are required."}, indent=2)

        if 'audit_log' not in data:
            data['audit_log'] = []

        log_entry = {
            "event_type": audit_event,
            "subject_id": subject_id,
            "outcome_code": outcome_code,
            "outcome_details": outcome_details
        }
        data['audit_log'].append(log_entry)
        return json.dumps(log_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_trail",
                "description": "Logs a structured audit event for tracking important system actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_event": {"type": "string", "description": "The type of event being logged (e.g., 'PRODUCT_RISK_AUDIT')."},
                        "subject_id": {"type": "string", "description": "The ID of the primary entity this event relates to (e.g., a SKU or Order ID)."},
                        "outcome_code": {"type": "string", "description": "A fixed code representing the outcome (e.g., 'RISK_IDENTIFIED')."},
                        "outcome_details": {"type": "object", "description": "A dictionary of key-value pairs containing specific data about the outcome."}
                    },
                    "required": ["audit_event", "subject_id", "outcome_code"]
                }
            }
        }
