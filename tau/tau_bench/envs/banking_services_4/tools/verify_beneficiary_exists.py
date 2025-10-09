from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class VerifyBeneficiaryExists(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None) -> str:
        if not beneficiary_id:
            return json.dumps({'error': 'beneficiary_id is required'})
        beneficiaries = load_json('beneficiaries.json')
        beneficiary = next((b for b in beneficiaries if b['beneficiary_id'] == beneficiary_id), None)
        if not beneficiary:
            return json.dumps({'error': 'Beneficiary not found.'})
        return json.dumps(beneficiary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'verifyBeneficiaryExists',
                'description': 'Verifies a beneficiary exists by their ID and returns their details.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'beneficiary_id': {'type': 'string', 'description': 'Beneficiary ID to verify'}
                    },
                    'required': ['beneficiary_id']
                }
            }
        }
