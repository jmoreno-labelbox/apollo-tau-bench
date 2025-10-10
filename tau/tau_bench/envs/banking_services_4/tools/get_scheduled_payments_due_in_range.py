# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScheduledPaymentsDueInRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        if not start_date or not end_date:
            return json.dumps({'error': 'start_date and end_date are required'})
        payments = load_json('scheduled_payments.json')
        results = []
        for p in payments:
            if p['status'] != 'Active':
                continue
            npd = p.get('next_payment_date')
            if npd and start_date <= npd <= end_date:
                results.append(p)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_scheduled_payments_due_in_range',
                'description': 'Returns all active scheduled payments that fall within a given date range.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'start_date': {'type': 'string', 'description': 'Start date (YYYY-MM-DD)'},
                        'end_date': {'type': 'string', 'description': 'End date (YYYY-MM-DD)'}
                    },
                    'required': ['start_date', 'end_date']
                }
            }
        }
