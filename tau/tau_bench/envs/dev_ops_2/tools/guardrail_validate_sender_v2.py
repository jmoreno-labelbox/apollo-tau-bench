# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GuardrailValidateSenderV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        build_runs = _get_table(data, "build_runs")
        branches = _get_table(data, "branches")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        # Validate branch exists in branches dataset
        allowed = any(b.get("name") == run.get("branch") for b in branches)
        run["validated"] = bool(allowed)
        return json.dumps({"validated": bool(allowed)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "guardrail_validate_sender_v2", "description": "Validates repo/branch against DB; records validation flag on build_runs.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}
