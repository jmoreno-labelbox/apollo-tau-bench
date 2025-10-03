from tau_bench.envs.tool import Tool
import json
from typing import Any

class IngestCiWebhookV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        provider: str,
        run_id: str,
        status: str,
        repo: str | None = None,
        branch: str | None = None,
        commit_sha: str | None = None,
        job_name: str | None = None,
    ) -> str:
        pass
        build_runs = _get_table(data, "build_runs")
        existing = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if existing:
            payload = {"ack": True, "run_id": run_id, "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
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
        payload = {"ack": True, "run_id": run_id, "deduplicated": False}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IngestCiWebhookV2",
                "description": "Register a CI event envelope deterministically (idempotent by run_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "provider": {"type": "string"},
                        "run_id": {"type": "string"},
                        "status": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "commit_sha": {"type": "string"},
                        "job_name": {"type": "string"},
                    },
                    "required": ["provider", "run_id", "status"],
                },
            },
        }
