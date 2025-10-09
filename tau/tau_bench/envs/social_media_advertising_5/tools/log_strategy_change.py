from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogStrategyChange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        changed_at: str = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        rows = data.get("strategy_changes", [])
        nid = f"SC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {
            "change_id": nid,
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason,
        }
        rows.append(rec)
        data["strategy_changes"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Appends a strategy change log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_strategy": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "old_bid": {"type": ["number", "null"]},
                        "new_bid": {"type": ["number", "null"]},
                        "changed_at": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "old_bid",
                        "new_bid",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }
