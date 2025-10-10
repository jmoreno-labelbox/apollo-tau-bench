# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalSizeTool(Tool):
    """Calculates the total size of a list of files."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_size",
                "description": "Computes the sum of the sizes for a given list of file paths.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {
                            "type": "array",
                            "items": {
                                "oneOf": [{"type": "string"}, {"type": "object"}]
                            },
                        },
                        "file_list_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], file_list_name, file_paths) -> str:
        # Allow for either direct file_paths or a reference to a list of files contained in data.
        file_entries = []
        if "file_paths" in kwargs and file_paths is not None:
            file_entries = file_paths or []
        elif "file_list_name" in kwargs and file_list_name:
            name = file_list_name
            stored = data.get(name)
            if isinstance(stored, dict) and isinstance(stored.get("data"), list):
                file_entries = stored.get("data")
            else:
                return json.dumps(
                    {
                        "status": "error",
                        "message": "file_list_not_found",
                        "file_list_name": name,
                    }
                )
        else:
            # attempt to identify a default 'file_list' or 'file_check_log.json'
            if "file_list" in data and isinstance(data["file_list"], list):
                file_entries = data["file_list"]
            elif "file_check_log.json" in data and isinstance(
                data["file_check_log.json"].get("data"), list
            ):
                file_entries = data["file_check_log.json"]["data"]
            else:
                return json.dumps(
                    {"status": "error", "message": "no_file_entries_provided"}
                )

        # utility for obtaining dimensions from different entry forms
        def entry_size(entry):
            if isinstance(entry, dict):
                if "size" in entry and isinstance(entry["size"], (int, float)):
                    return int(entry["size"])
                # the entry might be hierarchical
                if (
                    "metadata" in entry
                    and isinstance(entry["metadata"], dict)
                    and "size" in entry["metadata"]
                ):
                    return int(entry["metadata"]["size"])
                # might incorporate a path for reference
                path = entry.get("path") or entry.get("file_path")
            else:
                path = entry

            # retrieve size using path
            if path:
                # verify file_index
                idx = data.get("file_index", {})
                if (
                    isinstance(idx, dict)
                    and path in idx
                    and isinstance(idx[path].get("size"), (int, float))
                ):
                    return int(idx[path]["size"])
                for item in list(data.get("files", {}).values()) or []:
                    if (
                        isinstance(item, dict)
                        and item.get("path") == path
                        and isinstance(item.get("size"), (int, float))
                    ):
                        return int(item["size"])
                for server in data.get("file_system", []) or []:
                    for f in server.get("files", []) or []:
                        if f.get("path") == path and isinstance(
                            f.get("size"), (int, float)
                        ):
                            return int(f.get("size"))
            # size not specified
            return None

        total = 0
        unknown: List[str] = []
        for e in file_entries:
            s = entry_size(e)
            if s is None:
                # attempt to demonstrate something beneficial
                if isinstance(e, dict):
                    unknown.append(e.get("path") or str(e))
                else:
                    unknown.append(str(e))
            else:
                total += s

        if unknown:
            return json.dumps(
                {"status": "error", "message": "unknown_sizes", "unknown": unknown}
            )

        # save a consistent field for subsequent tools
        data["last_total_size"] = total
        return json.dumps({"status": "success", "total_size": total})
