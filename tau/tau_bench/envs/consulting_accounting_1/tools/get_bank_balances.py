from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBankBalances(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        accts = data.get("bank_accounts", {}).values()
        total = 0.0
        details: list[dict[str, Any]] = []
        for a in accts:
            bal = float(a.get("current_balance", 0.0))
            total += bal
            details.append(
                {
                    "account_id": a.get("account_id"),
                    "balance": bal,
                    "currency": a.get("currency"),
                }
            )
        payload = {"total_balance": round(total, 2), "accounts": details}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBankBalances",
                "description": "Return total and per-account current balances.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
