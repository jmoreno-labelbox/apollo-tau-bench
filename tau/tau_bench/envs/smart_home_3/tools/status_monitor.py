# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StatusMonitor(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category, report_type = 'summary') -> str:

        status = {}

        if report_type == 'summary' or not category:
            status['devices'] = {
                'total': len(list(data.get('devices', {}).values())),
                'by_type': {},
                'by_location': {},
                'powered_on': 0
            }

            for device in list(data.get('devices', {}).values()):
                device_type = device.get('type', 'unknown')
                location = device.get('location', 'unknown')
                status['devices']['by_type'][device_type] = status['devices']['by_type'].get(device_type, 0) + 1
                status['devices']['by_location'][location] = status['devices']['by_location'].get(location, 0) + 1
                if device.get('state', {}).get('power') == 'on':
                    status['devices']['powered_on'] += 1

            status['scenes'] = {'total': len(list(data.get('scenes', {}).values()))}
            status['lists'] = {'total': len(list(data.get('custom_lists', {}).values()))}
            status['reminders'] = {
                'total': len(list(data.get('reminders', {}).values())),
                'active': len([r for r in list(data.get('reminders', {}).values()) if r.get('status') == 'active'])
            }
            status['members'] = {
                'total': len(list(data.get('members', {}).values())),
                'residents': len([m for m in list(data.get('members', {}).values()) if m.get('residence', {}).get('lives_in_house')])
            }

        if category == 'devices' or report_type == 'detailed':
            devices = list(data.get('devices', {}).values())
            status['device_details'] = [
                {
                    'id': d['id'],
                    'type': d['type'],
                    'location': d['location'],
                    'power': d.get('state', {}).get('power', 'unknown'),
                    'last_updated': d.get('state', {}).get('last_updated')
                } for d in devices
            ]

        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "status_monitor",
                "description": "Get system status and analytics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["summary", "detailed"], "description": "Type of report"},
                        "category": {"type": "string", "enum": ["devices", "scenes", "lists", "reminders", "members"], "description": "Focus on specific category"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
