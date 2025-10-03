from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetCourierInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], courier_id: str = None, tracking_id: str = None, coverage_area: str = None) -> str:
        couriers = data["couriers"]

        if courier_id:
            courier = next((c for c in couriers if c["courier_id"] == courier_id), None)
            if not courier:
                payload = {"error": "Courier not found"}
                out = json.dumps(payload)
                return out
            payload = courier
            out = json.dumps(payload, indent=2)
            return out

        if tracking_id:
            courier = next(
                (c for c in couriers if tracking_id in c["tracking_ids"]), None
            )
            if not courier:
                payload = {"error": "Courier not found for tracking ID"}
                out = json.dumps(payload)
                return out
            payload = {
                    "courier_id": courier["courier_id"],
                    "name": courier["name"],
                    "contact_info": courier["contact_info"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if coverage_area:
            matching_couriers = []
            for courier in couriers:
                if coverage_area in courier["coverage_area"]:
                    matching_couriers.append(
                        {
                            "courier_id": courier["courier_id"],
                            "name": courier["name"],
                            "coverage_area": courier["coverage_area"],
                        }
                    )
            payload = matching_couriers
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "courier_id, tracking_id, or coverage_area is required"}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCourierInfo",
                "description": "Get courier information by courier ID, tracking ID, or coverage area.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_id": {
                            "type": "string",
                            "description": "Courier ID to look up",
                        },
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to find courier",
                        },
                        "coverage_area": {
                            "type": "string",
                            "description": "Geographic area to find couriers for",
                        },
                    },
                },
            },
        }
