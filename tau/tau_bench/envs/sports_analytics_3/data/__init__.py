import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from the files located in data/
    tables = ['bullpen_sessions', 'curated_insights', 'game_day_events', 'games', 'ingestion_logs', 'pitch_execution_grades', 'pitches', 'player_dev_goals', 'player_dev_reports', 'players', 'scouting_reports', 'teams', 'umpire_game_models', 'umpires', 'venues', 'video_playlists', 'workflow_runs']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

