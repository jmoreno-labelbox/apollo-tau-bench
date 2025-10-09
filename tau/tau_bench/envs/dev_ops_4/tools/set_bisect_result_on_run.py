from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetBisectResultOnRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBisectResultOnRun",
                "description": "Stores a bisect result on a run's metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "first_bad_commit_sha": {
                            "type": "string",
                            "description": "First bad commit sha",
                        },
                        "last_good_commit_sha": {
                            "type": "string",
                            "description": "Last good commit sha",
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score between 0 and 1",
                        },
                    },
                    "required": [
                        "run_id",
                        "first_bad_commit_sha",
                        "last_good_commit_sha",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, first_bad_commit_sha=None, last_good_commit_sha=None, confidence=None, bisect_result=None):
        # Support bisect_result as an alternative parameter
        if bisect_result is not None:
            if isinstance(bisect_result, dict):
                first_bad_commit_sha = bisect_result.get('first_bad_commit_sha', first_bad_commit_sha)
                last_good_commit_sha = bisect_result.get('last_good_commit_sha', last_good_commit_sha)
        run = next((r for r in data.get("build_runs", {}).values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["bisect"] = {
            "first_bad_commit_sha": first_bad_commit_sha,
            "last_good_commit_sha": last_good_commit_sha,
            "confidence": confidence,
        }
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
