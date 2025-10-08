from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateIngestionLog(Tool):
    """
    Establish a new ingestion log entry.

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
    def invoke(data: dict[str, Any], source_name: str = None, status_code: int = None, records_ingested: int = None, request_timestamp_utc: str = "2025-08-10 12:00:00") -> str:
        #1) Confirm required fields
        missing = []
        if source_name is None:
            missing.append("source_name")
        if status_code is None:
            missing.append("status_code")
        if records_ingested is None:
            missing.append("records_ingested")
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Access DB
        logs: list[dict[str, Any]] = data.get("ingestion_logs", [])

        #3) Create a new ingestion_id in a deterministic manner
        new_id = get_next_ingestion_id(data)

        #4) Establish record
        new_row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": get_current_timestamp(),
            "status_code": status_code,
            "records_ingested": records_ingested,
        }

        #5) Add
        logs.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIngestionLog",
                "description": "Create a new ingestion log record; ingestion_id auto-generated (count + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "Name of the ingestion source (e.g., 'mlb_api', 'trackman').",
                        },
                        "status_code": {
                            "type": "integer",
                            "description": "HTTP-like status code of the ingestion attempt.",
                        },
                        "records_ingested": {
                            "type": "integer",
                            "description": "Number of records successfully ingested.",
                        },
                        "request_timestamp_utc": {
                            "type": "string",
                            "description": "UTC timestamp 'YYYY-MM-DD HH:MM:SS' (optional). Defaults to '2025-08-10 12:00:00' if omitted.",
                        },
                    },
                    "required": ["source_name", "status_code", "records_ingested"],
                },
            },
        }
