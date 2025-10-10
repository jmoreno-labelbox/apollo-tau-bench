# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AttachArtifactsIndexV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        build_runs = _get_table(data, "build_runs")
        artifacts = _get_table(data, "artifacts")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        # verify artifact entry
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        art.setdefault("logs_uri", f"artifact://logs/{run_id}")
        art.setdefault("reports_uri", f"artifact://reports/{run_id}")
        run["logs_uri"] = art["logs_uri"]
        run["artifacts_uri"] = art["reports_uri"]
        return json.dumps({"logs_uri": art["logs_uri"], "reports_uri": art["reports_uri"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "attach_artifacts_index_v2", "description": "Attaches deterministic logs/report URIs to a run and artifacts table.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}
