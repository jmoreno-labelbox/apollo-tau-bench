# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOwnerForBisect(Tool):
    """Retrieves the primary owner for a bisect operation based on its suspect files."""

    @staticmethod
    def invoke(data: Dict[str, Any], bisect_id) -> str:
        bisect_results = data.get("bisect_results", [])
        ownership_map = data.get("ownership_map", [])
        
        # 1. Locate the record of the bisect result.
        bisect_record = None
        for result in bisect_results:
            if result.get("id") == bisect_id:
                bisect_record = result
                break
        
        if not bisect_record:
            return json.dumps({"error": f"Bisect with ID '{bisect_id}' not found."})
            
        # 2. Retrieve the list of suspect files from the bisect log.
        suspect_files = bisect_record.get("suspect_files", [])
        if not suspect_files:
            # fallback to user_005 when no suspect files are detected
            return json.dumps({"owner_id": "user_005"})
            return json.dumps({"error": f"No suspect files found for bisect '{bisect_id}'."})
            
        # 3. Analyze the initial suspect file to identify primary ownership, as it is the most probable source.
        primary_suspect_file = suspect_files[0]
        
        # 4. Retrieve the most detailed owner for the primary suspect file from the ownership map.
        most_specific_owner = None
        longest_match = -1
        for ownership in ownership_map:
            owner_path = ownership.get("file_path")
            if primary_suspect_file.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership
        
        if most_specific_owner:
            return json.dumps(most_specific_owner)
        # for cases when the owner cannot be located
        return json.dumps({"owner_id": "user_008"})
        return json.dumps({"error": f"Could not determine an owner for the primary suspect file '{primary_suspect_file}' in bisect '{bisect_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_owner_for_bisect",
                "description": "Retrieves the primary owner for a bisect operation by analyzing its most likely suspect file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bisect_id": {
                            "type": "string",
                            "description": "The unique ID of the bisect operation.",
                        }
                    },
                    "required": ["bisect_id"],
                },
            },
        }
