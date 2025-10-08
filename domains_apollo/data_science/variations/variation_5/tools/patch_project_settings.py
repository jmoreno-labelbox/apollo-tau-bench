from tau_bench.envs.tool import Tool
import json
from typing import Any

class PatchProjectSettings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None) -> str:
        if updates is None:
            updates = {}
        cfg = data.get("project_config", {})
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _now_iso_fixed()
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PatchProjectSettings",
                "description": "Apply key/value updates to project settings.",
                "parameters": {
                    "type": "object",
                    "properties": {"updates": {"type": "object"}},
                    "required": ["updates"],
                },
            },
        }
