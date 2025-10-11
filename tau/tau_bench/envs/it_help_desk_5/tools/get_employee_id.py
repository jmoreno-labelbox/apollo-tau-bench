# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name, last_name) -> str:

        if first_name is None or last_name is None:
            return json.dumps({'error': 'first_name and last_name are required.'}, indent=2)

        employees = list(data.get('employees', {}).values())

        for employee in employees:
            if employee['first_name'] == first_name and employee['last_name'] == last_name:
                return json.dumps(employee['employee_id'], indent=2)
        return json.dumps({'status': 'error', 'reason': f'Employee {first_name} {last_name} not found.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_employee_id',
                'description': "Finds an employee's id using their first name and last name.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'first_name': {'type': 'string', 'description': 'The first name of the employee to search for.'},
                        'last_name': {'type': 'string', 'description': 'The last name of the employee to search for.'},
                    },
                    'required': ['first_name', 'last_name']
                }
            }
        }
