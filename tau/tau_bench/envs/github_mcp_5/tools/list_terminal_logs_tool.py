from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime

class ListTerminalLogsTool(Tool):
    """
    List terminal log events deterministically.

    This tool retrieves all recorded terminal log events from the dataset.
    Each event is augmented with a deterministic `report_date` field set to CURRENT_DATE.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok".
            - data: A list of terminal events with their original metadata plus:
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - None. Returns an empty list if no terminal events exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        events = data.get("terminal", [])
        deterministic_events = [{**e, "report_date": CURRENT_DATE} for e in events]
        return _response("ok", deterministic_events)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listTerminalEvents",
                "description": "List timeline events from terminal logs deterministically.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
