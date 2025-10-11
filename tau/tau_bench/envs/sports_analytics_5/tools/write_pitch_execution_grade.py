# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class WritePitchExecutionGrade(Tool):
    """Insert pitch_execution_grades based on miss_distance and (optional) model fields."""
    @staticmethod
    def invoke(data, actual_quadrant, game_pk, intended_quadrant_model, miss_distance_inches, pitch_id)->str:
        err = _require_tables(data, ["pitch_execution_grades"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["pitch_id","game_pk","intended_quadrant_model","actual_quadrant","miss_distance_inches"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["pitch_execution_grades"]
        new_id = _next_id(rows, "grade_id")
        grade = _grade_execution(miss_distance_inches)
        row = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": grade
        }
        rows.append(row)
        return json.dumps({"grade_id": new_id, "execution_grade": grade}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"write_pitch_execution_grade","description":"Creates a pitch_execution_grades row with deterministic grade policy.","parameters":{"type":"object","properties":{"pitch_id":{"type":"integer"},"game_pk":{"type":"integer"},"intended_quadrant_model":{"type":"string"},"actual_quadrant":{"type":"string"},"miss_distance_inches":{"type":"number"}},"required":["pitch_id","game_pk","intended_quadrant_model","actual_quadrant","miss_distance_inches"]}}}
