# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterSymbol(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "register_symbol",
                "description": "Registers a symbol record for a build module.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_id": {"type": "string", "description": "Build id"},
                        "module_name": {"type": "string", "description": "Module name"},
                        "platform": {"type": "string", "description": "Platform name"},
                        "pdb_uri": {"type": "string", "description": "PDB/Symbol uri"},
                        "status": {"type": "string", "description": "available|deprecated", "enum": ["available", "deprecated"]}
                    },
                    "required": ["build_id", "module_name", "platform", "pdb_uri", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        build_id = kwargs.get("build_id")
        module_name = kwargs.get("module_name")
        platform = kwargs.get("platform")
        pdb_uri = kwargs.get("pdb_uri")
        status = kwargs.get("status")
        symbols = data.get("symbols", [])
        sym_id = f"AUTO::symbol::{build_id}::{module_name}"
        existing = next((s for s in symbols if s.get("id") == sym_id), None)
        if existing:
            existing.update({"build_id": build_id, "module_name": module_name, "platform": platform, "pdb_uri": pdb_uri, "status": status})
        else:
            symbols.append({"id": sym_id, "build_id": build_id, "module_name": module_name, "platform": platform, "pdb_uri": pdb_uri, "status": status})
        data["symbols"] = symbols
        return json.dumps({"symbol": next(s for s in symbols if s.get("id") == sym_id)}, indent=2)
