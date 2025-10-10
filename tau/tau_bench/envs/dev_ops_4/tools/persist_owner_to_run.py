# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PersistOwnerToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "persist_owner_to_run",
                "description": "Persists a resolved ownership mapping into the run metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "owner_id": {"type": "string", "description": "Owner user id"},
                        "team_id": {"type": "string", "description": "Team id"},
                        "ownership_type": {"type": "string", "description": "file_owner|codeowner|service_owner", "enum": ["file_owner", "codeowner", "service_owner"]},
                        "confidence_score": {"type": "number", "description": "0..1"}
                    },
                    "required": ["run_id", "owner_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, confidence_score, owner_id, ownership_type, run_id, team_id):
        owner = {
            "owner_id": owner_id,
            "team_id": team_id,
            "ownership_type": ownership_type,
            "confidence_score": confidence_score,
        }
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["owner"] = owner
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
