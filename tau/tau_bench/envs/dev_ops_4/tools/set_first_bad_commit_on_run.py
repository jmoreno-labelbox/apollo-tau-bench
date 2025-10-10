# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetFirstBadCommitOnRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_first_bad_commit_on_run",
                "description": "Annotates a run with a first-bad commit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "commit_sha": {"type": "string", "description": "First bad commit sha"}
                    },
                    "required": ["run_id", "commit_sha"]
                }
            }
        }

    @staticmethod
    def invoke(data, commit_sha, run_id):
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["first_bad_commit"] = commit_sha
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
