# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadOffboardingMemo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], memo_id) -> str:
        memo = next((m for m in list(data.get("hr_memos", {}).values()) if m.get("memo_id") == memo_id and m.get("type") == "offboarding"), None)
        if not memo:
            return json.dumps({"error": f"Offboarding memo {memo_id} not found."}, indent=2)
        return json.dumps(memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "read_offboarding_memo", "description": "Reads and returns a specific offboarding memo from the HR memos table.", "parameters": {"type": "object", "properties": {"memo_id": {"type": "string"}}, "required": ["memo_id"]}}}
