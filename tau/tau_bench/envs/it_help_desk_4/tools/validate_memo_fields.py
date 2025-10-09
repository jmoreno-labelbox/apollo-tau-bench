from tau_bench.envs.tool import Tool
import json
from typing import Any

class ValidateMemoFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo: dict[str, Any] = None) -> str:
        required_fields = [
            "legal_name",
            "department",
            "job_title",
            "manager_id",
            "start_date",
        ]
        missing_fields = [field for field in required_fields if field not in memo]
        if missing_fields:
            payload = {"is_valid": False, "missing_fields": missing_fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"is_valid": True, "missing_fields": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validateMemoFields",
                "description": "Validates that a parsed HR memo contains all required fields for onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo": {"type": "object"}},
                    "required": ["memo"],
                },
            },
        }
