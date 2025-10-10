# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


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
