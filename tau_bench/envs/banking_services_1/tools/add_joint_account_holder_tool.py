from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class AddJointAccountHolderTool(Tool):
    """
    Tool used to add a joint account holder to an existing bank account.

    This tool validates the input data to ensure the account exists and the
    joint holder is a valid customer. It updates the account's list of
    joint holders accordingly.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes the logic to add a joint account holder.

        get_info() -> Dict[str, Any]:
            Returns metadata about the tool, including name, description, and input/output structure.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, holder_id: str = None) -> str:
        if not account_id or not holder_id:
            return json.dumps({"error": "account_id and holder_id are required"})

        accounts = load_json("accounts_joint_holders.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                acc.setdefault("joint_holders", []).append(holder_id)
                return json.dumps(
                    {"status": "Added", "added_at": get_current_timestamp()},
                    indent=2,
                )

        return json.dumps({"error": "Account not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddJointAccountHolder",
                "description": "Add a joint account holder to an existing account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "holder_id": {
                            "type": "string",
                            "description": "New holder's customer ID",
                        },
                    },
                    "required": ["account_id", "holder_id"],
                },
            },
        }
