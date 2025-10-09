from tau_bench.envs.tool import Tool
import json
from typing import Any

class DraftFixDiffV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str) -> str:
        pass
        fixes = _get_table(data, "fix_proposals")
        existing = next((f for f in fixes if f.get("run_id") == run_id), None)
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        patch_id = f"FP-{run_id}"
        proposal = {
            "patch_id": patch_id,
            "run_id": run_id,
            "status": "proposed",
            "summary": f"auto tentative fix for run {run_id}",
        }
        fixes.append(proposal)
        payload = proposal
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DraftFixDiffV2",
                "description": "Creates a deterministic fix proposal entry using policy templates.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }
