# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostJournalEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        account = kwargs.get("account")
        memo = kwargs.get("memo","")
        amount_ref = kwargs.get("amount_ref", {})
        amount = float(amount_ref.get("adjustment", 0.0))
        journals = data.setdefault("journals", [])
        rec = {"journal_id": f"JRN-{len(journals)+1:05d}", "date": date, "account": account, "amount": round(amount,2), "memo": memo}
        journals.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"post_journal_entry",
            "description":"Post a simple journal entry (in-memory).",
            "parameters":{"type":"object","properties":{
                "date":{"type":"string"},
                "account":{"type":"string"},
                "amount_ref":{"type":"object"},
                "memo":{"type":"string"}
            },"required":["date","account","amount_ref"]}
        }}
