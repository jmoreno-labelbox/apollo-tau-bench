# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetTraceFlag(Tool):
    """Enable/disable a trace flag for an org (ensure-exists)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, flag_name: Any, is_active: Any) -> str:
        if not org_id or not flag_name or is_active is None:
            return json.dumps(
                {"error": "Missing required fields: org_id, flag_name, is_active"}, indent=2
            )
        flags = data.setdefault("trace_flags", [])
        for flag in flags:
            if flag.get("org_id") == org_id and flag.get("flag_name") == flag_name:
                flag["is_active"] = bool(is_active)
                return json.dumps(flag, indent=2)
        next_id = str(max([int(f.get("flag_id")) for f in flags] + [400]) + 1)
        record = {
            "flag_id": next_id,
            "org_id": org_id,
            "flag_name": flag_name,
            "is_active": bool(is_active),
        }
        flags.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_trace_flag",
                "description": "Ensure a trace flag exists and set its active state for the org.",
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
