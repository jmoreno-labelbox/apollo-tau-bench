from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SaveModelConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, config_name: str = None, params: dict = None) -> str:
        if params is None:
            params = {}
        cfgs = data.get("model_config", {}).values()
        row = next(
            (
                c
                for c in cfgs.values() if c.get("model_name") == model_name
                and c.get("config_name") == config_name
            ),
            None,
        )
        if row:
            row["params"] = params
            row["updated_at"] = _fixed_now_iso()
            out = {
                "model_name": model_name,
                "config_name": config_name,
                "action": "updated",
            }
        else:
            max_id = 0
            for c in cfgs.values():
                try:
                    cid = int(c.get("config_id", 0))
                    if cid > max_id:
                        max_id = cid
                except (ValueError, TypeError):
                    continue
            new_id = max_id + 1
            row = {
                "config_id": new_id,
                "model_name": model_name,
                "config_name": config_name,
                "params": params,
                "created_at": _fixed_now_iso(),
            }
            data["model_config"][row["model_config_id"]] = row
            out = {
                "config_id": new_id,
                "model_name": model_name,
                "config_name": config_name,
                "action": "inserted",
            }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertModelConfig",
                "description": "Insert or update a model configuration by (model_name, config_name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "config_name": {"type": "string"},
                        "params": {"type": "object"},
                    },
                    "required": ["model_name", "config_name", "params"],
                },
            },
        }
