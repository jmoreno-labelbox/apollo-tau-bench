# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class GenerateEmailContentTool(Tool):
    """Generates HTML email content."""

    @staticmethod
    def invoke(data: Dict[str, Any], attachments, context_data, recipient_data, template_code) -> str:
        recipient_data = recipient_data or {}
        context_data = context_data or {}
        attachments = attachments or []

        if not template_code:
            return _err("template_code is required")

        # Content URI generated deterministically from template_code
        rid = recipient_data.get("client_id") or "000"
        if isinstance(rid, int) or (isinstance(rid, str) and rid.isdigit()):
            client_id = int(rid)
        else:
            client_id = 15  # Standard fallback option

        # URI generation tailored for specific templates
        if template_code == "open_house_summary":
            uri = f"https://storage.example.com/emails/email_openhouse_{client_id:03d}.html"
        elif template_code == "comp_report_delivery":
            uri = f"https://storage.example.com/emails/email_comp_{client_id:03d}.html"
        elif template_code == "report_followup":
            uri = f"https://storage.example.com/emails/email_report_followup_{client_id:03d}.html"
        elif template_code == "briefing_followup":
            uri = f"https://storage.example.com/emails/email_briefing_followup_{client_id:03d}.html"
        elif template_code == "briefing_delivery":
            uri = f"https://storage.example.com/emails/email_briefing_{client_id:03d}.html"
        elif template_code == "first_time_buyer":
            uri = f"https://storage.example.com/emails/email_first_buyer_{client_id:03d}.html"
        elif template_code == "general_update":
            uri = (
                f"https://storage.example.com/emails/email_general_{client_id:03d}.html"
            )
        elif template_code == "market_update":
            uri = (
                f"https://storage.example.com/emails/email_market_{client_id:03d}.html"
            )
        elif template_code == "investment_alert":
            uri = f"https://storage.example.com/emails/email_investment_{client_id:03d}.html"
        elif template_code == "listing_summary":
            uri = (
                f"https://storage.example.com/emails/email_listing_{client_id:03d}.html"
            )
        elif template_code == "welcome_new_client":
            uri = (
                f"https://storage.example.com/emails/email_welcome_{client_id:03d}.html"
            )
        elif template_code == "post_closing_checkin":
            uri = (
                f"https://storage.example.com/emails/email_closing_{client_id:03d}.html"
            )
        elif template_code == "next_steps":
            uri = f"https://storage.example.com/emails/email_next_steps_{client_id:03d}.html"
        elif template_code == "follow_up":
            uri = f"https://storage.example.com/emails/email_followup_{client_id:03d}.html"
        else:
            uri = f"https://storage.example.com/emails/email_comp_{client_id:03d}.html"

        # Assign subject line using the specified template.
        property_id = context_data.get("subject_property_id", "HTX003")
        date = context_data.get("date", "2025-09-15")

        if template_code == "open_house_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Open House Summary Report for {date}"
            )
        elif template_code == "comp_report_delivery":
            subject_line = (
                context_data.get("subject_line")
                or f"Your comparable analysis for {property_id} is complete"
            )
        elif template_code == "report_followup":
            subject_line = (
                context_data.get("subject_line")
                or f"Follow-up on Your Property Analysis for {property_id}"
            )
        elif template_code == "briefing_followup":
            subject_line = (
                context_data.get("subject_line") or f"Follow-up on Your Client Briefing"
            )
        elif template_code == "briefing_delivery":
            subject_line = (
                context_data.get("subject_line")
                or f"Your Property Market Briefing is Ready"
            )
        elif template_code == "first_time_buyer":
            subject_line = (
                context_data.get("subject_line")
                or f"First-Time Buyer Resources for {property_id}"
            )
        elif template_code == "general_update":
            subject_line = (
                context_data.get("subject_line") or f"Real Estate Market Update"
            )
        elif template_code == "market_update":
            subject_line = context_data.get("subject_line") or f"Your Market Update"
        elif template_code == "investment_alert":
            subject_line = (
                context_data.get("subject_line") or f"Investment Opportunity Alert"
            )
        elif template_code == "listing_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Property Listing Summary for {property_id}"
            )
        elif template_code == "welcome_new_client":
            subject_line = (
                context_data.get("subject_line")
                or f"Welcome to Our Real Estate Services"
            )
        elif template_code == "post_closing_checkin":
            subject_line = (
                context_data.get("subject_line")
                or f"Post-Closing Check-in and Next Steps"
            )
        elif template_code == "next_steps":
            subject_line = (
                context_data.get("subject_line")
                or f"Next Steps in Your Real Estate Journey"
            )
        elif template_code == "follow_up":
            subject_line = (
                context_data.get("subject_line")
                or f"Following Up on Your Real Estate Needs"
            )
        else:
            subject_line = (
                context_data.get("subject_line")
                or f"Your Comparable Property Analysis for {property_id}"
            )

        out = {
            "email_content_uri": uri,
            "template_used": str(template_code),
            "personalization_applied": True,
            "subject_line": subject_line,
            "attachment_count": int(len(attachments)),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_email_content",
                "description": "Generate HTML email content and return its URI.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_code": {"type": "string"},
                        "recipient_data": {"type": "object"},
                        "context_data": {"type": "object"},
                        "attachments": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "template_code",
                        "recipient_data",
                        "context_data",
                        "attachments",
                    ],
                },
            },
        }