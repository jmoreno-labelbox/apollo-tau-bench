# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteIngestionLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        logs = data.get("ingestion_logs", [])
        logs.append(kwargs)
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_ingestion_log", "description": "Writes an ingestion log row.", "parameters": {"type": "object", "properties": {"source_name": {"type": "string"}, "status_code": {"type": "integer"}, "records_ingested": {"type": "integer"}}, "required": ["source_name", "status_code"]}}}
