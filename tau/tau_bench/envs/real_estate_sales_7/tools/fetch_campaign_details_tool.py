# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchCampaignDetailsTool(Tool):
    """Fetch a campaign and related email count and audit entries."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = _as_int(kwargs.get("campaign_id"))
        if campaign_id is None:
            return _err("campaign_id is required")

        campaign = next(
            (
                c
                for c in list(data.get("campaigns", {}).values())
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_campaign_details",
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
