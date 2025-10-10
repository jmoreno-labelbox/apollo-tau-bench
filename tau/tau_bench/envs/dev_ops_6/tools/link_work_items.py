# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkWorkItems(Tool):
    """Create or confirm a link {parent_id, child_id, link_type} (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        parent_id = kwargs.get('parent_id')
        child_id = kwargs.get('child_id')
        link_type = kwargs.get('link_type', 'relates_to')
        if not parent_id or not child_id:
            return _err('parent_id and child_id are required')
        if parent_id == child_id:
            return _err('cannot link an item to itself')
        links = _table(data, 'work_item_links')
        for l in links:
            if l.get('parent_id') == parent_id and l.get('child_id') == child_id and (l.get('link_type') == link_type):
                return _ok({'message': 'link already exists', 'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type})
        links.append({'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type})
        return _ok({'created_link': {'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'link_work_items', 'description': 'Link two work items (parent/child/link_type).', 'parameters': {'type': 'object', 'properties': {'parent_id': {'type': 'string'}, 'child_id': {'type': 'string'}, 'link_type': {'type': 'string'}}, 'required': ['parent_id', 'child_id']}}}
