# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSupportTicketForTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        transaction_id = kwargs.get('transaction_id')
        reason = kwargs.get('reason')
        if not customer_id or not transaction_id or not reason:
            return json.dumps({'error': 'customer_id, transaction_id, and reason are required'})

        # This function would ideally append to the support_tickets.json file,
        # but here we just simulate the creation for demonstration.
        new_ticket = {
            "ticket_id": f"tkt_{generate_unique_id()}",
            "customer_id": customer_id,
            "status": "Open",
            "priority": "High",
            "channel": "System",
            "category": "Transaction Inquiry",
            "request_details": {
                "target_entity": "Transaction",
                "target_id": transaction_id,
                "operation": "INVESTIGATE",
                "parameters": { "reason": reason }
            }
        }
        return json.dumps({'success': True, 'ticket_created': new_ticket}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_support_ticket_for_transaction',
                'description': 'Creates a high-priority support ticket to investigate a transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer reporting the issue.'},
                        'transaction_id': {'type': 'string', 'description': 'The ID of the transaction to be investigated.'},
                        'reason': {'type': 'string', 'description': 'The reason for creating the support ticket.'}
                    },
                    'required': ['customer_id', 'transaction_id', 'reason']
                }
            }
        }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_support_ticket_for_transaction',
                'description': 'Creates a high-priority support ticket to investigate a transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer reporting the issue.'
                        },
                        'transaction_id': {
                            'type': 'string',
                            'description': 'The ID of the transaction to be investigated.'
                        },
                        'reason': {
                            'type': 'string',
                            'description': 'The reason for creating the support ticket.'
                        }
                    },
                    'required': ['customer_id', 'transaction_id', 'reason']
                }
            }
        }
