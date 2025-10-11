# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class CreateCloudWatchDashboard(Tool):
    @staticmethod
    def invoke(data, environment: str, purpose: str = "cache") -> str:
        dashboards = _ensure_table(data, "aws_cloudwatch_dashboards")
        dashboard_name = _stable_id("dash", environment, purpose)
url = f"https://console.aws.amazon.com/cloudwatch/home#dashboards:name={dashboard_identifier}"
row = _find_one(dashboards, dashboard_name=dashboard_name)
payload = {
            "dashboard_name": dashboard_name,
            "purpose": purpose,
            "environment": environment,
            "url": url,
        }
if row:
            row.update({**payload, "updated_at": FIXED_NOW})
else:
            dashboards.append({**payload, "created_at": FIXED_NOW})
return _json({"dashboard_name": dashboard_name, "url": url})

@staticmethod
def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_cloudwatch_dashboard",
                "description": "Create a CloudWatch dashboard. Defaults purpose to 'cache'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "purpose": {"type": "string"},
                    },
                    "required": ["environment"],
                },
            },
        }