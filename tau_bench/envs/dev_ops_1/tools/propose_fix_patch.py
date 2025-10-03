from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProposeFixPatch(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str,
        logs_uri: str | None = None,
        first_bad_commit: str | None = None,
    ) -> str:
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
            "logs_uri": logs_uri or f"artifact://logs/{run_id}",
            "first_bad_commit": first_bad_commit,
            "status": "proposed",
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
                "name": "ProposeFixPatch",
                "description": "Creates a deterministic fix proposal entry for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "logs_uri": {"type": "string"},
                        "first_bad_commit": {"type": "string"},
                    },
                    "required": ["run_id"],
                },
            },
        }
