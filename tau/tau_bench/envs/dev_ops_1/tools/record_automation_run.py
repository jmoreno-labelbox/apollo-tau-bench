# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _max_int_suffix(items: List[Dict[str, Any]], key: str, prefix: str, default: int = 0) -> int:
    max_val = default
    for it in items:
        raw = it.get(key)
        if isinstance(raw, str) and raw.startswith(prefix + "-"):
            try:
                num = int(raw.split("-")[-1])
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
    return max_val

def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], automation_type: str, inputs: Dict[str, Any], outputs: Dict[str, Any], status: str) -> str:
        runs = _get_table(data, "automation_runs")
        max_id = _max_int_suffix(runs, "run_id", "AR", 0)
        run_id = f"AR-{max_id + 1}"
        rec = {"run_id": run_id, "automation_type": automation_type, "inputs": inputs, "outputs": outputs, "status": status}
        runs.append(rec)
        return json.dumps({"automation_run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "record_automation_run", "description": "Persists a deterministic automation_runs entry with next run_id.", "parameters": {"type": "object", "properties": {"automation_type": {"type": "string"}, "inputs": {"type": "object"}, "outputs": {"type": "object"}, "status": {"type": "string"}}, "required": ["automation_type", "inputs", "outputs", "status"]}}}