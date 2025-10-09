from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class TransferToHumanAgents(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], summary: str) -> str:
        payload = {"status": "Transfer successful", "summary": summary}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferToHumanAgents",
                "description": "Transfers the user to a human agent, with a summary of the issue. Use only when the user's issue cannot be resolved with the available tools.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "A concise summary of the user's issue and why the transfer is necessary.",
                        }
                    },
                    "required": ["summary"],
                },
            },
        }
