# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkUpdateChecklistItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], fields = {}, item_ids = []) -> str:
        rows = _ensure_list(data, "checklist_items")
        updated = []
        for item_id in item_ids:
            row = _find_by_key(rows, "item_id", item_id)
            if row:
                for k, v in fields.items():
                    row[k] = v
                row["updated_ts"] = NOW_TS
                updated.append(item_id)
        return json.dumps({"updated_item_ids": updated, "count": len(updated)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "bulk_update_checklist_items", "description": "Update multiple checklist items.",
                             "parameters": {"type": "object",
                                            "properties": {"item_ids": {"type": "array", "items": {"type": "string"}},
                                                           "fields": {"type": "object"}},
                                            "required": ["item_ids", "fields"]}}}
