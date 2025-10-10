# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get('employee_id')
        status = kwargs.get('status')

        if employee_id is None:
            return json.dumps({'status': 'error', 'description': 'The employee_id field is required.'}, indent=2)

        if all([param is None for param in [status]]):
            return json.dumps({'status': 'error', 'description': 'At least one parameter to be changed is required.'}, indent=2)

        directory_accounts = data.get('directory_accounts')

        for account in directory_accounts:
            if account['employee_id'] == employee_id:
                if status is not None:
                    account['status'] = status
                    if status == 'disabled':
                        account['disabled_at'] = FIXED_NOW

        return json.dumps({'status': 'ok', 'description': f'Successfully updated account for {employee_id}.'})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_directory_account',
                'description': 'Allows updates for directory accounts, including disabling accounts.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to update.'},
                        'status': {'type': 'string', 'description': 'The status to set.'}
                    },
                    'required': ['employee_id']
                }
            }
        }
