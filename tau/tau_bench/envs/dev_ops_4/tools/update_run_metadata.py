# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRunMetadata(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_run_metadata",
                "description": "Patches a run's metadata object by merging the provided fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "metadata_patch": {"type": "object", "description": "Partial metadata patch"}
                    },
                    "required": ["run_id", "metadata_patch"]
                }
            }
        }

    @staticmethod
    def invoke(data, metadata_patch, run_id):
        patch = metadata_patch or {}
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta.update(patch)
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
