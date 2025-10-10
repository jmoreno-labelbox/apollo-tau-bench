# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = data.get('license_inventory')

        license_id = kwargs.get('license_id')
        if license_id is None:
            return json.dumps({'status': 'error', 'reason': 'The license_id field is required.'}, indent=2)

        for license in inventory:
            if license['license_id'] == license_id:
                if license['total_seats'] - license['reserved_seats'] - license['used_seats'] > 0:
                    return json.dumps({'available': True}, indent=2)
                else:
                    return json.dumps({'available': False}, indent=2)

        return json.dumps({'status': 'error', 'reason': f'License {license_id} not found'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_license_availability',
                'description': 'Checks if a license with a designated id is available.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'license_id': {'type': 'string', 'description': 'The id of the license to search for.'}
                    },
                }
            }
        }
