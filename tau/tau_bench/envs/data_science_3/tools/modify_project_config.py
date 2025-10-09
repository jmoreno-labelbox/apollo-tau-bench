from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None) -> str:
        if updates is None:
            updates = {}
        cfg = data.get("project_config", {}).values()
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _fixed_now_iso()
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectConfig",
                "description": "Update project configuration with provided key/value pairs.",
                "parameters": {
                    "type": "object",
                    "properties": {"updates": {"type": "object"}},
                    "required": ["updates"],
                },
            },
        }
