from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigureContentDeliveryNetwork(Tool):
    """Set up CDN configurations to enhance content delivery efficiency."""

    @staticmethod
    def invoke(
        data: dict[str, Any], cdn_provider: Any, region: Any = "us-east-1"
    ) -> str:
        if not cdn_provider:
            return _error("cdn_provider is required.")

        cdn_configs = data.setdefault("cdn_configurations", [])
        config_id = f"CDN_{len(cdn_configs) + 1:03d}"

        config = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        cdn_configs.append(config)

        result = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "status": "configured",
        }

        _append_audit(data, "cdn_configured", config_id, {"cdn_provider": cdn_provider})
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        cdn_provider = cdn_provider
        region = region

        if not cdn_provider:
            return _error("cdn_provider is required.")

        cdn_configs = data.setdefault("cdn_configurations", [])
        config_id = f"CDN_{len(cdn_configs) + 1:03d}"

        config = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        cdn_configs.append(config)

        result = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "status": "configured",
        }

        _append_audit(data, "cdn_configured", config_id, {"cdn_provider": cdn_provider})
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureContentDeliveryNetwork",
                "description": "Configure CDN settings for improved content delivery performance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cdn_provider": {"type": "string"},
                        "region": {"type": "string"},
                    },
                    "required": ["cdn_provider"],
                },
            },
        }
