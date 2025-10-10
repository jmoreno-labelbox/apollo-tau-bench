# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeviceAssignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get('employee_id')
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)

        assets = data.get('it_assets')
        unassign = kwargs.get('unassign')
        assigned_assets = []

        for asset in assets:
            if asset['assigned_to'] == employee_id:
                if unassign:
                    asset['status'] = 'in_stock'
                    asset['assigned_to'] = None
                assigned_assets.append(asset)

        if unassign:
            return json.dumps({'status': 'ok', 'reason': f'Successfully unassigned all devices from {employee_id}.'}, indent=2)
        else:
            return json.dumps(assigned_assets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'device_assignment',
                'description': 'Updates or returns a list of devices assigned to an employee',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee.'},
                        'unassign': {'type': 'boolean', 'description': 'Whether to unassign devices.'}
                    },
                    'required': ['employee_id']
                }
            }
        }
