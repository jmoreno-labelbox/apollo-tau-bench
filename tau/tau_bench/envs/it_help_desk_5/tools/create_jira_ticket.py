# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], issue_type, priority, summary) -> str:
        jira_tickets = data.get('jira_tickets')

        if len(jira_tickets) > 0:
            last_jira_id = jira_tickets[-1]['jira_id']
        else:
            last_jira_id = 'ITSD-1000'

        id_components = last_jira_id.split('-')
        new_jira_id = f'{id_components[0]}-{str(int(id_components[1])+1).zfill(4)}'
        if issue_type is None:
            return json.dumps({'status': 'error', 'reason': 'issue_type parameter is required'}, indent=2)
        if summary is None:
            return json.dumps({'status': 'error', 'reason': 'summary parameter is required'}, indent=2)
        if priority is None:
            return json.dumps({'status': 'error', 'reason': 'priority parameter is required'}, indent=2)

        new_jira_ticket = {
            "jira_id": new_jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": "To Do",
            "created_at": "2025-07-10T13:00:00+00:00",
            "updated_at": "2025-07-14T15:30:00+00:00"
        }

        jira_tickets.append(new_jira_ticket)

        return json.dumps({'status': 'ok', 'reason': f'Successfully created a new Jira ticket {new_jira_id}.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_jira_ticket',
                'description': 'Creates a new Jira ticket.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'issue_type': {'type': 'string', 'description': 'The type of issue to assign to the Jira ticket'},
                        'summary': {'type': 'string', 'description': 'A description of the issue.'},
                        'priority': {'type': 'string', 'description': 'The priority of the issue.'}
                    },
                    'required': ['issue_type', 'summary', 'priority']
                }
            }
        }
