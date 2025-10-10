# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLicenseAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        license_id = kwargs.get('license_id')
        if license_id is None:
            return json.dumps({'status': 'error', 'description': 'The license_id field is required.'}, indent=2)

        inventory = data.get('license_inventory')

        for license in inventory:
            if license['license_id'] == license_id:
                license['last_audit_at'] = FIXED_NOW

                return json.dumps({'status': 'ok', 'description': f'Successfully updated {license_id}.'}, indent=2)

        return json.dumps({'status': 'error', 'description': f'Unable to find {license_id}.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_license_audit',
                'description': "Updates a liscense's audit date",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'license_id': {'type': 'string', 'description': 'The license to update.'},
                    },
                    'required': ['license_id']
                }
            }
        }
