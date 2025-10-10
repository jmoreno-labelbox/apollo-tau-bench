# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class DeployLambdaFunction(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        environment: str,
        service_name: str,
        source_bundle_id: str,
        function_purpose: str,
    ) -> str:
        lambdas = _ensure_table(data, "aws_lambdas")
        fn_slug = f"{service_name.lower().replace(' ','-')}-{function_purpose.lower()}-{environment.lower()}"
        function_name = f"fn-{fn_slug}"
        function_arn = f"arn:aws:lambda:local:000000000000:function:{function_name}"
        row = _find_one(lambdas, function_arn=function_arn)
        payload = {
            "function_arn": function_arn,
            "function_name": function_name,
            "service_name": service_name,
            "environment": environment,
            "function_purpose": function_purpose,
            "source_bundle_id": source_bundle_id,
        }
        if row:
            row.update({**payload, "updated_at": FIXED_NOW})
        else:
            lambdas.append({**payload, "created_at": FIXED_NOW})
        return _json({"function_arn": function_arn, "function_name": function_name})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "deploy_lambda_function",
                "description": "Deploy Lambda; deterministic name from service/purpose/environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "service_name": {"type": "string"},
                        "source_bundle_id": {"type": "string"},
                        "function_purpose": {
                            "type": "string",
                            "enum": ["cache_warmer", "webhook", "ingest", "maintenance"],
                        },
                    },
                    "required": [
                        "environment",
                        "service_name",
                        "source_bundle_id",
                        "function_purpose",
                    ],
                },
            },
        }
