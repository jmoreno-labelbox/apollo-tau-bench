from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class ComputeAndResolveDestinationPathsTool(Tool):
    """Determines destination paths for files according to sorting rules and addresses name conflicts."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeAndResolveDestinationPaths",
                "description": "Computes destination paths for all files in file_list, handles conflicts by appending integers, and populates the 'destination_path' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_directory": {"type": "string"},
                        "sort_rules": {"type": "object"},
                    },
                    "required": ["destination_directory", "sort_rules"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_directory: str, sort_rules: dict[str, str]) -> str:
        dest_dir = destination_directory
        sort_rules = sort_rules
        destination_paths: set[str] = set()

        for file in data.get("file_list", []):
            ext = file["filename"].split(".")[-1] if "." in file["filename"] else ""
            sub_dir = sort_rules.get(ext, "miscellaneous")
            base = (
                ".".join(file["filename"].split(".")[:-1])
                if "." in file["filename"]
                else file["filename"]
            )
            ext_suffix = f".{ext}" if ext else ""
            new_name = f"{base}{ext_suffix}"
            new_path = f"{dest_dir}/{sub_dir}/{new_name}"

            counter = 0
            candidate = new_path
            while candidate in destination_paths:
                candidate = f"{dest_dir}/{sub_dir}/{base}_{counter}{ext_suffix}"
                counter += 1

            destination_paths.add(candidate)
            file["destination_path"] = candidate
        payload = {"status": "success", "paths_resolved": len(data.get("file_list", []))}
        out = json.dumps(
            payload)
        return out
