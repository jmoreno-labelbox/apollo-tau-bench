from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkArtifactToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LinkArtifactToRun",
                "description": "Sets the artifacts_uri on a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "artifacts_uri": {
                            "type": "string",
                            "description": "Artifacts URI",
                        },
                    },
                    "required": ["run_id", "artifacts_uri"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, artifacts_uri=None, artifact_id=None):
        # Support artifact_id as an alternative to artifacts_uri
        if artifact_id is not None:
            artifacts_uri = artifact_id
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        run["artifacts_uri"] = artifacts_uri
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
