from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EnrollDeviceInMDM(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        asset = next(
            (a for a in data.get("it_assets", {}).values() if a.get("asset_id") == asset_id),
            None,
        )
        if asset:
            asset["mdm_enrolled"] = True
            payload = {"asset_id": asset_id, "enrollment_status": "success"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": f"Asset {asset_id} not found for MDM enrollment."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enrollDeviceInMdm",
                "description": "Enrolls a specified IT asset into the Mobile Device Management system.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
