from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class FetchBeneficiariesByRelationship(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, relationship: str = None) -> str:
        if not customer_id or not relationship:
            return json.dumps({'error': 'customer_id and relationship are required'})
        beneficiaries = load_json('beneficiaries.json')
        filtered = [b for b in beneficiaries.values() if b['customer_id'] == customer_id and b['relationship'].lower() == relationship.lower()]
        return json.dumps(filtered, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'fetchBeneficiariesByRelationship',
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
