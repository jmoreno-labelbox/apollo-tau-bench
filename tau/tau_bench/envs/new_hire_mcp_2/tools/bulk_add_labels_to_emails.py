# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None

def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class BulkAddLabelsToEmails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], label_ids = [], message_ids = []) -> str:
        rows = _ensure_list(data, "emails")
        updated = []
        for mid in message_ids:
            row = _find_by_key(rows, "message_id", mid)
            if row:
                dst = row.setdefault("labels_ids", [])
                for lid in label_ids:
                    if lid not in dst:
                        dst.append(lid)
                updated.append(mid)
        return json.dumps({"message_ids": updated, "count": len(updated), "labels_applied": label_ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "bulk_add_labels_to_emails", "description": "Apply label_ids to multiple emails.",
                             "parameters": {"type": "object", "properties": {
                                 "message_ids": {"type": "array", "items": {"type": "string"}},
                                 "label_ids": {"type": "array", "items": {"type": "string"}}},
                                            "required": ["message_ids", "label_ids"]}}}