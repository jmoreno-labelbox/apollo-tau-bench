# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        utilization = kwargs.get('utilization')

        if all([param == None for param in [utilization]]):
            return json.dumps({'status': 'error', 'reason': 'Input parameters to filter by are required.'}, indent=2)

        licenses = data.get('license_inventory')
        filtered_licenses = []

        for license in licenses:
            util = (license['used_seats'] + license['reserved_seats'])/license['total_seats']
            if util < utilization:
                filtered_licenses.append(license['license_id'])

        return json.dumps(filtered_licenses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'filter_licenses',
                'description': 'Reterns the licenses that match input criteria.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'utilization': {'type': 'float', 'description': 'Filters liceses by utilization.'},
                    },
                }
            }
        }
