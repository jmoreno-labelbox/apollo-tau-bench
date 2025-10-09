from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class WritePitchExecutionGrades(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        grades_count = kwargs.get("grades_count")
        data.setdefault("pitch_execution_grades", []).append(
            {
                "grade_id": f"grade_{len(data.get('pitch_execution_grades', {}))+1}",
                "game_pk": game_pk,
                "grades_count": grades_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WritePitchExecutionGrades",
                "description": "Writes pitch execution grades to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "grades_count": {"type": "integer"},
                    },
                    "required": ["game_pk"],
                },
            },
        }
