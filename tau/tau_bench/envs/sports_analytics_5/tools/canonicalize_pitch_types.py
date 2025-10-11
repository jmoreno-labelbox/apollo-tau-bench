# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CanonicalizePitchTypes(Tool):
    """Write pitch_type_canonical for pitches lacking it using PITCH_MAP."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        if "pitches" not in data:
            return json.dumps({"error":"Missing required table(s): pitches"}, indent=2)
        updated = 0
        for p in data["pitches"]:
            raw = p.get("pitch_type_raw")
            if raw and not p.get("pitch_type_canonical"):
                p["pitch_type_canonical"] = PITCH_MAP.get(raw, raw)
                updated += 1
        return json.dumps({"updated_rows": updated}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"canonicalize_pitch_types","description":"Maps pitch_type_raw to canonical labels in pitches.","parameters":{"type":"object","properties":{},"required":[]}}}
