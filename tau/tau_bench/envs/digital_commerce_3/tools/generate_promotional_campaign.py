from tau_bench.envs.tool import Tool
import json
from typing import Any

class GeneratePromotionalCampaign(Tool):
    """Create and set up marketing campaigns with targeting criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_name: Any,
        target_segment: Any = "all",
        discount_percentage: Any = 10
    ) -> str:
        pass
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
        data["promotions"][promotion["promotion_id"]] = promotion

        result = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "status": "active",
        }

        _append_audit(
            data,
            "promotion_created",
            promotion_id,
            {"campaign_name": campaign_name, "target_segment": target_segment},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
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
        data["promotions"][promotion["promotion_id"]] = promotion

        result = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "status": "active",
        }

        _append_audit(
            data,
            "promotion_created",
            promotion_id,
            {"campaign_name": campaign_name, "target_segment": target_segment},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GeneratePromotionalCampaign",
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
