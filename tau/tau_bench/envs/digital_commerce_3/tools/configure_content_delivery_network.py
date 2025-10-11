# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ConfigureContentDeliveryNetwork(Tool):
    """Configure CDN settings for improved content delivery performance."""

    @staticmethod
    def invoke(data: Dict[str, Any], cdn_provider: Any, region: Any = "us-east-1") -> str:
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

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_content_delivery_network",
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
