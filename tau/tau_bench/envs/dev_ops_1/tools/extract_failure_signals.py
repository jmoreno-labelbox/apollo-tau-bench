# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class ExtractFailureSignals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        artifacts = _get_table(data, "artifacts")
        build_runs = _get_table(data, "build_runs")
        crashes = _get_table(data, "crash_events")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        reduced_log_uri = f"artifact://reduced_log/{run_id}"
        symbolicated_stack_uri = f"artifact://symbolicated_stack/{run_id}"
        art.update({"reduced_log_uri": reduced_log_uri, "symbolicated_stack_uri": symbolicated_stack_uri})
        signature = f"sig:{run.get('commit_sha') or run_id}:first_failure"
        crashes.append({"crash_id": f"CR-{run_id}", "fingerprint": signature, "build_number": run_id, "platform": run.get("provider"), "count_24h": 1, "top_frame": "main()", "symbolicated_stack_uri": symbolicated_stack_uri})
        return json.dumps({"reduced_log_uri": reduced_log_uri, "symbolicated_stack_uri": symbolicated_stack_uri, "error_signature": signature}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "extract_failure_signals", "description": "Creates deterministic reduced log and symbolicated stack URIs and stores an error signature.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}