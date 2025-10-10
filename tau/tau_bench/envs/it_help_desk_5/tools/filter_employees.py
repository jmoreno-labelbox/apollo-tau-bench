# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get('employees')

        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        department = kwargs.get('department')
        job_title = kwargs.get('job_title')
        manager = kwargs.get('manager_id')
        status = kwargs.get('status')

        if all([attribute == None for attribute in [first_name, last_name, department, job_title, manager, status]]):
            return json.dumps({'status': 'error', 'reason': 'No criteria specified'}, indent=2)

        temp_employees = employees.copy()

        if first_name is not None:
            temp_employees = [employee for employee in temp_employees if employee['first_name'] == first_name]

        if last_name is not None:
            temp_employees = [employee for employee in temp_employees if employee['last_name'] == last_name]

        if department is not None:
            temp_employees = [employee for employee in temp_employees if employee['department'] == department]

        if job_title is not None:
            temp_employees = [employee for employee in temp_employees if employee['job_title'] == job_title]

        if manager is not None and manager != 'None':
            temp_employees = [employee for employee in temp_employees if employee['manager_id'] == manager]

        if manager is not None and manager == 'None':
            temp_employees = [employee for employee in temp_employees if employee['manager_id'] is None]

        if status is not None:
            temp_employees = [employee for employee in temp_employees if employee['status'] == status]

        return json.dumps(temp_employees, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'filter_employees',
                'description': 'Finds employees based on certain criteria.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'first_name': {'type': 'string', 'description': 'The first name to search for.'},
                        'last_name': {'type': 'string', 'description': 'The last name to search for.'},
                        'department': {'type': 'string', 'description': 'The department to search for.'},
                        'job_title': {'type': 'string', 'description': 'The job title to search for.'},
                        'manager_id': {'type': 'string', 'description': 'The manager to search for.'},
                        'status': {'type': 'string', 'description': 'The status to search for.'},
                    },
                }
            }
        }
