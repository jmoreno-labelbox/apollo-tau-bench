# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateEmailEntryTool(Tool):
    """Creates an entry in the emails table and an accompanying audit event."""

    @staticmethod
    def invoke(data: Dict[str, Any], body_uri, broker_id, campaign_id, client_id, subject, template_code) -> str:

        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        # --- Automatically create subject and body_uri if they are not supplied ---
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
                report_id = latest_report.get("report_id")
                subject_property = latest_report.get("subject_property_id", "HTX000")
            else:
                report_status, report_id, subject_property = "draft", None, "HTX000"

            if not subject:
                if template_code == "open_house_summary":
                    subject = f"Open House Schedule for {subject_property}"
                elif template_code == "comp_report_delivery":
                    subject = (
                        f"Your comparable analysis for {subject_property} is complete"
                    )
                elif template_code == "report_followup":
                    subject = (
                        f"Follow-up on Your Property Analysis for {subject_property}"
                    )
                elif template_code == "briefing_followup":
                    subject = f"Follow-up on Your Client Briefing"
                elif template_code == "briefing_delivery":
                    subject = f"Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {subject_property}"
                elif template_code == "general_update":
                    subject = f"Real Estate Market Update"
                elif template_code == "market_update":
                    subject = f"Your Market Update"
                elif template_code == "investment_alert":
                    subject = f"Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {subject_property}"
                elif template_code == "welcome_new_client":
                    subject = f"Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = f"Post-Closing Check-in and Next Steps"
                elif template_code == "next_steps":
                    subject = f"Next Steps in Your Real Estate Journey"
                elif template_code == "follow_up":
                    subject = f"Following Up on Your Real Estate Needs"
                else:
                    # Alternative logic depending on the report's status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {subject_property} is complete"
                    elif report_status == "ready_for_review":
                        subject = f"Your comp report is ready for review"
                    elif report_status == "sent_to_broker":
                        subject = f"Comp report for {subject_property} sent to broker for review"
                    else:
                        subject = f"Market analysis update for {subject_property}"

            if not body_uri:
                if template_code == "open_house_summary":
                    body_uri = f"https://storage.example.com/emails/email_openhouse_{int(client_id):03d}.html"
                elif template_code == "comp_report_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif template_code == "report_followup":
                    body_uri = f"https://storage.example.com/emails/email_report_followup_{int(client_id):03d}.html"
                elif template_code == "briefing_followup":
                    body_uri = f"https://storage.example.com/emails/email_briefing_followup_{int(client_id):03d}.html"
                elif template_code == "briefing_delivery":
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
                elif template_code == "next_steps":
                    body_uri = f"https://storage.example.com/emails/email_next_steps_{int(client_id):03d}.html"
                elif template_code == "follow_up":
                    body_uri = f"https://storage.example.com/emails/email_followup_{int(client_id):03d}.html"
                elif template_code == "urgent_comp_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif report_id:
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(report_id):03d}.html"
                else:
                    # Set to the default configuration for the comparison report format.
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        # --- Generate Email Record ---
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

        # --- Generate Audit Log Entry ---
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

        return json.dumps({"email": email_rec, "audit_event": audit_rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_email_entry",
                "description": (
                    "Creates an entry in the emails table and a corresponding audit event for compliance."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "subject": {
                            "type": "string",
                            "description": (
                                "Optional - auto-generated based on comp report status if not provided"
                            ),
                        },
                        "body_uri": {
                            "type": "string",
                            "description": (
                                "Optional - auto-generated based on comp report status if not provided"
                            ),
                        },
                        "template_code": {"type": "string"},
                        "campaign_id": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id", "broker_id", "template_code"],
                },
            },
        }
