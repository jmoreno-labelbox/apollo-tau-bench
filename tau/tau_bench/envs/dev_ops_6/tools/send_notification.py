# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNotification(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notifications = _table(data, 'notifications')
        nid = kwargs.get('id')
        # --- FIX: Generate ID if not provided ---
        if not nid:
            nid = f"notification_{len(notifications) + 1:04d}"

        if any((n.get('id') == nid for n in notifications)):
            return _err(f'notification id {nid} already exists')
        record = {'id': nid, 'project_id': kwargs.get('project_id', 'project_001'), 'notification_type': kwargs.get('notification_type', 'info'), 'title': kwargs.get('title', ''), 'message': kwargs.get('message', ''), 'recipient_id': kwargs.get('recipient_id', 'user_000'), 'channel': kwargs.get('channel', 'slack'), 'sent_at': kwargs.get('sent_at', FIXED_TS), 'read_at': kwargs.get('read_at')}
        if not record['message']:
            return _err('message must be non-empty')
        md = kwargs.get('metadata')
        if md is not None:
            record['metadata'] = md
        notifications.append(record)
        return _ok({'notification': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'send_notification', 'description': 'Record a notification (deterministic timestamp). Optionally include CI/linkage metadata.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'project_id': {'type': 'string'}, 'notification_type': {'type': 'string'}, 'title': {'type': 'string'}, 'message': {'type': 'string'}, 'recipient_id': {'type': 'string'}, 'channel': {'type': 'string'}, 'sent_at': {'type': 'string'}, 'read_at': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['message']}}}
