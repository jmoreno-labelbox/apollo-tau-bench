from tau_bench.envs.tool import Tool
import json
from typing import Any

class find_build_run(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], commit_sha: str) -> str:
        pass
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("commit_sha") == commit_sha:
                payload = run
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Build run for commit {commit_sha} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindBuildRun",
                "description": "Finds a build run by the commit SHA that triggered it.",
                "parameters": {
                    "type": "object",
                    "properties": {"commit_sha": {"type": "string"}},
                    "required": ["commit_sha"],
                },
            },
        }
