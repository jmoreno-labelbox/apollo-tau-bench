# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class GeneratePromotionalCampaign(Tool):
    """Generate and configure promotional campaigns with targeting rules."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        campaign_name: Any,
        target_segment: Any = "all",
        discount_percentage: Any = 10,
    ) -> str:
        campaign_name = f"{campaign_name}"
        target_segment = f"{target_segment}"
        try:
            discount_percentage = int(discount_percentage)
        except Exception:
            discount_percentage = 10
        import re as _re_patch

        _m = _re_patch.match(r".*?-(\d+)$", campaign_name.strip())
        if _m:
            try:
                discount_percentage = int(_m.group(1))
            except Exception:
                pass
        campaign_name = campaign_name
        target_segment = target_segment
        discount_percentage = discount_percentage

        if not campaign_name:
            return _error("campaign_name is required.")

        promotions = data.setdefault("promotions", [])
        promotion_id = f"PROMO_{len(promotions) + 1:03d}"

        promotion = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "start_date": FIXED_NOW,
            "status": "active",
        }
        promotions.append(promotion)

        result = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "status": "active",
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_promotional_campaign",
                "description": "Generate and configure promotional campaigns with targeting rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_name": {"type": "string"},
                        "target_segment": {"type": "string"},
                        "discount_percentage": {"type": "number"},
                    },
                    "required": ["campaign_name"],
                },
            },
        }
