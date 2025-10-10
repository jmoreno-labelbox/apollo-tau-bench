# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateHubspotTicket(Tool):
    """ Create a new ticket in the HubSpot system for tracking. """

    @staticmethod
    def invoke(data: Dict[str, Any], assignee_id, category, description, priority, requester_id, subject, timestamp) -> str:
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        existing_ids = [int(item["ticket_id"].replace("TI-", "")) for item in hubspot_tickets if
                        item.get("ticket_id", "").startswith("TI-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        ticket_id = f"TI-{next_id_num:03d}"

        new_ticket = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp, 
            "subject": subject,
            "description": description,
            "status": "OPEN",
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
            "closed_at": None
        }

        hubspot_tickets.append(new_ticket)
        data['hubspot_tickets'] = hubspot_tickets

        return json.dumps({
            "message": "HubSpot ticket created successfully.",
            "ticket_details": new_ticket
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Creates a new ticket in the HubSpot system to track an incident or request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string", "description": "The title or subject line of the ticket."},
                        "description": {"type": "string",
                                        "description": "A detailed description of the issue or event."},
                        "priority": {"type": "string",
                                     "description": "The priority level of the ticket (e.g., HIGH, MEDIUM, LOW)."},
                        "assignee_id": {"type": "string",
                                        "description": "The user ID of the person the ticket is assigned to."},
                        "requester_id": {"type": "string",
                                         "description": "The user ID of the person who initiated the event or request."},
                        "category": {"type": "string",
                                     "description": "The category of the ticket (e.g., SECURITY_INCIDENT, ACCESS_REQUEST)."},
                        "timestamp": {"type": "string", "description": "The current timestamp for the creation record."}
                    },
                    "required": ["subject", "description", "priority", "assignee_id", "requester_id", "category",
                                 "timestamp"]
                }
            }
        }
