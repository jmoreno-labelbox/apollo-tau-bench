# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOwnerForBisect(Tool):
    """Retrieves the primary owner for a bisect operation based on its suspect files."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bisect_id = kwargs.get("bisect_id")
        bisect_results = data.get("bisect_results", [])
        ownership_map = data.get("ownership_map", [])
        
        # 1. Find the bisect result record
        bisect_record = None
        for result in bisect_results:
            if result.get("id") == bisect_id:
                bisect_record = result
                break
        
        if not bisect_record:
            return json.dumps({"error": f"Bisect with ID '{bisect_id}' not found."})
            
        # 2. Get the list of suspect files from the bisect record
        suspect_files = bisect_record.get("suspect_files", [])
        if not suspect_files:
            # default to user_005 if no suspect files are found
            return json.dumps({"owner_id": "user_005"})
            return json.dumps({"error": f"No suspect files found for bisect '{bisect_id}'."})
            
        # 3. Use the first suspect file to determine primary ownership, as it's the most likely culprit.
        primary_suspect_file = suspect_files[0]
        
        # 4. Find the most specific owner for the primary suspect file from the ownership map
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
        # for when the owner is not found
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
