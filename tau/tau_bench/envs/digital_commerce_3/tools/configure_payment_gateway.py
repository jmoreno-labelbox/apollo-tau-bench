from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigurePaymentGateway(Tool):
    """Set up payment gateway configurations and processing guidelines."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        gateway_name: Any,
        merchant_id: Any,
        supported_currencies: Any = ["USD"]
    ) -> str:
        if not gateway_name or not merchant_id:
            return _error("gateway_name and merchant_id are required.")

        gateways = data.setdefault("payment_gateways", [])
        gateway = {
            "gateway_id": f"GW_{len(gateways) + 1:03d}",
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "supported_currencies": supported_currencies,
            "status": "active",
            "configured_at": FIXED_NOW,
        }
        gateways.append(gateway)

        result = {
            "gateway_id": gateway["gateway_id"],
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "status": "configured",
        }

        _append_audit(
            data,
            "payment_gateway_configured",
            gateway["gateway_id"],
            {"gateway_name": gateway_name, "merchant_id": merchant_id},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        gateway_name = gateway_name
        merchant_id = merchant_id
        supported_currencies = supported_currencies

        if not gateway_name or not merchant_id:
            return _error("gateway_name and merchant_id are required.")

        gateways = data.setdefault("payment_gateways", [])
        gateway = {
            "gateway_id": f"GW_{len(gateways) + 1:03d}",
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "supported_currencies": supported_currencies,
            "status": "active",
            "configured_at": FIXED_NOW,
        }
        gateways.append(gateway)

        result = {
            "gateway_id": gateway["gateway_id"],
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "status": "configured",
        }

        _append_audit(
            data,
            "payment_gateway_configured",
            gateway["gateway_id"],
            {"gateway_name": gateway_name, "merchant_id": merchant_id},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigurePaymentGateway",
                "description": "Configure payment gateway settings and processing rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "gateway_name": {"type": "string"},
                        "merchant_id": {"type": "string"},
                        "supported_currencies": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["gateway_name", "merchant_id"],
                },
            },
        }
