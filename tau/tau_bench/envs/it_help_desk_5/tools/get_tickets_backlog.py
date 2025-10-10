# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTicketsBacklog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snapshot_id = kwargs.get('snapshot_id')

        snapshots = data.get('backlog_snapshot_open')

        if snapshot_id is None:
            if len(snapshots) > 0:
                target_snapshot = snapshots[-1]
            else:
                return json.dumps({'status': 'error', 'description': 'The snapshot could not be found.'}, indent=2)
        else:
            for snapshot in snapshots:
                if snapshot['snapshot_id'] == snapshot_id:
                    target_snapshot = snapshot
            if target_snapshot is None:
                return json.dumps({'status': 'error', 'description': 'The snapshot could not be found.'}, indent=2)

        return json.dumps(target_snapshot['open_ticket_ids'], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_tickets_backlog',
                'description': 'Gets a list of tickets from a snapshot, the default being the last snapshot.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'snapshot_id': {'type': 'string', 'description': 'The id of the snapshot to look for.'},
                    },
                }
            }
        }
