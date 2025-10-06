from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CalculateTotalSizeTool(Tool):
    """Determines the total size of a collection of files."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalSize",
                "description": "Computes the sum of the sizes for a given list of file paths.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {
                            "type": "array",
                            "items": {
},
                        },
                        "file_list_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_paths: list = None, file_list_name: str = None, file_list_directory: str = None) -> str:
        pass
        # Allow either direct file_paths or a reference to a file list contained in data.
        file_entries = []
        if file_paths is not None:
            file_entries = file_paths or []
        elif file_list_name:
            name = file_list_name
            stored = data.get(name)
            if isinstance(stored, dict) and isinstance(stored.get("data"), list):
                file_entries = stored.get("data")
            else:
                payload = {
                    "status": "error",
                    "message": "file_list_not_found",
                    "file_list_name": name,
                }
                out = json.dumps(payload)
                return out
        else:
            # attempt to identify a default 'file_list' or 'file_check_log.json'.
            if "file_list" in data and isinstance(data["file_list"], list):
                file_entries = data["file_list"]
            elif "file_check_log.json" in data and isinstance(
                data["file_check_log.json"].get("data"), list
            ):
                file_entries = data["file_check_log.json"]["data"]
            else:
                payload = {"status": "error", "message": "no_file_entries_provided"}
                out = json.dumps(payload)
                return out

        # utility to retrieve size from different entry formats.
        def entry_size(entry):
            pass
            if isinstance(entry, dict):
                if "size" in entry and isinstance(entry["size"], (int, float)):
                    return int(entry["size"])
                # the entry might be nested.
                if (
                    "metadata" in entry
                    and isinstance(entry["metadata"], dict)
                    and "size" in entry["metadata"]
                ):
                    return int(entry["metadata"]["size"])
                # might contain a path that we can reference.
                path = entry.get("path") or entry.get("file_path")
            else:
                path = entry

            # retrieve size based on path.
            if path:
                # verify file_index.
                idx = data.get("file_index", {})
                if (
                    isinstance(idx, dict)
                    and path in idx
                    and isinstance(idx[path].get("size"), (int, float))
                ):
                    return int(idx[path]["size"])
                for item in data.get("files", []) or []:
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
            # size is undetermined.
            return None

        total = 0
        unknown: list[str] = []
        for e in file_entries:
            s = entry_size(e)
            if s is None:
                # attempt to display useful information.
                if isinstance(e, dict):
                    unknown.append(e.get("path") or str(e))
                else:
                    unknown.append(str(e))
            else:
                total += s

        if unknown:
            payload = {"status": "error", "message": "unknown_sizes", "unknown": unknown}
            out = json.dumps(payload)
            return out

        # save a deterministic field for subsequent tools.
        data["last_total_size"] = total
        payload = {"status": "success", "total_size": total}
        out = json.dumps(payload)
        return out
