from tau_bench.envs.tool import Tool
import json
from typing import Any

class PostJournalEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str, account: str, memo: str = "", amount_ref: dict[str, Any] = {}, amount: float = None) -> str:
        if amount is None:
            amount = float(amount_ref.get("adjustment", 0.0))
        else:
            amount = float(amount)
        journals = data.setdefault("journals", [])
        rec = {
            "journal_id": f"JRN-{len(journals)+1:05d}",
            "date": date,
            "account": account,
            "amount": round(amount, 2),
            "memo": memo,
        }
        journals.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostJournalEntry",
                "description": "Post a simple journal entry (in-memory).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "account": {"type": "string"},
                        "amount_ref": {"type": "object"},
                        "memo": {"type": "string"},
                    },
                    "required": ["date", "account", "amount_ref"],
                },
            },
        }
