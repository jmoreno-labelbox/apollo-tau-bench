from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnableDigitalCommerceGateway(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], api_group_name: str, environment: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        key = f"DCG:{api_group_name}:{environment}"
        row = _find_one(settings, name=key)
        value = json.dumps(
            {"status": "Enabled", "group": api_group_name, "env": environment}
        )
        if row:
            row["value"] = value
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("dcg", api_group_name, environment),
                    "name": key,
                    "value": value,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json(
            {
                "dcg_id": _stable_id("dcg", api_group_name, environment),
                "status": "Enabled",
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnableDigitalCommerceGateway",
                "description": "Enable the Digital Commerce Gateway group in an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "api_group_name": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                    },
                    "required": ["api_group_name", "environment"],
                },
            },
        }
