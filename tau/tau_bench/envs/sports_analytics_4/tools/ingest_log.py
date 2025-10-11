# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IngestLog(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get("ingestion_logs", [])
        logs.append(kwargs)
        # return outcome
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "makeLogs", "description": "Persists an ingestion log row.", "parameters": {"type": "object", "properties": {"source_name": {"type": "string"}, "status_code": {"type": "integer"}, "logs_ingested": {"type": "integer"}}, "required": ["source_name", "status_code"]}}}
