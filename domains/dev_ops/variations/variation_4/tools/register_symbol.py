from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterSymbol(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RegisterSymbol",
                "description": "Registers a symbol record for a build module.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_id": {"type": "string", "description": "Build id"},
                        "module_name": {"type": "string", "description": "Module name"},
                        "platform": {"type": "string", "description": "Platform name"},
                        "pdb_uri": {"type": "string", "description": "PDB/Symbol uri"},
                        "status": {
                            "type": "string",
                            "description": "available|deprecated",
                            "enum": ["available", "deprecated"],
                        },
                    },
                    "required": [
                        "build_id",
                        "module_name",
                        "platform",
                        "pdb_uri",
                        "status",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data, build_id=None, module_name=None, platform=None, pdb_uri=None, status=None):
        symbols = data.get("symbols", [])
        sym_id = f"AUTO::symbol::{build_id}::{module_name}"
        existing = next((s for s in symbols if s.get("id") == sym_id), None)
        if existing:
            existing.update(
                {
                    "build_id": build_id,
                    "module_name": module_name,
                    "platform": platform,
                    "pdb_uri": pdb_uri,
                    "status": status,
                }
            )
        else:
            symbols.append(
                {
                    "id": sym_id,
                    "build_id": build_id,
                    "module_name": module_name,
                    "platform": platform,
                    "pdb_uri": pdb_uri,
                    "status": status,
                }
            )
        data["symbols"] = symbols
        payload = {"symbol": next(s for s in symbols if s.get("id") == sym_id)}
        out = json.dumps(
            payload, indent=2
        )
        return out
