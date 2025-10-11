# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(table: List[Dict[str, Any]], key: str, prefix: str) -> str:
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split('_')[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"

class CreateDataArchiveEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, location_uri, retention_label, system) -> str:
        archives = data.setdefault("data_archives", [])
        archive_id = _get_next_id(archives, "archive_id", "arch")
        new_archive = {"archive_id": archive_id, "employee_id": employee_id, "system": system, "location_uri": location_uri, "retention_label": retention_label, "created_at": FIXED_NOW}
        archives.append(new_archive)
        return json.dumps(new_archive, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_data_archive_entry", "description": "Creates an entry in the data archives table, typically after a mailbox export.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "system": {"type": "string"}, "retention_label": {"type": "string"}, "location_uri": {"type": "string"}}, "required": ["employee_id", "system", "retention_label", "location_uri"]}}}