# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GridEncodePitchLocations(Tool):
    """Compute 12x12 zone cell for each pitch (requires explicit zone bounds). Optional persist=True writes back to pitches."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        if "pitches" not in data:
            return json.dumps({"error":"Missing required table(s): pitches"}, indent=2)
        need = _check_required(kwargs, ["min_x","max_x","min_z","max_z"])
        if need:
            return json.dumps({"error": need}, indent=2)
        mnx, mxx, mnz, mxz = map(float, (kwargs["min_x"], kwargs["max_x"], kwargs["min_z"], kwargs["max_z"]))
        if not (mxx > mnx and mxz > mnz):
            return json.dumps({"error":"Invalid bounds: require max_x>min_x and max_z>min_z"}, indent=2)

        def _cell(x, z):
            if x is None or z is None:
                return None
            x = max(mnx, min(mxx, float(x))); z = max(mnz, min(mxz, float(z)))
            cx = int(((x - mnx) / (mxx - mnx)) * 12.0) + 1
            cz = int(((z - mnz) / (mxz - mnz)) * 12.0) + 1
            return f"{cx if cx<=12 else 12}-{cz if cz<=12 else 12}"
        out = []
        for p in data["pitches"]:
            out.append({"pitch_id": p.get("pitch_id"), "zone_cell_12x12": _cell(p.get("plate_x"), p.get("plate_z"))})

        if kwargs.get("persist"):
            # write back to source table
            for p, rec in zip(data["pitches"], out):
                p["zone_cell_12x12"] = rec["zone_cell_12x12"]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"grid_encode_pitch_locations","description":"Adds 12x12 zone cell labels for pitches given explicit bounds; optional persist=True writes back.","parameters":{"type":"object","properties":{"min_x":{"type":"number"},"max_x":{"type":"number"},"min_z":{"type":"number"},"max_z":{"type":"number"},"persist":{"type":"boolean"}},"required":["min_x","max_x","min_z","max_z"]}}}
