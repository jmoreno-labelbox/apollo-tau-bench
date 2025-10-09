from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildMtpMessages(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], train_samples: int = None, test_samples: int = None, model_path: str = None) -> str:
        if train_samples is None or test_samples is None or not model_path:
            payload = {"error": "Missing train_samples, test_samples, or model_path"}
            out = json.dumps(payload)
            return out
        messages = [
            f"Training samples: {int(train_samples)}",
            f"Test samples: {int(test_samples)}",
            f"Model saved to: {model_path}",
        ]
        payload = {"messages": messages}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpMessages",
                "description": "Builds deterministic MTP messages list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_samples": {"type": "integer"},
                        "test_samples": {"type": "integer"},
                        "model_path": {"type": "string"},
                    },
                    "required": ["train_samples", "test_samples", "model_path"],
                },
            },
        }
