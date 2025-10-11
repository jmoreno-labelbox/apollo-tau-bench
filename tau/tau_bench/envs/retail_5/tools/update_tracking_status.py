# Copyright Sierra

import json
import os
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool

# Note: DATA_DIR and load_json are no longer used by the invoke methods,
# which is the correct architecture. They are left here in case they are
# used by other parts of the framework not provided.
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

def get_current_timestamp() -> str:
    # Deterministic timestamp as per requirements
    return "2025-08-12T12:00:00.000000"

def generate_unique_id() -> str:
    # Deterministic ID as per requirements
    return 'fd520c73'


class UpdateTrackingStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], status, tracking_id) -> str:

        if not tracking_id or not status:
            return json.dumps({'error': 'tracking_id and status are required'})

        tracking_data = data['tracking']
        tracking_info = next((t for t in tracking_data if tracking_id in t['tracking_id']), None)

        if not tracking_info:
            return json.dumps({'error': 'Tracking information not found'})

        if 'tracking_history' not in tracking_info:
            tracking_info['tracking_history'] = {}

        tracking_info['tracking_history'][status] = get_current_timestamp()

        return json.dumps({
            'success': True,
            'tracking_id': tracking_id,
            'new_status': status,
            'updated_at': get_current_timestamp(),
            'tracking_history': tracking_info['tracking_history']
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_tracking_status',
                'description': 'Update the tracking status of a shipment.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'tracking_id': {'type': 'string', 'description': 'Tracking ID to update'},
                        'status': {'type': 'string', 'description': 'New tracking status (e.g., in_transit, delivered)'}
                    },
                    'required': ['tracking_id', 'status']
                }
            }
        }
