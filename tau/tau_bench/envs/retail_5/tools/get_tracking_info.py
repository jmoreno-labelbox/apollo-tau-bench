# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTrackingInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id, tracking_id) -> str:

        if not tracking_id and not order_id:
            return json.dumps({'error': 'Either tracking_id or order_id is required'})

        tracking_data = data['tracking']

        if tracking_id:
            tracking_info = next((t for t in tracking_data if tracking_id in t['tracking_id']), None)
        else:
            tracking_info = next((t for t in tracking_data if t['order_id'] == order_id), None)

        if not tracking_info:
            return json.dumps({'error': 'Tracking information not found'})

        return json.dumps(tracking_info, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_tracking_info',
                'description': 'Get tracking information for an order by tracking ID or order ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'tracking_id': {'type': 'string', 'description': 'Tracking ID to look up'},
                        'order_id': {'type': 'string', 'description': 'Order ID to get tracking for'}
                    }
                }
            }
        }
