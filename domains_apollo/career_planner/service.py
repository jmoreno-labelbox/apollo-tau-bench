# service.py
import json
from copy import deepcopy
from pathlib import Path
from typing import Dict, List, Any

from domains.base import BaseDomain
from domains.dto import Tool


class TalentManagementSystem(BaseDomain):
    """
    Domain-level service that exposes an in-memory database for
    recruiting, L&D, and people-analytics workflows.

    • All JSON files in ./data are loaded at startup.
    • `reset_database()` rolls everything back to the pristine snapshot
      taken at launch.
    """

    # ---- INITIALISATION --------------------------------------------------

    def __init__(self, tools: List[Tool]):
        super().__init__(tools)

        # one authoritative copy on disk ➜ master_database
        self.master_database: Dict[str, Any] = self._load_data()

        # scratch copy mutated by tool calls during a conversation
        self.database: Dict[str, Any] = deepcopy(self.master_database)

    # ---- PUBLIC API ------------------------------------------------------

    def reset_database(self) -> bool:
        """
        Restore the working copy (`self.database`) to the original
        on-disk state (`self.master_database`).

        Returns
        -------
        bool
            Always True (makes it easy to use in tests or tools chains).
        """
        self.database = deepcopy(self.master_database)
        return True

    # ---- INTERNAL HELPERS ------------------------------------------------

    def _load_data(self) -> Dict[str, Any]:
        """
        Read every JSON file in ./data that corresponds to a table name
        we care about.  Missing files or empty files are tolerated —
        they'll just load as empty lists so the tools don't crash.

        Returns
        -------
        Dict[str, Any]
            A dictionary keyed by table name, each value holding the
            parsed JSON content (usually a list of dicts).
        """
        data_dir = Path(__file__).parent / "data"

        # Add or remove table names here if your schema evolves.
        table_files = [
            # Core recruiting objects
            "job_postings",
            "job_applications",
            "talent_network",
            "shortlisted_candidates",      # written by tools at runtime

            # People data
            "users",
            "teams",
            "user_education",
            "user_certification",

            # Skill & learning
            "role_skill_catalog",
            "course_catalog",
            "user_course_progress",
            "skill_gap_analysis",
            "team_training_log",
            "goals",
            "soft_skills",

            # Mentorship
            "user_mentorship_relationships",
            "user_mentorship",
            "mentorship_strategies",

            # HR processes
            "hr_workflows",
            "training_recommendations",    # written by tools
            "recruiter_evaluations",       # written by tools
            "interviews"                   # written by tools
        ]

        db: Dict[str, Any] = {}

        for table_name in table_files:
            file_path = data_dir / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    raw = f.read().strip()
                    db[table_name] = json.loads(raw) if raw else []
            except FileNotFoundError:
                # Table hasn't been created on disk yet — start empty.
                db[table_name] = []
            except json.JSONDecodeError as err:
                # Corrupt JSON — surface the issue but keep the service alive.
                print(f"[WARN] Could not parse {file_path}: {err}")
                db[table_name] = []

        return db
