# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)

        license_assignments = data.get('license_assignments', [])
        licenses = []

        for assignment in license_assignments:
            if assignment['employee_id'] == employee_id:
                licenses.append(assignment['license_id'])
        return json.dumps(licenses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_employee_licenses',
                'description': 'Finds licenses associated with a specified employee.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to search for.'},
                    },
                    'required': ['employee_id']
                }
            }
        }
