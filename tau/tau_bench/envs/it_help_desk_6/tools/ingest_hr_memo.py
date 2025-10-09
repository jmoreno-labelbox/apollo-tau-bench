from tau_bench.envs.tool import Tool
import json
from typing import Any

class IngestHrMemo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str, memo_json: dict[str, Any]) -> str:
        pass
        row = {"memo_id": memo_id, **memo_json}
        _append_row(data["hr_memos"], row)
        payload = {"status": "ok", "memo": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ingestHrMemo",
                "description": "Insert an HR memo into the hr_memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "memo_id": {"type": "string"},
                        "memo_json": {"type": "object"},
                    },
                    "required": ["memo_id", "memo_json"],
                },
            },
        }
