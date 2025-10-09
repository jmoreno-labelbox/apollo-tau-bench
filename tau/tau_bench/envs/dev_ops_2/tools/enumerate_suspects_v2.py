from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnumerateSuspectsV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str) -> str:
        pass
        build_runs = _get_table(data, "build_runs")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        suspects = []
        if run.get("first_bad_commit"):
            suspects.append({"ref": run.get("first_bad_commit")})
        payload = {"suspects": suspects}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnumerateSuspectsV2",
                "description": "Enumerates suspects from stored run fields (e.g., first_bad_commit).",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }
