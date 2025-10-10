# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPaymentScheduleForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        payments = load_json('scheduled_payments.json')
        filtered = [p for p in payments if p['source_account_id'] == account_id]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_payment_schedule_for_account',
                'description': 'Returns all recurring payment details for a specific account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }
