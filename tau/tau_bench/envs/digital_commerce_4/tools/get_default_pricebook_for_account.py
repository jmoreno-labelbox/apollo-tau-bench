# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDefaultPricebookForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: Any) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required."}, indent=2)
        account_id = _as_id(account_id)
        acc = next(
            (a for a in list(data.get("accounts", {}).values()) if _as_id(a.get("account_id")) == account_id), None
        )
        if not acc:
            return json.dumps({}, indent=2)
        pbid = _as_id(acc.get("default_pricebook_id"))
        pb = next(
            (p for p in data.get("pricebooks", []) if _as_id(p.get("pricebook_id")) == pbid), None
        )
        return json.dumps({"account_id": account_id, "pricebook": (pb or {})}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_default_pricebook_for_account",
                "description": "Return the default pricebook record for an account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Target account_id."}
                    },
                    "required": ["account_id"],
                },
            },
        }
