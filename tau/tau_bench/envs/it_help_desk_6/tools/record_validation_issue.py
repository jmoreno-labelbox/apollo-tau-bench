# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordValidationIssue(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], issue_id: str, entity: str, entity_id: str, field: str, rule: str, details: str, created_at: str
    ) -> str:
        row = {
            "issue_id": issue_id,
            "entity": entity,
            "entity_id": entity_id,
            "field": field,
            "rule": rule,
            "details": details,
            "created_at": created_at,
        }
        _append_row(data["validation_issues"], row)
        return json.dumps({"status": "ok", "validation_issue": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_validation_issue",
                "description": "Append a validation issue entry describing an input or data inconsistency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_id": {"type": "string"},
                        "entity": {"type": "string"},
                        "entity_id": {"type": "string"},
                        "field": {"type": "string"},
                        "rule": {"type": "string"},
                        "details": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["issue_id", "entity", "entity_id", "field", "rule", "details", "created_at"],
                },
            },
        }
