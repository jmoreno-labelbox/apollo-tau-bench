# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug


def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], ):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

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