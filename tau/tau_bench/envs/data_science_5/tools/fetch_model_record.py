# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchModelRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], model_id, model_name) -> str:
        models = list(data.get("models", {}).values()) or []
        mid = model_id
        mname = model_name
        row = None
        if mid is not None:
            row = next((m for m in models if str(m.get("model_id")) == str(mid)), None)
        elif mname:
            row = next((m for m in models if m.get("model_name") == mname), None)
        return json.dumps(row or {"error": "Model not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_model_record",
            "description": "Read a model by id or by name.",
            "parameters": {"type": "object", "properties": {
                "model_id": {"type": "string"},
                "model_name": {"type": "string"}
            }, "required": []}
        }}
