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

class CreateLambdaSchedule(Tool):
    @staticmethod
    def invoke(data, function_arn: str, schedule_expression: str = "rate(15 minutes)") -> str:
        schedules = _ensure_table(data, "aws_lambda_schedules")
        schedule_id = _stable_id("sched", function_arn, schedule_expression)
        rule_name = f"rule-{schedule_id}"
        row = _find_one(schedules, schedule_id=schedule_id)
        if row:
            row.update(
                {
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            schedules.append(
                {
                    "schedule_id": schedule_id,
                    "rule_name": rule_name,
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"schedule_id": schedule_id, "rule_name": rule_name})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_lambda_schedule",
                "description": "Create an EventBridge schedule for a Lambda. Defaults to rate(15 minutes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function_arn": {"type": "string"},
                        "schedule_expression": {"type": "string"},
                    },
                    "required": ["function_arn"],
                },
            },
        }