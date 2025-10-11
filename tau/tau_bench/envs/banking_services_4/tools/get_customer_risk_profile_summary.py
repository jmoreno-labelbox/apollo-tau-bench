from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class GetCustomerRiskProfileSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        customers = load_json('customers.json')
        customer = next((c for c in customers.values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({'error': 'Customer not found'})
        summary = {
            'aml_risk_level': customer.get('compliance', {}).values().get('aml_risk_level'),
            'credit_score': customer.get('financial_profile', {}).values().get('credit_score'),
            'kyc_status': customer.get('compliance', {}).values().get('kyc_status')
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerRiskProfileSummary',
                'description': 'Retrieves AML risk level, credit score, and KYC status.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }
