from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateSecretFor(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], environment: str, purpose: str, value_source_id: str
    ) -> str:
        _environmentL = environment or ''.lower()
        pass
        settings = _ensure_table(data, "custom_settings")
        key = f"secret:{purpose}:{environment}"
        kms_key_alias = f"alias/dcomm-{environment.lower()}"
        secret_arn = _stable_id("arn:secret", key, value_source_id, kms_key_alias)
        row = _find_one(settings, name=key)
        payload = {"source": value_source_id, "kms": kms_key_alias, "arn": secret_arn}
        if row:
            row.update({"value": json.dumps(payload), "updated_at": FIXED_NOW})
        else:
            settings.append(
                {
                    "setting_id": _stable_id("sec", key),
                    "name": key,
                    "value": json.dumps(payload),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"secret_arn": secret_arn})
        _environmentL = environment or ''.lower()
        pass
        settings = _ensure_table(data, "custom_settings")
        key = f"secret:{purpose}:{environment}"
        kms_key_alias = f"alias/dcomm-{environment.lower()}"
        secret_arn = _stable_id("arn:secret", key, value_source_id, kms_key_alias)
        row = _find_one(settings, name=key)
        payload = {"source": value_source_id, "kms": kms_key_alias, "arn": secret_arn}
        if row:
            row.update({"value": json.dumps(payload), "updated_at": FIXED_NOW})
        else:
            settings.append(
                {
                    "setting_id": _stable_id("sec", key),
                    "name": key,
                    "value": json.dumps(payload),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"secret_arn": secret_arn})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateSecretFor",
                "description": "Create/rotate a secret using deterministic naming by environment and purpose.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "purpose": {
                            "type": "string",
                            "enum": [
                                "REDIS_AUTH_HEADER",
                                "OAUTH_CLIENT_SECRET",
                                "API_AUTH_HEADER",
                            ],
                        },
                        "value_source_id": {"type": "string"},
                    },
                    "required": ["environment", "purpose", "value_source_id"],
                },
            },
        }
