from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadOffboardingMemo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str = None) -> str:
        memo = next(
            (
                m
                for m in data.get("hr_memos", [])
                if m.get("memo_id") == memo_id and m.get("type") == "offboarding"
            ),
            None,
        )
        if not memo:
            payload = {"error": f"Offboarding memo {memo_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "readOffboardingMemo",
                "description": "Reads and returns a specific offboarding memo from the HR memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo_id": {"type": "string"}},
                    "required": ["memo_id"],
                },
            },
        }
