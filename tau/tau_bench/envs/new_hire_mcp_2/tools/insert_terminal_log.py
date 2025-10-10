# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "terminal_log")
        new_id = _next_seq_id(rows, "entry_id")
        payload = {"entry_id": new_id, "message_text": kwargs.get("message_text"), "printed_ts": NOW_TS}
        rows.append(payload)
        return json.dumps({"entry_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "insert_terminal_log", "description": "Append an audit line to terminal_log.",
                             "parameters": {"type": "object", "properties": {"message_text": {"type": "string"}},
                                            "required": ["message_text"]}}}
