# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UnassignLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, license_ids = []) -> str:
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)
        assignments = data.get('license_assignments')
        inventory = data.get('license_inventory')

        for assignment in assignments:
            if assignment['employee_id'] == employee_id and (len(license_ids) == 0 or assignment['license_id'] in license_ids):
                assignment['status'] = 'inactive'
                license_ids.append(assignment['license_id'])

        license_ids = set(license_ids)

        for license in inventory:
            if license['license_id'] in license_ids:
                license['used_seats'] -= 1

        return json.dumps({'status': 'ok', 'reason': f'Licenses successfully removed for {employee_id}'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'unassign_licenses',
                'description': 'Unssigns licenses from an employee and updates license_inventory. Takes the employee_id and license_ids as input. If no license_ids are supplied, removes all licenses from the employee.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee.'},
                        'license_ids': {'type': 'array', 'items':{'type': 'string'}, 'description': 'A list of license ids to unassign from the employee.'},
                    },
                    'required': ['employee_id']
                }
            }
        }
