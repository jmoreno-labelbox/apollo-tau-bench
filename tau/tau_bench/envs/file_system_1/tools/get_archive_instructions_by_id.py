# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetArchiveInstructionsByID(Tool):
    """Retrieves a specific archival task by its ID from the instructions database."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_id = kwargs.get("archive_id")
        for instruction in data.get('archive_instructions', []):
            if instruction.get('archive_id') == archive_id:
                return json.dumps(instruction)
        return json.dumps({"error": f"Archive instruction with ID '{archive_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_archive_instructions_by_id", "description": "Fetches a specific archival task (e.g., files to include, destination) by its unique ID.", "parameters": {"type": "object", "properties": {"archive_id": {"type": "string", "description": "The unique ID of the archive task (e.g., 'arch_001')."}}, "required": ["archive_id"]}}}
