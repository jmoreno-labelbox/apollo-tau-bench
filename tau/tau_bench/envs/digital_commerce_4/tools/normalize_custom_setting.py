from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class NormalizeCustomSetting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], setting_id: str) -> str:
        settings = data.get("custom_settings", [])
        st = next((s for s in settings if s.get("setting_id") == setting_id), None)
        if not st:
            payload = {"error": f"setting {setting_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if st.get("value") == "NULL":
            st["value"] = None
        payload = st
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeCustomSetting",
                "description": "Normalize a custom setting value: string 'NULL' -> null.",
                "parameters": {
                    "type": "object",
                    "properties": {"setting_id": {"type": "string"}},
                    "required": ["setting_id"],
                },
            },
        }
