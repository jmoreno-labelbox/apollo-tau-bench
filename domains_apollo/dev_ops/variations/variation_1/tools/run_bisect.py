from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunBisect(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str,
        suspects: list[dict[str, Any]],
        test_target: str,
    ) -> str:
        bisects = _get_table(data, "bisect_results")
        existing = next((b for b in bisects if b.get("run_id") == run_id), None)
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        first_bad = next((s.get("ref") for s in suspects if s.get("ref")), None)
        record = {
            "run_id": run_id,
            "test_target": test_target,
            "first_bad_commit": first_bad,
            "suspect_count": len(suspects),
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
                "name": "RunBisect",
                "description": "Stores a deterministic bisect outcome for a run, selecting the first suspect ref as first_bad_commit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "suspects": {"type": "array"},
                        "test_target": {"type": "string"},
                    },
                    "required": ["run_id", "suspects", "test_target"],
                },
            },
        }
