# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetKitComponents(Tool):
    """
    Retrieves the list of component SKUs and quantities for a given virtual kit,
    identified either by SKU or by human‑friendly name.
    """
    KITS_DATABASE = {
        "KIT-ROBO-S1": {
            "kit_name": "Basic Robotic Starter Kit",
            "components": [
                {"sku": "TECH-ROBO-N14", "quantity": 1, "product_name": "Articulated Robotic Arm"},
                {"sku": "TECH-BATT-Q17", "quantity": 2, "product_name": "Lithium‑Ion Battery Pack"}
            ]
        }
    }
    @staticmethod
    def invoke(data: Dict[str, Any], kit_name, kit_sku) -> str:
        kit_sku: str | None = kit_sku
        kit_name: str | None = kit_name

        if not kit_sku and not kit_name:
            return json.dumps(
                {"error": "You must provide either 'kit_sku' or 'kit_name'."},
                indent=2,
            )
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
            return json.dumps({"error": f"Kit with {missing} not found."}, indent=2)

        return json.dumps(kit_data["components"], indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_kit_components",
                "description": (
                    "Retrieves the bill of materials (component SKUs and their "
                    "quantities) for a virtual kit identified by SKU or name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kit_sku": {
                            "type": "string",
                            "description": "The SKU of the virtual kit (e.g., 'KIT-ROBO-S1')."
                        },
                        "kit_name": {
                            "type": "string",
                            "description": "The friendly name of the virtual kit "
                                           "(e.g., 'Basic Robotic Starter Kit')."
                        }
                    },
                    # Nenhum campo é mandatório; pelo menos um é necessário na lógica.
                    "required": []
                }
            }
        }
