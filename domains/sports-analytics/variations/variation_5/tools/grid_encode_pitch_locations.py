from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GridEncodePitchLocations(Tool):
    """Calculate a 12x12 zone cell for each pitch (requires defined zone bounds). Optional persist=True will return data to pitches."""

    @staticmethod
    def invoke(data, min_x: float, max_x: float, min_z: float, max_z: float, persist: bool = False, game_pk: Any = None, scope: Any = None, cells_x: int = None, cells_z: int = None, return_rows: bool = None) -> str:
        pass
        if "pitches" not in data:
            payload = {"error": "Missing required table(s): pitches"}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"min_x": min_x, "max_x": max_x, "min_z": min_z, "max_z": max_z}, ["min_x", "max_x", "min_z", "max_z"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        mnx, mxx, mnz, mxz = map(float, (min_x, max_x, min_z, max_z))
        if not (mxx > mnx and mxz > mnz):
            payload = {"error": "Invalid bounds: require max_x>min_x and max_z>min_z"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        def _cell(x, z):
            pass
            if x is None or z is None:
                return None
            x = max(mnx, min(mxx, float(x)))
            z = max(mnz, min(mxz, float(z)))
            cx = int(((x - mnx) / (mxx - mnx)) * 12.0) + 1
            cz = int(((z - mnz) / (mxz - mnz)) * 12.0) + 1
            return f"{cx if cx<=12 else 12}-{cz if cz<=12 else 12}"

        out = []
        for p in data["pitches"]:
            out.append(
                {
                    "pitch_id": p.get("pitch_id"),
                    "zone_cell_12x12": _cell(p.get("plate_x"), p.get("plate_z")),
                }
            )

        if persist:
            #return data to the source table
            for p, rec in zip(data["pitches"], out):
                p["zone_cell_12x12"] = rec["zone_cell_12x12"]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GridEncodePitchLocations",
                "description": "Adds 12x12 zone cell labels for pitches given explicit bounds; optional persist=True writes back.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_x": {"type": "number"},
                        "max_x": {"type": "number"},
                        "min_z": {"type": "number"},
                        "max_z": {"type": "number"},
                        "persist": {"type": "boolean"},
                    },
                    "required": ["min_x", "max_x", "min_z", "max_z"],
                },
            },
        }
