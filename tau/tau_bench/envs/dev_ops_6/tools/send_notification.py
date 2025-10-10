# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNotification(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], id, metadata, read_at, channel = 'slack', message = '', notification_type = 'info', project_id = 'project_001', recipient_id = 'user_000', sent_at = FIXED_TS, title = '') -> str:
        notifications = _table(data, 'notifications')
        nid = id
        # --- SOLUTION: Create ID if absent ---
        if not nid:
            nid = f"notification_{len(notifications) + 1:04d}"

        if any((n.get('id') == nid for n in notifications)):
            return _err(f'notification id {nid} already exists')
        record = {'id': nid, 'project_id': project_id, 'notification_type': notification_type, 'title': title, 'message': message, 'recipient_id': recipient_id, 'channel': channel, 'sent_at': sent_at, 'read_at': read_at}
        if not record['message']:
            return _err('message must be non-empty')
        md = metadata
        if md is not None:
            record['metadata'] = md
        notifications.append(record)
        return _ok({'notification': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'send_notification', 'description': 'Record a notification (deterministic timestamp). Optionally include CI/linkage metadata.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'project_id': {'type': 'string'}, 'notification_type': {'type': 'string'}, 'title': {'type': 'string'}, 'message': {'type': 'string'}, 'recipient_id': {'type': 'string'}, 'channel': {'type': 'string'}, 'sent_at': {'type': 'string'}, 'read_at': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['message']}}}
