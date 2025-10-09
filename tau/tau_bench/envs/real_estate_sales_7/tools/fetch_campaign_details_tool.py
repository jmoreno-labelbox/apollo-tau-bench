from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class FetchCampaignDetailsTool(Tool):
    """Retrieve a campaign along with the associated email count and audit records."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: int = None) -> str:
        campaign_id = _as_int(campaign_id)
        if campaign_id is None:
            return _err("campaign_id is required")

        campaign = next(
            (
                c
                for c in data.get("campaigns", [])
                if _as_int(c.get("campaign_id")) == campaign_id
            ),
            None,
        )
        if not campaign:
            return _err(f"campaign_id {campaign_id} not found", code="not_found")

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("campaign_id")) == campaign_id
        ]
        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "campaign"
            and _as_int(a.get("entity_id")) == campaign_id
        ]
        audits_sorted = sorted(
            audits, key=lambda a: a.get("occurred_at") or "", reverse=True
        )

        out = {
            "campaign": campaign,
            "emails_count": len(emails),
            "audit_events": audits_sorted[:10],
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCampaignDetails",
                "description": (
                    "Fetch campaign record with email count and audit history."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }
