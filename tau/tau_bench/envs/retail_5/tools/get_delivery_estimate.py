# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDeliveryEstimate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], destination_country, delivery_option = 'standard') -> str:

        if not destination_country:
            return json.dumps({'error': 'destination_country is required'})

        couriers = data['couriers']

        available_couriers = [c for c in couriers if destination_country in c['coverage_area']]

        if not available_couriers:
            return json.dumps({'error': f'No delivery available to {destination_country}'})

        delivery_estimates = {
            'express': {'min_days': 1, 'max_days': 3, 'cost_multiplier': 2.5},
            'standard': {'min_days': 3, 'max_days': 7, 'cost_multiplier': 1.0},
            'economy': {'min_days': 7, 'max_days': 14, 'cost_multiplier': 0.7}
        }

        estimate = delivery_estimates.get(delivery_option, delivery_estimates['standard'])

        return json.dumps({
            'destination_country': destination_country,
            'delivery_option': delivery_option,
            'estimated_days': f"{estimate['min_days']}-{estimate['max_days']}",
            'available_couriers': len(available_couriers),
            'cost_multiplier': estimate['cost_multiplier']
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_delivery_estimate',
                'description': 'Get delivery time estimates and available couriers for a destination.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'destination_country': {'type': 'string', 'description': 'Country to deliver to'},
                        'delivery_option': {'type': 'string', 'description': 'Delivery speed option', 'enum': ['express', 'standard', 'economy'], 'default': 'standard'}
                    },
                    'required': ['destination_country']
                }
            }
        }
