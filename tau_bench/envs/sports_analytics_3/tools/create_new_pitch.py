from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateNewPitch(Tool):
    """
    Add a new pitch row with complete details.
    Required inputs (exact names):
      - game_pk (int)
      - at_bat_index (int)
      - pitch_number (int)
      - pitcher_id (int)
      - hitter_id (int)
      - pitch_type_raw (string)
      - pitch_type_canonical (string)
      - velocity_mph (number)
      - spin_rate_rpm (number)
      - release_x (number)
      - release_z (number)
      - plate_x (number)
      - plate_z (number)
      - exit_velocity_mph (number)
      - launch_angle_deg (number)
      - leverage_index (number)
    Behavior:
      - pitch_id is generated: max existing pitch_id + 1 (starts at 1).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        game_pk: int = None,
        at_bat_index: int = None,
        pitch_number: int = None,
        pitcher_id: int = None,
        hitter_id: int = None,
        pitch_type_raw: str = None,
        pitch_type_canonical: str = None,
        velocity_mph: float = None,
        spin_rate_rpm: float = None,
        release_x: float = None,
        release_z: float = None,
        plate_x: float = None,
        plate_z: float = None,
        exit_velocity_mph: float = None,
        launch_angle_deg: float = None,
        leverage_index: float = None
    ) -> str:
        required_fields = [
            "game_pk",
            "at_bat_index",
            "pitch_number",
            "pitcher_id",
            "hitter_id",
            "pitch_type_raw",
            "pitch_type_canonical",
            "velocity_mph",
            "spin_rate_rpm",
            "release_x",
            "release_z",
            "plate_x",
            "plate_z",
            "exit_velocity_mph",
            "launch_angle_deg",
            "leverage_index",
        ]
        missing = [
            f for f in required_fields if locals().get(f) is None
        ]
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(payload, indent=2)
            return out

        pitches: list[dict[str, Any]] = data.get("pitches", [])

        # Create a new pitch_id in a deterministic manner
        new_id = get_next_pitch_id(data)

        new_pitch = {"pitch_id": new_id}
        for f in required_fields:
            new_pitch[f] = locals().get(f)

        pitches.append(new_pitch)
        payload = new_pitch
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Construct JSON schema properties
        props: dict[str, Any] = {
            "game_pk": {"type": "integer"},
            "at_bat_index": {"type": "integer"},
            "pitch_number": {"type": "integer"},
            "pitcher_id": {"type": "integer"},
            "hitter_id": {"type": "integer"},
            "pitch_type_raw": {"type": "string"},
            "pitch_type_canonical": {"type": "string"},
            "velocity_mph": {"type": "number"},
            "spin_rate_rpm": {"type": "number"},
            "release_x": {"type": "number"},
            "release_z": {"type": "number"},
            "plate_x": {"type": "number"},
            "plate_z": {"type": "number"},
            "exit_velocity_mph": {"type": "number"},
            "launch_angle_deg": {"type": "number"},
            "leverage_index": {"type": "number"},
        }
        return {
            "type": "function",
            "function": {
                "name": "createNewPitch",
                "description": "Insert a new pitch with full details; pitch_id auto-generated.",
                "parameters": {
                    "type": "object",
                    "properties": props,
                    "required": list(props.keys()),
                },
            },
        }
