import json
from pathlib import Path
from typing import List, Dict, Any

from domains.base import BaseDomain
from domains.dto import Tool

import copy

class SportsAnalyticsSystem(BaseDomain):
    """
    Domain service for a sports analytics system.
    Manages the state of games, players, and other sports-related data.
    """
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):

        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        """
        Loads all data tables from their JSON files.
        """
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "bullpen_sessions",
            "curated_insights",
            "game_day_events",
            "games",
            "ingestion_logs",
            "pitch_execution_grades",
            "pitches",
            "player_dev_goals",
            "player_dev_reports",
            "players",
            "scouting_reports",
            "teams",
            "umpire_game_models",
            "umpires",
            "venues",
            "video_playlists",
            "workflow_runs",
        ]

        for table_name in table_files:
            file_path = data_path / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        db[table_name] = json.loads(content)
                    else:
                        db[table_name] = []
            except FileNotFoundError:
                db[table_name] = []
            except json.JSONDecodeError:
                db[table_name] = []
        return db
