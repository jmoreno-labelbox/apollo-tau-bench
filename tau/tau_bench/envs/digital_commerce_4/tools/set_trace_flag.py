from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetTraceFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: str, flag_name: str, is_active: bool
    ) -> str:
        org_id, flag_name = _sid(org_id), _sid(flag_name)
        is_active = bool(is_active)
        flags = data.get("trace_flags", {}).values()
        tf = next(
            (
                f
                for f in flags.values() if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not tf:
            payload = {"error": "trace flag not found"}
            out = json.dumps(payload, indent=2)
            return out
        org_type = (
            "UAT"
            if org_id.endswith("QRS")
            else ("Staging" if org_id.endswith("DEF") else "Production")
        )
        if (
            org_type == "Production"
            and is_active
            and flag_name in ("CacheAPI.EcommLogger", "ApexDebug")
        ):
            payload = {"error": "forbidden in Production"}
            out = json.dumps(payload, indent=2)
            return out
        tf["is_active"] = bool(is_active)
        _ws_append(
            data,
            f"{org_id}:{flag_name}",
            "SET_TRACE_FLAG",
            {"is_active": bool(is_active)},
        )
        _append_audit(
            data,
            "SET_TRACE_FLAG",
            f"{org_id}:{flag_name}",
            {"is_active": bool(is_active)},
        )
        payload = tf
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setTraceFlag",
                "description": "Enable/disable a trace flag with production-safe guardrails.",
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
