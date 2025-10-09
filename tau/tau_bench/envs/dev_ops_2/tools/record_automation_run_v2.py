from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordAutomationRunV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        automation_type: str,
        inputs: dict[str, Any],
        outputs: dict[str, Any],
        status: str,
    ) -> str:
        pass
        runs = _get_table(data, "automation_runs")
        max_id = _max_int_suffix(runs, "run_id", "AR", 0)
        run_id = f"AR-{max_id + 1}"
        rec = {
            "run_id": run_id,
            "automation_type": automation_type,
            "inputs": inputs,
            "outputs": outputs,
            "status": status,
        }
        runs.append(rec)
        payload = {"automation_run_id": run_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRunV2",
                "description": "Persists a deterministic automation_runs entry with next AR-<n> id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_type": {"type": "string"},
                        "inputs": {"type": "object"},
                        "outputs": {"type": "object"},
                        "status": {"type": "string"},
                    },
                    "required": ["automation_type", "inputs", "outputs", "status"],
                },
            },
        }
