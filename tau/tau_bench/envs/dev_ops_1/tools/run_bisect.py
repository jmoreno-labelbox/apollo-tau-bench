# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunBisect(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, suspects: List[Dict[str, Any]], test_target: str) -> str:
        bisects = _get_table(data, "bisect_results")
        existing = next((b for b in bisects if b.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        first_bad = next((s.get("ref") for s in suspects if s.get("ref")), None)
        record = {"run_id": run_id, "test_target": test_target, "first_bad_commit": first_bad, "suspect_count": len(suspects)}
        bisects.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_bisect", "description": "Stores a deterministic bisect outcome for a run, selecting the first suspect ref as first_bad_commit.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "suspects": {"type": "array", "items": {"type": "string"}}, "test_target": {"type": "string"}}, "required": ["run_id", "suspects", "test_target"]}}}
