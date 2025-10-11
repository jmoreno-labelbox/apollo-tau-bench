# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table










def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], **crit):
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

class CreateCloudWatchAlarm(Tool):
    @staticmethod
    def invoke(
        data,
        resource_id: str,
        metric_name: str = "Errors",
        threshold: float = 1.0,
        period_seconds: int = 300,
        comparison: str = "GreaterThanOrEqualToThreshold",
    ) -> str:
        alarms = _ensure_table(data, "aws_cloudwatch_alarms")
        alarm_id = _stable_id(
            "al", resource_id, metric_name, str(threshold), str(period_seconds), comparison
        )
        alarm_name = f"{metric_name}-{resource_id}"
        row = _find_one(alarms, alarm_id=alarm_id)
        payload = {
            "resource_id": resource_id,
            "metric_name": metric_name,
            "threshold": float(threshold),
            "period_seconds": int(period_seconds),
            "comparison": comparison,
        }
        if row:
            row.update(payload)
            row["state"] = "OK"
            row["updated_at"] = FIXED_NOW
        else:
            alarms.append(
                {
                    "alarm_id": alarm_id,
                    "alarm_name": alarm_name,
                    "state": "OK",
                    **payload,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"alarm_id": alarm_id, "alarm_name": alarm_name, "state": "OK"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_cloudwatch_alarm",
                "description": "Create a CloudWatch alarm. Defaults: Errors, 1.0, 300s, GTE.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "threshold": {"type": "number"},
                        "period_seconds": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["resource_id"],
                },
            },
        }