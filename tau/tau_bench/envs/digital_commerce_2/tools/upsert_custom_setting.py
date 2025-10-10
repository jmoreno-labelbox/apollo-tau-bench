# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertCustomSetting(Tool):
    """Upsert a custom setting value for an org (ensure-exists)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, setting_name: Any, value: Any) -> str:
        if not org_id or not setting_name:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or setting_name"}, indent=2
            )
        settings = data.setdefault("custom_settings", [])
        for rec in settings:
            if rec.get("org_id") == org_id and rec.get("setting_name") == setting_name:
                rec["value"] = value
                return json.dumps(rec, indent=2)
        next_id = str(max([int(s.get("setting_id")) for s in settings] + [100]) + 1)
        record = {
            "setting_id": next_id,
            "org_id": org_id,
            "setting_name": setting_name,
            "value": value,
        }
        settings.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_custom_setting",
                "description": "Create or update a custom setting (org_id + setting_name) with the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "setting_name": {"type": "string"},
                        "value": {},
                    },
                    "required": ["org_id", "setting_name", "value"],
                },
            },
        }
