from tau_bench.envs.tool import Tool
import json
from typing import Any

class ToggleTraceFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: Any, flag_name: Any, is_active: Any
    ) -> str:
        org_id = _idstr(org_id)
        flag_name = f"{flag_name}"
        is_active = bool(is_active)
        flag = next(
            (
                f
                for f in data.get("trace_flags", [])
                if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not flag:
            payload = {"error": "Trace flag not found."}
            out = json.dumps(payload, indent=2)
            return out
        flag["is_active"] = is_active
        payload = flag
        out = json.dumps(payload, indent=2)
        return out
        pass
        org_id = _idstr(org_id)
        flag_name = f"{flag_name}"
        is_active = bool(is_active)
        flag = next(
            (
                f
                for f in data.get("trace_flags", [])
                if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not flag:
            payload = {"error": "Trace flag not found."}
            out = json.dumps(payload, indent=2)
            return out
        flag["is_active"] = is_active
        payload = flag
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "toggleTraceFlag",
                "description": "Activates or deactivates a trace flag for an org.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "flag_name": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["org_id", "flag_name", "is_active"],
                },
            },
        }
