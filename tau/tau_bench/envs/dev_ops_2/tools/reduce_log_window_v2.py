# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReduceLogWindowV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        artifacts = _get_table(data, "artifacts")
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        reduced_log_uri = f"artifact://reduced_log/{run_id}"
        art["reduced_log_uri"] = reduced_log_uri
        return json.dumps({"reduced_log_uri": reduced_log_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "reduce_log_window_v2", "description": "Writes a deterministic reduced log URI for the run.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}
