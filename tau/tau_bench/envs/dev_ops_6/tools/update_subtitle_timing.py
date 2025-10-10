# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSubtitleTiming(Tool):
    """Update subtitle_timing row fields (e.g., subtitle_start/end/text) with basic guards."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sub_id = kwargs.get('id')
        updates: Dict[str, Any] = kwargs.get('updates', {})
        table = _table(data, 'subtitle_timing')
        row = next((r for r in table if r.get('id') == sub_id), None)
        if not row:
            return _err(f'subtitle_timing id not found: {sub_id}')
        if 'subtitle_start' in updates and 'subtitle_end' in updates:
            s, e = (updates['subtitle_start'], updates['subtitle_end'])
            if not (isinstance(s, (int, float)) and isinstance(e, (int, float))):
                return _err('subtitle_start/subtitle_end must be numeric')
            if not 0 <= s < e:
                return _err('subtitle_start must be >= 0 and < subtitle_end')
        row.update(updates)
        return _ok({'updated_subtitle': {'id': sub_id, 'applied_updates': updates}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'update_subtitle_timing', 'description': 'Update a subtitle_timing record with basic timing guards.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'updates': {'type': 'object'}}, 'required': ['id', 'updates']}}}
