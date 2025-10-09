from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetFeatureToggle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, toggle_name: str, value: str) -> str:
        org_id, toggle_name, value = _sid(org_id), _sid(toggle_name), _sid(value)
        settings = data.get("custom_settings", [])
        st = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id and s.get("setting_name") == toggle_name
            ),
            None,
        )
        if not st:
            payload = {"error": "toggle not found"}
            out = json.dumps(payload, indent=2)
            return out
        st["value"] = value
        _ws_append(
            data, f"{org_id}:{toggle_name}", "SET_FEATURE_TOGGLE", {"value": value}
        )
        _append_audit(
            data, "SET_FEATURE_TOGGLE", f"{org_id}:{toggle_name}", {"value": value}
        )
        payload = st
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setFeatureToggle",
                "description": "Set a feature toggle value via custom settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "toggle_name": {"type": "string"},
                        "value": {"type": "string"},
                    },
                    "required": ["org_id", "toggle_name", "value"],
                },
            },
        }
