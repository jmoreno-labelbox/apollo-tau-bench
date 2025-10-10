# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTicketInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get('ticket_id')
        if ticket_id is None:
            return json.dumps({'status': 'error', 'description': 'The ticket_id field is required.'}, indent=2)

        tickets = data.get('tickets')

        for ticket in tickets:
            if ticket['ticket_id'] == ticket_id:
                return json.dumps(ticket, indent=2)
        return json.dumps({'status': 'error', 'description': 'The ticket was not found.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_ticket_info',
                'description': 'Gets info for a ticket based on ticket_id.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'ticket_id': {'type': 'string', 'description': 'The id of the ticket to search for.'},
                    },
                    'required': ['ticket_id']
                }
            }
        }
