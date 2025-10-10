# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if employee_id is None:
            return json.dumps({'status': 'error', 'reason': 'The employee_id field is required.'}, indent=2)

        employees = list(data.get('employees', {}).values())

        for employee in employees:
            if employee['employee_id'] == employee_id:
                return json.dumps(employee)
        return json.dumps({'status': 'error', 'reason': 'Employee not found.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_employee_info',
                'description': "Finds an employee's info using their id.",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to search for.'},
                    },
                    'required': ['employee_id']
                }
            }
        }
