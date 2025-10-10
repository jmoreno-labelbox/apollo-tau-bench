# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TicketStatistics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        field = kwargs.get('field')
        stat_type = kwargs.get('type')

        if field is None or stat_type is None:
            return json.dumps({'status': 'error', 'reason': 'The field and type parameters are required.'}, indent=2)

        if field not in ['tickets_opened', 'tickets_closed', 'closed_within_24h', 'avg_open_age_hours']:
            return json.dumps({'status': 'error', 'reason': 'The specified field could not be found in daily_metrics.'}, indent=2)

        if stat_type not in ['avg', 'sum']:
            return json.dumps({'status': 'error', 'reason': 'Unknown statistic type.'}, indent=2)

        daily_metrics = data.get('daily_metrics')

        pulled_data = []
        for metrics in daily_metrics:
            pulled_data.append(metrics[field])

        if stat_type == 'sum':
            return json.dumps({'result': sum(pulled_data)})
        elif stat_type == 'avg':
            return json.dumps({'result': sum(pulled_data)/len(pulled_data)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'ticket_statistics',
                'description': 'Calculates various statistics for ticket.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'field': {'type': 'string', 'description': 'The field in daily_metrics to target.'},
                        'type': {'type': 'string', 'description': 'The type of statistic to produce.'},
                    },
                    'required': ['field', 'type']
                }
            }
        }
