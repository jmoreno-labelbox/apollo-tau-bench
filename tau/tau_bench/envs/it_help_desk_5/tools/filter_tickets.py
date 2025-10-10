# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = kwargs.get('ids',[])
        status = kwargs.get('status')
        not_status = kwargs.get('not_status')

        if len(ids) == 0 and all([param is None for param in [status, not_status]]):
            return json.dumps({'status': 'error', 'description': 'Input parameters to search for are required.'}, indent=2)

        tickets = data.get('tickets')
        temp_tickets = tickets.copy()

        if len(ids) != 0:
            temp_tickets = [ticket for ticket in temp_tickets if ticket['ticket_id'] in ids]
        if status is not None:
            temp_tickets = [ticket for ticket in temp_tickets if ticket['status'] == status]
        if not_status is not None:
            temp_tickets = [ticket for ticket in temp_tickets if ticket['status'] != not_status]

        return json.dumps(temp_tickets, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'filter_tickets',
                'description': 'Filters tickets by input criteria.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'An array of ticket ids to search for.'},
                        'status': {'type': 'string', 'description': 'A status to search for.'},
                        'not_status': {'type': 'string', 'description': 'A status to exclude from search results.'}
                    },
                }
            }
        }
