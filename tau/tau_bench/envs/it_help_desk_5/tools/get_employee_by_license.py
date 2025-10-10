# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeByLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        license_id = kwargs.get('license_id')
        status = kwargs.get('status')
        if license_id is None or status is None:
            return json.dumps({'status': 'error', 'reason': 'The license_id and status fields are required.'}, indent=2)

        license_assignments = data.get('license_assignments')

        assignment_data = []

        for license in license_assignments:
            if license['license_id'] == license_id and license['status'] == status:
                assignment_data.append(license['employee_id'])

        return json.dumps(assignment_data, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_employee_by_license',
                'description': 'Returns the employees with licenses and statuses that match status.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'license_id': {'type': 'string', 'description': 'The license to filter by.'},
                        'status': {'type': 'string', 'desctiption': 'The status of the license to filter by.'}
                    },
                    'required': ['license_id', 'status']
                }
            }
        }
