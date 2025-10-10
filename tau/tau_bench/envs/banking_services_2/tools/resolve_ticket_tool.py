# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp


class ResolveTicketTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], resolution, ticket_id, agent_id = 'SYSTEM') -> str:

        support_tickets = list(data.get('support_tickets', {}).values())

        for ticket in support_tickets:
            if ticket['ticket_id'] == ticket_id:
                ticket['status'] = 'Resolved'
                ticket['resolution'] = resolution
                ticket['assigned_agent'] = agent_id
                ticket['resolved_date'] = get_current_timestamp()

                return json.dumps({
                    "ticket_id": ticket_id,
                    "status": "Resolved",
                    "resolution": resolution,
                    "resolved_by": agent_id,
                    "resolved_date": ticket['resolved_date']
                }, indent=2)

        return json.dumps({"error": f"Ticket {ticket_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_ticket",
                "description": "Resolve a customer support ticket",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Ticket identifier"},
                        "resolution": {"type": "string", "description": "Resolution description"},
                        "agent_id": {"type": "string", "description": "Agent resolving the ticket"}
                    },
                    "required": ["ticket_id", "resolution"]
                }
            }
        }
