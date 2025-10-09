from tau_bench.envs.tool import Tool
import json
from typing import Any

class GuardrailValidateSenderV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str) -> str:
        pass
        build_runs = _get_table(data, "build_runs")
        branches = _get_table(data, "branches")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        #Check if the branch is present in the branches dataset
        allowed = any(b.get("name") == run.get("branch") for b in branches.values())
        run["validated"] = bool(allowed)
        payload = {"validated": bool(allowed)}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GuardrailValidateSenderV2",
                "description": "Validates repo/branch against DB; records validation flag on build_runs.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }
