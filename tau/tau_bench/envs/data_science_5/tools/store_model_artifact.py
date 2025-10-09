from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class StoreModelArtifact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_name: str = None,
        model_type: str = None,
        framework: str = None,
        version: str = None,
        status: str = None
    ) -> str:
        models = data.get("models", {}).values()
        max_id = 0
        for m in models:
            try:
                mid = int(m.get("model_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "model_id": new_id,
            "model_name": model_name,
            "model_type": model_type,
            "framework": framework,
            "version": version,
            "status": status,
            "created_at": _now_iso_fixed(),
            "updated_at": _now_iso_fixed(),
        }
        data["models"][row["model_id"]] = row
        payload = {"model_id": new_id, "model_name": row["model_name"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreModelArtifact",
                "description": "Register a model in the registry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "model_type": {"type": "string"},
                        "framework": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "model_name",
                        "model_type",
                        "framework",
                        "version",
                        "status",
                    ],
                },
            },
        }
