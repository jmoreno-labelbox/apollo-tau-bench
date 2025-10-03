from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class ValidateRoutingNumberTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], routing_number: str = None) -> str:
        valid_routing_numbers = {
            "021000021": "Chase Bank",
            "011401533": "Wells Fargo",
            "121042882": "Wells Fargo CA",
            "111000025": "Bank of America",
            "026009593": "Bank of America",
            "031201360": "Citibank",
            "221172186": "TD Bank"
        }

        is_valid = routing_number in valid_routing_numbers
        bank_name = valid_routing_numbers.get(routing_number, "Unknown")

        return json.dumps({
            "routing_number": routing_number,
            "is_valid": is_valid,
            "bank_name": bank_name if is_valid else "Invalid routing number"
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateRoutingNumber",
                "description": "Validate a bank routing number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "routing_number": {"type": "string", "description": "9-digit routing number"}
                    },
                    "required": ["routing_number"]
                }
            }
        }
