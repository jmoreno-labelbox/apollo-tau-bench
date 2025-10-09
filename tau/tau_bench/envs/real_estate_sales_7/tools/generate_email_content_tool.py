from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GenerateEmailContentTool(Tool):
    """Creates HTML content for emails."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        template_code: str = None,
        recipient_data: dict[str, Any] = None,
        context_data: dict[str, Any] = None,
        attachments: list = None
    ) -> str:
        recipient_data = recipient_data or {}
        context_data = context_data or {}
        attachments = attachments or []

        if not template_code:
            return _err("template_code is required")

        # Deterministic content URI generated from template_code
        rid = recipient_data.get("client_id") or "000"
        if isinstance(rid, int) or (isinstance(rid, str) and rid.isdigit()):
            client_id = int(rid)
        else:
            client_id = 15  # Standard fallback

        # URI generation specific to the template
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

        # Establish subject line according to the template
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
                context_data.get("subject_line") or "Follow-up on Your Client Briefing"
            )
        elif template_code == "briefing_delivery":
            subject_line = (
                context_data.get("subject_line")
                or "Your Property Market Briefing is Ready"
            )
        elif template_code == "first_time_buyer":
            subject_line = (
                context_data.get("subject_line")
                or f"First-Time Buyer Resources for {property_id}"
            )
        elif template_code == "general_update":
            subject_line = (
                context_data.get("subject_line") or "Real Estate Market Update"
            )
        elif template_code == "market_update":
            subject_line = context_data.get("subject_line") or "Your Market Update"
        elif template_code == "investment_alert":
            subject_line = (
                context_data.get("subject_line") or "Investment Opportunity Alert"
            )
        elif template_code == "listing_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Property Listing Summary for {property_id}"
            )
        elif template_code == "welcome_new_client":
            subject_line = (
                context_data.get("subject_line")
                or "Welcome to Our Real Estate Services"
            )
        elif template_code == "post_closing_checkin":
            subject_line = (
                context_data.get("subject_line")
                or "Post-Closing Check-CO and Next Steps"
            )
        elif template_code == "next_steps":
            subject_line = (
                context_data.get("subject_line")
                or "Next Steps in Your Real Estate Journey"
            )
        elif template_code == "follow_up":
            subject_line = (
                context_data.get("subject_line")
                or "Following Up on Your Real Estate Needs"
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateEmailContent",
                "description": "Generate HTML email content and return its URI.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_code": {"type": "string"},
                        "recipient_data": {"type": "object"},
                        "context_data": {"type": "object"},
                        "attachments": {"type": "array"},
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
