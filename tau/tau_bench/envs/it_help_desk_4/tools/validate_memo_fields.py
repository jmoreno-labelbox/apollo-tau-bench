# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateMemoFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        memo = kwargs.get("memo")
        required_fields = ["legal_name", "department", "job_title", "manager_id", "start_date"]
        missing_fields = [field for field in required_fields if field not in memo]
        if missing_fields:
            return json.dumps({"is_valid": False, "missing_fields": missing_fields}, indent=2)
        return json.dumps({"is_valid": True, "missing_fields": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_memo_fields", "description": "Validates that a parsed HR memo contains all required fields for onboarding.", "parameters": {"type": "object", "properties": {"memo": {"type": "object"}}, "required": ["memo"]}}}
