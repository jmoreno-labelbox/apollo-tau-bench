# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBankBalances(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        accts = list(data.get("bank_accounts", {}).values())
        total = 0.0
        details: List[Dict[str, Any]] = []
        for a in accts:
            bal = float(a.get("current_balance", 0.0))
            total += bal
            details.append({"account_id": a.get("account_id"),"balance": bal,"currency": a.get("currency")})
        return json.dumps({"total_balance": round(total, 2),"accounts": details}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_bank_balances","description": "Return total and per-account current balances.","parameters": {"type": "object","properties": {}}}}
