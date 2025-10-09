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

class SendEmailTool(Tool):
    """Generates an email entry with automatic subject/body creation if not provided."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        broker_id: str = None,
        template_code: str = None,
        subject: str = None,
        body_uri: str = None,
        campaign_id: str = None,
        property_id: str = None
    ) -> str:
        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        # Process property_id as either a string or a list of strings
        if property_id:
            if isinstance(property_id, list):
                pid = ", ".join(property_id)
            else:
                pid = str(property_id)
        else:
            # Automatically create property_id if absent
            comp_reports = [
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("client_id")) == int(client_id)
            ]
            if comp_reports:
                comp_reports.sort(
                    key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                    reverse=True,
                )
                latest_report = comp_reports[0]
                pid = latest_report.get("subject_property_id", "HTX000")
            else:
                pid = "HTX000"

        # Automatically create subject and body_uri if they are absent
        if not subject or not body_uri:
            comp_reports = [
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("client_id")) == int(client_id)
            ]
            if comp_reports:
                comp_reports.sort(
                    key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                    reverse=True,
                )
                latest_report = comp_reports[0]
                report_status = latest_report.get("status", "draft")
            else:
                report_status = "draft"

            if not subject:
                if template_code == "open_house_summary":
                    subject = f"Open House Schedule for {pid}"
                elif template_code == "comp_report_delivery":
                    subject = f"Your comparable analysis for {pid} is complete"
                elif template_code == "report_followup":
                    subject = f"Follow-up on Your Property Analysis for {pid}"
                elif template_code == "briefing":
                    subject = "Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {pid}"
                elif template_code == "general_update":
                    subject = "Real Estate Market Update"
                elif template_code == "market_update":
                    subject = "Your Market Update"
                elif template_code == "investment_alert":
                    subject = "Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {pid}"
                elif template_code == "welcome_new_client":
                    subject = "Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = "Post-Closing Check-CO and Next Steps"
                elif template_code == "follow_up":
                    subject = "Following Up on Your Real Estate Needs"
                else:
                    # Backup logic determined by report status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {pid} is complete"
                    elif report_status == "ready_for_review":
                        subject = "Your comp report is ready for review"
                    elif report_status == "sent_to_broker":
                        subject = f"Comp report for {pid} sent to broker for review"
                    else:
                        subject = f"Market analysis update for {pid}"

            if not body_uri:
                if template_code == "open_house_summary":
                    body_uri = f"https://storage.example.com/emails/email_openhouse_{int(client_id):03d}.html"
                elif template_code == "comp_report_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif template_code == "report_followup":
                    body_uri = f"https://storage.example.com/emails/email_report_followup_{int(client_id):03d}.html"
                elif template_code == "briefing":
                    body_uri = f"https://storage.example.com/emails/email_briefing_{int(client_id):03d}.html"
                elif template_code == "first_time_buyer":
                    body_uri = f"https://storage.example.com/emails/email_first_buyer_{int(client_id):03d}.html"
                elif template_code == "general_update":
                    body_uri = f"https://storage.example.com/emails/email_general_{int(client_id):03d}.html"
                elif template_code == "market_update":
                    body_uri = f"https://storage.example.com/emails/email_market_{int(client_id):03d}.html"
                elif template_code == "investment_alert":
                    body_uri = f"https://storage.example.com/emails/email_investment_{int(client_id):03d}.html"
                elif template_code == "listing_summary":
                    body_uri = f"https://storage.example.com/emails/email_listing_{int(client_id):03d}.html"
                elif template_code == "welcome_new_client":
                    body_uri = f"https://storage.example.com/emails/email_welcome_{int(client_id):03d}.html"
                elif template_code == "post_closing_checkin":
                    body_uri = f"https://storage.example.com/emails/email_closing_{int(client_id):03d}.html"
                elif template_code == "follow_up":
                    body_uri = f"https://storage.example.com/emails/email_followup_{int(client_id):03d}.html"
                else:
                    # Revert to comp report format
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        # Generate Email Entry
        email_rows = data.setdefault("emails", [])
        email_id = _next_int_id(email_rows, "email_id")
        email_rec = {
            "email_id": email_id,
            "client_id": int(client_id),
            "broker_id": int(broker_id),
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": HARD_TS,
            "campaign_id": campaign_id,
        }
        email_rows.append(email_rec)

        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(broker_id),
            "action": "sent",
            "entity_type": "email",
            "entity_id": str(email_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"client_id": int(client_id), "template": template_code},
        }
        audit_rows.append(audit_rec)
        payload = {"email": email_rec, "audit_event": audit_rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": (
                    "Create an email entry with template-based subject/body defaults."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "template_code": {"type": "string"},
                        "subject": {"type": ["string", "null"]},
                        "body_uri": {"type": ["string", "null"]},
                        "campaign_id": {"type": ["integer", "null"]},
                        "property_id": {
                            "type": ["string", "array", "null"],
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["client_id", "broker_id", "template_code"],
                },
            },
        }
