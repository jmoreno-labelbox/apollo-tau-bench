# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCourierInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        courier_id = kwargs.get('courier_id')
        tracking_id = kwargs.get('tracking_id')
        coverage_area = kwargs.get('coverage_area')

        couriers = data['couriers']

        if courier_id:
            courier = next((c for c in couriers if c['courier_id'] == courier_id), None)
            if not courier:
                return json.dumps({'error': 'Courier not found'})
            return json.dumps(courier, indent=2)

        if tracking_id:
            courier = next((c for c in couriers if tracking_id in c['tracking_ids']), None)
            if not courier:
                return json.dumps({'error': 'Courier not found for tracking ID'})
            return json.dumps({
                'courier_id': courier['courier_id'],
                'name': courier['name'],
                'contact_info': courier['contact_info']
            }, indent=2)

        if coverage_area:
            matching_couriers = []
            for courier in couriers:
                if coverage_area in courier['coverage_area']:
                    matching_couriers.append({
                        'courier_id': courier['courier_id'],
                        'name': courier['name'],
                        'coverage_area': courier['coverage_area']
                    })
            return json.dumps(matching_couriers, indent=2)

        return json.dumps({'error': 'courier_id, tracking_id, or coverage_area is required'})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_courier_info',
                'description': 'Get courier information by courier ID, tracking ID, or coverage area.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'courier_id': {'type': 'string', 'description': 'Courier ID to look up'},
                        'tracking_id': {'type': 'string', 'description': 'Tracking ID to find courier'},
                        'coverage_area': {'type': 'string', 'description': 'Geographic area to find couriers for'}
                    }
                }
            }
        }
