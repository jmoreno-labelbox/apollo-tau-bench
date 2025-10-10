# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReceiveCiEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], provider: str, run_id: str, status: str, repo: Optional[str] = None, branch: Optional[str] = None, commit_sha: Optional[str] = None, job_name: Optional[str] = None) -> str:
        build_runs = _get_table(data, "build_runs")
        existing = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if existing:
            return json.dumps({"ack": True, "run_id": run_id, "deduplicated": True}, indent=2)
        record = {
            "run_id": run_id,
            "provider": provider,
            "status": status,
            "repo": repo,
            "branch": branch,
            "commit_sha": commit_sha,
            "job_name": job_name,
            "artifacts_uri": None,
            "logs_uri": None,
        }
        build_runs.append(record)
        return json.dumps({"ack": True, "run_id": run_id, "deduplicated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "receive_ci_event", "description": "Registers a CI event run envelope deterministically (idempotent by run_id).", "parameters": {"type": "object", "properties": {"provider": {"type": "string"}, "run_id": {"type": "string"}, "status": {"type": "string"}, "repo": {"type": "string"}, "branch": {"type": "string"}, "commit_sha": {"type": "string"}, "job_name": {"type": "string"}}, "required": ["provider", "run_id", "status"]}}}
