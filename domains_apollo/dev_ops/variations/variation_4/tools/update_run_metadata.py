from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateRunMetadata(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateRunMetadata",
                "description": "Patches a run's metadata object by merging the provided fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "metadata_patch": {
                            "type": "object",
                            "description": "Partial metadata patch",
                        },
                    },
                    "required": ["run_id", "metadata_patch"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, metadata_patch=None):
        run_id = run_id
        patch = metadata_patch or {}
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta.update(patch)
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
