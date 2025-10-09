from tau_bench.envs.tool import Tool
import json
from typing import Any

class LaunchTargetedBisectV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], run_id: str, test_target: str | None = None
    ) -> str:
        pass
        bisects = _get_table(data, "bisect_results")
        build_runs = _get_table(data, "build_runs")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        existing = next((b for b in bisects if b.get("run_id") == run_id), None)
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        record = {
            "run_id": run_id,
            "test_target": test_target
            or run.get("repro_command")
            or (run.get("job_name") or "smoke"),
            "first_bad_commit": run.get("first_bad_commit"),
        }
        bisects.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LaunchTargetedBisectV2",
                "description": "Stores deterministic bisect outcome for run using stored first_bad_commit and repro_command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "test_target": {"type": "string"},
                    },
                    "required": ["run_id"],
                },
            },
        }
