# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class AttachRunArtifacts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, logs_uri: Optional[str] = None, dumps_uri: Optional[str] = None, reports_uri: Optional[str] = None) -> str:
        build_runs = _get_table(data, "build_runs")
        artifacts = _get_table(data, "artifacts")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        artifact_entry = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not artifact_entry:
            artifact_entry = {"run_id": run_id}
            artifacts.append(artifact_entry)
        if logs_uri is None:
            logs_uri = f"artifact://logs/{run_id}"
        if reports_uri is None:
            reports_uri = f"artifact://reports/{run_id}"
        artifact_entry.update({"logs_uri": logs_uri, "dumps_uri": dumps_uri, "reports_uri": reports_uri})
        run["logs_uri"] = logs_uri
        run["artifacts_uri"] = reports_uri
        return json.dumps(artifact_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "attach_run_artifacts", "description": "Attaches deterministic artifact URIs to a CI run and persists an artifact record.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "logs_uri": {"type": "string"}, "dumps_uri": {"type": "string"}, "reports_uri": {"type": "string"}}, "required": ["run_id"]}}}