from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetFirstBadCommitOnRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetFirstBadCommitOnRun",
                "description": "Annotates a run with a first-bad commit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "commit_sha": {
                            "type": "string",
                            "description": "First bad commit sha",
                        },
                    },
                    "required": ["run_id", "commit_sha"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, commit_sha=None):
        pass
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["first_bad_commit"] = commit_sha
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
