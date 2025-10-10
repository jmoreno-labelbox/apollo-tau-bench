# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_type, employee_id) -> str:
        if employee_id is None or asset_type is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id and asset_type fields are required.'}, indent=2)

        assets = data.get('it_assets')

        for asset in assets:
            if asset['asset_type'] == asset_type and asset['status'] == 'in_stock':
                asset['status'] = 'assigned'
                asset['assigned_to'] = employee_id
                return json.dumps({'status': 'ok', 'device': asset}, indent=2)

        return json.dumps({'status': 'error', 'description': 'Unable to find available asset.'})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'assign_device',
                'description': 'Assigns an employee a device of a specified type.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee.'},
                        'asset_type': {'type': 'string', 'description': 'The type of asset to assign to an employee.'}
                    },
                    'required': ['employee_id', 'asset_type']
                }
            }
        }
