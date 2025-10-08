from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_text: str = None) -> str:
        rows = _ensure_list(data, "terminal_log")
        new_id = _next_seq_id(rows, "entry_id")
        payload = {
            "entry_id": new_id,
            "message_text": message_text,
            "printed_ts": NOW_TS,
        }
        rows.append(payload)
        payload = {"entry_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertTerminalLog",
                "description": "Append an audit line to terminal_log.",
                "parameters": {
                    "type": "object",
                    "properties": {"message_text": {"type": "string"}},
                    "required": ["message_text"],
                },
            },
        }
