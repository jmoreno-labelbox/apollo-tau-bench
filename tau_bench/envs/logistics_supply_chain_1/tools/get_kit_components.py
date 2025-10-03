from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class GetKitComponents(Tool):
    """
    Fetches the list of component SKUs and their quantities for a specified virtual kit,
    identified by either SKU or a user-friendly name.
    """

    KITS_DATABASE = {
        "KIT-ROBO-S1": {
            "kit_name": "Basic Robotic Starter Kit",
            "components": [
                {
                    "sku": "TECH-ROBO-N14",
                    "quantity": 1,
                    "product_name": "Articulated Robotic Arm",
                },
                {
                    "sku": "TECH-BATT-Q17",
                    "quantity": 2,
                    "product_name": "Lithium‑Ion Battery Pack",
                },
            ],
        }
    }

    @staticmethod
    def invoke(data: dict[str, Any], kit_sku: str = None, kit_name: str = None) -> str:
        if not kit_sku and not kit_name:
            payload = {"error": "You must provide either 'kit_sku' or 'kit_name'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        kit_data = GetKitComponents.KITS_DATABASE.get(kit_sku) if kit_sku else None
        if not kit_data and kit_name:
            kit_data = next(
                (
                    v
                    for v in GetKitComponents.KITS_DATABASE.values()
                    if v["kit_name"].lower() == kit_name.lower()
                ),
                None,
            )

        if not kit_data:
            missing = f"SKU '{kit_sku}'" if kit_sku else f"name '{kit_name}'"
            payload = {"error": f"Kit with {missing} not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = kit_data["components"]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetKitComponents",
                "description": (
                    "Retrieves the bill of materials (component SKUs and their "
                    "quantities) for a virtual kit identified by SKU or name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kit_sku": {
                            "type": "string",
                            "description": "The SKU of the virtual kit (e.g., 'KIT-ROBO-S1').",
                        },
                        "kit_name": {
                            "type": "string",
                            "description": "The friendly name of the virtual kit "
                            "(e.g., 'Basic Robotic Starter Kit').",
                        },
                    },
                    #No field is mandatory; at least one is required in the logic
                    "required": [],
                },
            },
        }
