# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MailboxExists(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)

        employees = list(data.get('employees', {}).values())

        for employee in employees:
            if employee['employee_id'] == employee_id:
                return json.dumps({'mailbox_exists': True}, indent=2)
        return json.dumps({'mailbox_exists': False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'mailbox_exists',
                'description': 'Determines whether or not an employee mailbox exists.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to search for.'},
                    },
                    'required': ['employee_id']
                }
            }
        }
