# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLicenseInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_name) -> str:
        if license_name is None:
            return json.dumps({'status': 'error', 'reason': 'The license_name field is required.'}, indent=2)

        inventory = data.get('license_inventory')
        assignments = data.get('license_assignments')

        for license in inventory:
            if license['name'] == license_name:
                assigned_licenses = []
                for assignment in assignments:
                    if assignment['license_id'] == license['license_id']:
                        assigned_licenses.append(assignment)
                license_overview = {
                    'info': license,
                    'assignments': assigned_licenses
                }
                return json.dumps(license_overview, indent=2)

        return json.dumps({'status': 'error', 'reason': 'Could not find specified license.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_license_info',
                'description': 'Gets all info associated with a specific license.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'license_name': {'type': 'string', 'description': 'The name of the license.'},
                    },
                    'required': ['license_name']
                }
            }
        }
