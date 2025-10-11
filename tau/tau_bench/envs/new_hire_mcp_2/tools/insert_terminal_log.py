# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_seq_id(rows: List[Dict[str, Any]], key: str, width: int = 4) -> str:
    mx = 0
    for r in rows:
        v = r.get(key)
        if isinstance(v, str) and v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1).zfill(width)

def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class InsertTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message_text) -> str:
        rows = _ensure_list(data, "terminal_log")
        new_id = _next_seq_id(rows, "entry_id")
        payload = {"entry_id": new_id, "message_text": message_text, "printed_ts": NOW_TS}
        rows.append(payload)
        return json.dumps({"entry_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "insert_terminal_log", "description": "Append an audit line to terminal_log.",
                             "parameters": {"type": "object", "properties": {"message_text": {"type": "string"}},
                                            "required": ["message_text"]}}}