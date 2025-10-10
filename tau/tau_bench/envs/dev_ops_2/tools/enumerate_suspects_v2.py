# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnumerateSuspectsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        build_runs = _get_table(data, "build_runs")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        suspects = []
        if run.get("first_bad_commit"):
            suspects.append({"ref": run.get("first_bad_commit")})
        return json.dumps({"suspects": suspects}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enumerate_suspects_v2", "description": "Enumerates suspects from stored run fields (e.g., first_bad_commit).", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}
