from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, objective: str = None, created_date: str = None) -> str:
        campaigns = data.get("campaigns", [])
        nid = max((int(c["campaign_id"]) for c in campaigns), default=0) + 1
        rec = {
            "campaign_id": str(nid),
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": "paused",
        }
        campaigns.append(rec)
        data["campaigns"] = campaigns
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCampaign",
                "description": "Creates a paused campaign with a provided created_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                        "created_date": {"type": "string"},
                    },
                    "required": ["name", "objective", "created_date"],
                },
            },
        }
