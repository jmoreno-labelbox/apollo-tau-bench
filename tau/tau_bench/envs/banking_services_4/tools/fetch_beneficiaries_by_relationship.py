# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchBeneficiariesByRelationship(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        relationship = kwargs.get('relationship')
        if not customer_id or not relationship:
            return json.dumps({'error': 'customer_id and relationship are required'})
        beneficiaries = load_json('beneficiaries.json')
        filtered = [b for b in beneficiaries if b['customer_id'] == customer_id and b['relationship'].lower() == relationship.lower()]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'fetch_beneficiaries_by_relationship',
                'description': 'Returns beneficiaries based on relationship type (e.g., "Friend", "Family").',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'relationship': {'type': 'string', 'description': 'Relationship type (e.g., Friend, Family, etc.)'}
                    },
                    'required': ['customer_id', 'relationship']
                }
            }
        }
