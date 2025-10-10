# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetBisectResultOnRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_bisect_result_on_run",
                "description": "Stores a bisect result on a run's metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "first_bad_commit_sha": {"type": "string", "description": "First bad commit sha"},
                        "last_good_commit_sha": {"type": "string", "description": "Last good commit sha"},
                        "confidence": {"type": "number", "description": "Confidence score between 0 and 1"}
                    },
                    "required": ["run_id", "first_bad_commit_sha", "last_good_commit_sha"]
                }
            }
        }

    @staticmethod
    def invoke(data, confidence, first_bad_commit_sha, last_good_commit_sha, run_id):
        fbc = first_bad_commit_sha
        lgc = last_good_commit_sha
        conf = confidence
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["bisect"] = {"first_bad_commit_sha": fbc, "last_good_commit_sha": lgc, "confidence": conf}
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
