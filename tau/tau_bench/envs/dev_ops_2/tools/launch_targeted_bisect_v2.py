# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class LaunchTargetedBisectV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, test_target: Optional[str] = None) -> str:
        bisects = _get_table(data, "bisect_results")
        build_runs = _get_table(data, "build_runs")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        existing = next((b for b in bisects if b.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        record = {
            "run_id": run_id,
            "test_target": test_target or run.get("repro_command") or (run.get("job_name") or "smoke"),
            "first_bad_commit": run.get("first_bad_commit"),
        }
        bisects.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "launch_targeted_bisect_v2", "description": "Stores deterministic bisect outcome for run using stored first_bad_commit and repro_command.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "test_target": {"type": "string"}}, "required": ["run_id"]}}}