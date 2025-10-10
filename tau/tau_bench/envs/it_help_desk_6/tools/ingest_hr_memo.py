# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IngestHrMemo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], memo_id: str, memo_json: Dict[str, Any]) -> str:
        row = {"memo_id": memo_id, **memo_json}
        _append_row(data["hr_memos"], row)
        return json.dumps({"status": "ok", "memo": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ingest_hr_memo",
                "description": "Insert an HR memo into the hr_memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo_id": {"type": "string"}, "memo_json": {"type": "object"}},
                    "required": ["memo_id", "memo_json"],
                },
            },
        }
