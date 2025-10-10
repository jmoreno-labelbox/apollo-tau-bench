# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_build_run(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], commit_sha: str) -> str:
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("commit_sha") == commit_sha:
                return json.dumps(run, indent=2)
        return json.dumps({"error": f"Build run for commit {commit_sha} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_build_run", "description": "Finds a build run by the commit SHA that triggered it.", "parameters": { "type": "object", "properties": { "commit_sha": { "type": "string" } }, "required": ["commit_sha"] } } }
