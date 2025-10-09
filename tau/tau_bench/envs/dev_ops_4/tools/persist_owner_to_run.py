from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class PersistOwnerToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "PersistOwnerToRun",
                "description": "Persists a resolved ownership mapping into the run metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "owner_id": {"type": "string", "description": "Owner user id"},
                        "team_id": {"type": "string", "description": "Team id"},
                        "ownership_type": {
                            "type": "string",
                            "description": "file_owner|codeowner|service_owner",
                            "enum": ["file_owner", "codeowner", "service_owner"],
                        },
                        "confidence_score": {"type": "number", "description": "0..1"},
                    },
                    "required": ["run_id", "owner_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, owner_id=None, team_id=None, ownership_type=None, confidence_score=None, owner_path=None):
        # Support owner_path as an alternative to owner_id
        if owner_path is not None:
            owner_id = owner_path
        owner = {
            "owner_id": owner_id,
            "team_id": team_id,
            "ownership_type": ownership_type,
            "confidence_score": confidence_score,
        }
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["owner"] = owner
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
