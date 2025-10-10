# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIngestionLog(Tool):
    """
    Create a new ingestion log entry.

    Inputs (exact names; case-sensitive):
      - source_name (str)                [required]
      - status_code (int)                [required]
      - records_ingested (int)           [required]
      - request_timestamp_utc (str)      [optional] 'YYYY-MM-DD HH:MM:SS'
          If omitted, defaults deterministically to '2025-08-10 12:00:00'.

    Behavior:
      - ingestion_id is auto-generated as count(ingestion_logs) + 1.
      - Exact types are required; no coercion.
      - Appends the new record to data["ingestion_logs"] and returns it.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], records_ingested, source_name, status_code, request_timestamp_utc = "2025-08-10 12:00:00") -> str:
        request_ts = request_timestamp_utc

        # 1) Check mandatory fields for validity
        missing = []
        if source_name is None:
            missing.append("source_name")
        if status_code is None:
            missing.append("status_code")
        if records_ingested is None:
            missing.append("records_ingested")
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Connect to the database
        logs: List[Dict[str, Any]] = list(data.get("ingestion_logs", {}).values())

        # 3) Create a new ingestion_id in a deterministic manner.
        new_id = get_next_ingestion_id(data)

        # 4) Generate entry
        new_row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": get_current_timestamp(),
            "status_code": status_code,
            "records_ingested": records_ingested
        }

        # 5) Add
        logs.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ingestion_log",
                "description": "Create a new ingestion log record; ingestion_id auto-generated (count + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "Name of the ingestion source (e.g., 'mlb_api', 'trackman')."
                        },
                        "status_code": {
                            "type": "integer",
                            "description": "HTTP-like status code of the ingestion attempt."
                        },
                        "records_ingested": {
                            "type": "integer",
                            "description": "Number of records successfully ingested."
                        },
                        "request_timestamp_utc": {
                            "type": "string",
                            "description": "UTC timestamp 'YYYY-MM-DD HH:MM:SS' (optional). Defaults to '2025-08-10 12:00:00' if omitted."
                        }
                    },
                    "required": ["source_name", "status_code", "records_ingested"]
                }
            }
        }
