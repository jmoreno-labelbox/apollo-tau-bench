# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildMtpMessages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], model_path, test_samples, train_samples) -> str:
        if train_samples is None or test_samples is None or not model_path:
            return json.dumps({"error":"Missing train_samples, test_samples, or model_path"})
        messages = [
            f"Training samples: {int(train_samples)}",
            f"Test samples: {int(test_samples)}",
            f"Model saved to: {model_path}"
        ]
        return json.dumps({"messages": messages})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_messages","description":"Builds deterministic MTP messages list.","parameters":{"type":"object","properties":{"train_samples":{"type":"integer"},"test_samples":{"type":"integer"},"model_path":{"type":"string"}},"required":["train_samples","test_samples","model_path"]}}}
