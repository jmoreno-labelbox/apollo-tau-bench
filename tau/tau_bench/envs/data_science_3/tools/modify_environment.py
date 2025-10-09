from tau_bench.envs.tool import Tool
import json
from typing import Any

class ModifyEnvironment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None) -> str:
        updates = updates or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _fixed_now_iso()
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateEnvironment",
                "description": "Update environment variables/secrets.",
                "parameters": {
                    "type": "object",
                    "properties": {"updates": {"type": "object"}},
                    "required": ["updates"],
                },
            },
        }
