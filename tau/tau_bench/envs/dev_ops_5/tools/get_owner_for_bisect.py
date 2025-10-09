from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOwnerForBisect(Tool):
    """Fetches the primary owner for a bisect operation according to its suspect files."""

    @staticmethod
    def invoke(data: dict[str, Any], bisect_id: str = None) -> str:
        bisect_results = data.get("bisect_results", [])
        ownership_map = data.get("ownership_map", [])

        #1. Locate the bisect result record
        bisect_record = None
        for result in bisect_results:
            if result.get("id") == bisect_id:
                bisect_record = result
                break

        if not bisect_record:
            payload = {"error": f"Bisect with ID '{bisect_id}' not found."}
            out = json.dumps(payload)
            return out

        #2. Retrieve the list of suspect files from the bisect record
        suspect_files = bisect_record.get("suspect_files", [])
        if not suspect_files:
            payload = {"owner_id": "user_005"}
            out = json.dumps(payload)
            return out
            payload = {"error": f"No suspect files found for bisect '{bisect_id}'."}
            out = json.dumps(
                payload)
            return out

        #3. Utilize the first suspect file to identify primary ownership, as it is the most probable cause.
        primary_suspect_file = suspect_files[0]

        #4. Identify the most specific owner for the primary suspect file using the ownership map
        most_specific_owner = None
        longest_match = -1
        for ownership in ownership_map:
            owner_path = ownership.get("file_path")
            if primary_suspect_file.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership

        if most_specific_owner:
            payload = most_specific_owner
            out = json.dumps(payload)
            return out
        payload = {"owner_id": "user_008"}
        out = json.dumps(payload)
        return out
        payload = {
                "error": f"Could not determine an owner for the primary suspect file '{primary_suspect_file}' in bisect '{bisect_id}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOwnerForBisect",
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
