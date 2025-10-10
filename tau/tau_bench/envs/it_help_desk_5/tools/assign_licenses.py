# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get('employee_id')
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)

        licenses = set()

        license_assignments = data.get('license_assignments', [])
        for assignment in license_assignments:
            if assignment['employee_id'] == employee_id:
                licenses.add(assignment['license_id'])

        group_map = data.get('rbac_group_map', [])
        job_title = kwargs.get('job_title')
        if job_title is None:
            for group in group_map:
                if group['job_title'] == job_title:
                    for license in group['default_license_bundle']:
                        licenses.add(license)

        inventory = data.get('license_inventory')

        for license in inventory:
            if license['license_id'] in licenses:
                license['used_seats'] += 1
                last_id = license_assignments[-1]['assignment_id']
                last_id = last_id.split('_')
                new_id_num = str(int(last_id[1])).zfill(4)
                new_license_assignment = {
                        "assignment_id": f'{last_id[0]}_{new_id_num}',
                        "account_id": "acc_000000", #Assign a unique account id for each user
                        "employee_id": "emp_0001",
                        "license_id": employee_id,
                        "status": "active",
                        "assigned_at": FIXED_NOW
                }
                license_assignments.append(new_license_assignment)

        return json.dumps({'status': 'ok', 'reason': f'Licenses successfully added for {employee_id}.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'assign_licenses',
                'description': 'Assigns licenses in the rbac_group_map or licenses provided to an employee, verifying license availability before assignment. Takes the employee_id as input as well as license_ids and or job_title.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee.'},
                        'license_ids': {'type': 'array', 'items':{'type': 'string'}, 'description': 'A list of license ids to assign to the employee.'},
                        'job_title': {'type': 'string', 'description': 'The job title to assign default licenses from.'}
                    },
                    'required': ['employee_id']
                }
            }
        }
