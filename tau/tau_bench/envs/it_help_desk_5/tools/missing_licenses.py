# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MissingLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get('employee_id')
        job_title = kwargs.get('job_title')
        if employee_id is None or job_title is None:
            return json.dumps({'status': 'error', 'description': 'The employee_id and job_title fields are required.'}, indent=2)


        employee_licenses = []
        license_assignments = data.get('license_assignments', [])

        for assignment in license_assignments:
            if assignment['employee_id'] == employee_id:
                employee_licenses.append(assignment['license_id'])


        group_map = data.get('rbac_group_map')
        missing = []

        for group in group_map:
            if group['job_title'] == job_title:
                licenses = group['default_license_bundle']
                for license in licenses:
                    if license not in employee_licenses:
                        missing.append(license)
                return json.dumps(missing, indent=2)
        return json.dumps({'status': 'error', 'description': 'Unable to find specified job_title.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'missing_licenses',
                'description': "Finds any licenses a job's default licenses from the rbac_group_map database that are not assigned to an employee.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The employee to verify licenses for.'},
                        'job_title':{'type': 'string', 'description': 'The job title to compare licenses against.'},
                    },
                    'required': ['employee_id', 'job_title']
                }
            }
        }
