from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetCurrencyConversionAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_currency: str = None, target_currency: str = None, source_amount: float = None) -> str:
        source = source_currency
        target = target_currency
        amount = source_amount

        if not all([source, target, amount]):
            return json.dumps(
                {"error": "source_currency, source_amount, and target_currency are required."},
                indent=2
            )

        rates = {
            "USD_EUR": 0.85,
            "EUR_USD": 1.18,
            "USD_GBP": 0.75,
            "GBP_USD": 1.33,
            "USD_CAD": 1.25,
            "CAD_USD": 0.80,
            # add more as needed
        }

        key = f"{source.upper()}_{target.upper()}"
        rate = rates.get(key)
        if rate is None:
            return json.dumps(
                {"error": f"No conversion rate available for {source} to {target}."},
                indent=2
            )

        target_amount = amount * rate

        return json.dumps(
            {
                "source_currency": source.upper(),
                "source_amount": amount,
                "target_currency": target.upper(),
                "target_amount": round(target_amount, 2)
            },
            indent=2
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrencyConversionAmount",
                "description": (
                    "Converts a specified amount from one currency to another "
                    "using a static rate table, returning both source and target amounts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_currency": {
                            "type": "string",
                            "description": "Currency code to convert from (e.g., 'USD')"
                        },
                        "source_amount": {
                            "type": "number",
                            "description": "Amount in the source currency"
                        },
                        "target_currency": {
                            "type": "string",
                            "description": "Currency code to convert to (e.g., 'EUR')"
                        }
                    },
                    "required": ["source_currency", "source_amount", "target_currency"]
                }
            }
        }
