# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkArtifactToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "link_artifact_to_run",
                "description": "Sets the artifacts_uri on a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "artifacts_uri": {"type": "string", "description": "Artifacts URI"}
                    },
                    "required": ["run_id", "artifacts_uri"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        artifacts_uri = kwargs.get("artifacts_uri")
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        run["artifacts_uri"] = artifacts_uri
        return json.dumps({"run": run}, indent=2)
