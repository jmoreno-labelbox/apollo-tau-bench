# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignAppAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], app_id, employee_id) -> str:

        if employee_id is None or app_id is None:
            return json.dumps({'status': 'error', 'description': 'The employee_id and app_id fields are required.'}, indent=2)

        accounts = data.get('app_accounts')

        new_account = {
                "app_account_id": "appacc_000000",
                "employee_id": employee_id,
                "app_id": app_id,
                "status": "active",
                "created_at": FIXED_NOW
        }

        accounts.append(new_account)

        return json.dumps({'status': 'ok', 'description': f'Added {app_id} account for {employee_id}'}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'assign_app_account',
                'description': 'Assigns an app to a user by appending to the app_accounts database.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to assign licenses to.'},
                        'app_id': {'type': 'string', 'description': 'The id of the app to assign.'}
                    },
                    'required': ['employee_id', 'app_id']
                }
            }
        }
