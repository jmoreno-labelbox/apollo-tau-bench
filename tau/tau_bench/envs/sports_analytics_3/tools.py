import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def get_next_ingestion_id(data):
    pass
    nsr = len(data.get("ingestion_logs", {}))
    next_num = nsr + 1
    return next_num


def get_current_timestamp() -> str:
    pass
    return "2025-08-10T12:00:00Z"  #according to Rules for the current time


def get_next_game_id(data):
    pass
    ngames = len(data.get("games", {}))
    next_num = 2024000000 + ngames + 1
    return next_num


def get_next_pitch_id(data):
    pass
    npitch = len(data.get("pitches", {}))
    next_num = npitch + 1
    return next_num


def get_next_player_goal_id(data):
    pass
    ngoal = len(data.get("player_dev_goals", {}))
    next_num = ngoal + 1
    return next_num


def get_next_event_id(data):
    pass
    nevent = len(data.get("game_day_events", {}))
    next_num = nevent + 1
    return next_num


def get_next_scouting_report_id(data):
    pass
    nsr = len(data.get("scouting_reports", {}))
    next_num = nsr + 1
    return next_num


def get_next_dev_report_goal_id(data):
    pass
    ndev_report = len(data.get("player_dev_reports", {}))
    next_num = ndev_report + 1
    return next_num


def get_next_grade_id(data):
    pass
    ngrade = len(data.get("pitch_execution_grades", {}))
    next_num = ngrade + 1
    return next_num


def get_next_workflow_run_id(data):
    pass
    nsr = len(data.get("workflow_runs", {}))
    next_num = nsr + 1
    return f"run_{next_num}"


def get_next_insight_id(data):
    pass
    ninsight = len(data.get("curated_insights", {}))
    next_num = ninsight + 1
    return next_num


def get_next_highlight_id(data):
    pass
    nhighlight = len(data.get("video_playlists", {}))
    next_num = nhighlight + 1
    return next_num


def get_log_start_timestamp() -> str:
    pass
    return "2025-08-10T12:00:00Z"  #according to Rules for the current time


#def get_future_date() -> str:
#return "2025-09-10"


def get_today_date() -> str:
    pass
    return "2025-08-10"


def get_log_end_timestamp() -> str:
    pass
    return "2025-08-10T12:15:00Z"  #according to Rules for the current time


class GetPlayerDetailsByName(Tool):
    """Retrieve a player record using its full_name (exact match, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], full_name: str = None) -> str:
        #1) Confirm validity
        if not full_name:
            payload = {"error": "Missing required field: full_name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", {}).values()

        #3) Lookup for exact matches (without normalization)
        for player in players.values():
            if player.get("full_name") == full_name:
                payload = player
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No player found with full_name {full_name}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlayerDetailsByName",
                "description": "Fetch a single player's full details by exact full_name (case-sensitive, no normalization).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact player full name to retrieve (e.g., 'Evelyn Martin').",
                        }
                    },
                    "required": ["full_name"],
                },
            },
        }


class GetPlayerDetailsById(Tool):
    """Retrieve a player record using its player_id."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", {}).values()

        #3) Lookup for exact matches
        for player in players.values():
            if player.get("player_id") == player_id:
                payload = player
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No player found with ID {player_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlayerDetailsById",
                "description": "Fetch a single player's full details by their player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }


class GetAllPlayersOfTeam(Tool):
    """Retrieve all players associated with a specific team_id."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        #1) Confirm validity
        if team_id is None:
            payload = {"error": "Missing required field: team_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players: list[dict[str, Any]] = data.get("players", {}).values()

        #3) Filter players based on exact team_id
        matching_players = [
            player for player in players.values() if player.get("current_team_id") == team_id
        ]

        if not matching_players:
            payload = {"error": f"No players found for team_id {team_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching_players
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPlayersOfTeam",
                "description": "Fetch all player records belonging to the specified team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID whose players should be retrieved.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }


class UpdatePlayerDetails(Tool):
    """Modify a player's information: primary_position, current_team_id, and/or roster_status."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, primary_position: str = None, current_team_id: str = None, roster_status: str = None) -> str:
        #1) Confirm validity: player_id is required
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #At least one optional field must be included
        if all(v is None for v in [primary_position, current_team_id, roster_status]):
            payload = {
                    "error": "At least one of primary_position, current_team_id, or roster_status must be provided"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", {}).values()

        #3) Locate and modify player
        for player in players.values():
            if player.get("player_id") == player_id:
                if primary_position is not None:
                    player["primary_position"] = primary_position
                if current_team_id is not None:
                    player["current_team_id"] = current_team_id
                if roster_status is not None:
                    player["roster_status"] = roster_status
                payload = player
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No player found with ID {player_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updatePlayerDetails",
                "description": (
                    "Update a player's primary_position, current_team_id, and/or roster_status. "
                    "At least one of these optional fields must be provided."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to update.",
                        },
                        "primary_position": {
                            "type": "string",
                            "description": "New primary position of the player.",
                        },
                        "current_team_id": {
                            "type": "integer",
                            "description": "New team ID for the player.",
                        },
                        "roster_status": {
                            "type": "string",
                            "description": "New roster status for the player.",
                        },
                    },
                    "required": ["player_id"],
                },
            },
        }


class GetTeamDetailsById(Tool):
    """Retrieve a team record using its team_id."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        #1) Confirm validity
        if team_id is None:
            payload = {"error": "Missing required field: team_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", {}).values()

        #3) Lookup for exact matches
        for team in teams.values():
            if team.get("team_id") == team_id:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with ID {team_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsById",
                "description": "Fetch a single team's full details by its team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID to retrieve.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }


class GetTeamDetailsByName(Tool):
    """Retrieve a team record using its team_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", {}).values()

        #3) Lookup for exact matches (without normalization)
        for team in teams.values():
            if team.get("team_name") == name:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with name {name}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsByName",
                "description": "Fetch a single team's full details by exact team_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact team name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class GetTeamDetailsByAbbreviation(Tool):
    """Retrieve a team record using its abbreviation (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], abbreviation: str = None) -> str:
        #1) Confirm validity
        if not isinstance(abbreviation, str) or abbreviation == "":
            payload = {"error": "Missing required field: abbreviation"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", {}).values()

        #3) Lookup for exact matches (without normalization)
        for team in teams.values():
            if team.get("abbreviation") == abbreviation:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with abbreviation {abbreviation}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsByAbbreviation",
                "description": "Fetch a single team's full details by exact abbreviation (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "abbreviation": {
                            "type": "string",
                            "description": "Exact team abbreviation to retrieve (e.g., 'NYM').",
                        }
                    },
                    "required": ["abbreviation"],
                },
            },
        }


class GetAllTeamsInLeague(Tool):
    """Retrieve all teams associated with a specific league."""

    @staticmethod
    def invoke(data: dict[str, Any], league: str = None) -> str:
        #1) Confirm validity
        if not isinstance(league, str) or league == "":
            payload = {"error": "Missing required field: league"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams: list[dict[str, Any]] = data.get("teams", {}).values()

        #3) Filter teams based on exact league
        matching_teams = [team for team in teams.values() if team.get("league") == league]

        if not matching_teams:
            payload = {"error": f"No teams found in league {league}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching_teams
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllTeamsInLeague",
                "description": "Fetch all team records belonging to the specified league (exact, case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "league": {
                            "type": "string",
                            "description": "Exact league name to retrieve teams for (e.g., 'American League').",
                        }
                    },
                    "required": ["league"],
                },
            },
        }


class GetGameDetailsByGamePk(Tool):
    """Retrieve a game record using its game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Lookup for exact matches
        for game in games:
            if game.get("game_pk") == game_pk:
                payload = game
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No game found with game_pk {game_pk}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGameDetailsByGamePk",
                "description": "Fetch a single game's full details by its game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key to retrieve.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }


class UpdateGameDetails(Tool):
    """
    Modify a game's details using exact input names:
      - Required: gamepk
      - Optional (at least one must be provided): status, score, attendance

    Business rule:
      - final_score ("score") and attendance can only be modified when the game's
        resulting status is 'Final'. This implies:
          * If you provide score/attendance without status, the current game
            status must already be 'Final'.
          * If you provide status along with score/attendance, that status must be
            'Final' in the same request.
    """

    @staticmethod
    def invoke(data: dict[str, Any], gamepk: int = None, status: str = None, score: int = None, attendance: int = None) -> str:
        #1) Confirm presence
        if gamepk is None:
            payload = {"error": "Missing required field: gamepk"}
            out = json.dumps(payload, indent=2)
            return out

        if status is None and score is None and attendance is None:
            payload = {
                    "error": "At least one of status, score, or attendance must be provided"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Locate the game
        target = None
        for game in games:
            if game.get("game_pk") == gamepk:
                target = game
                break

        if target is None:
            payload = {"error": f"No game found with game_pk {gamepk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Apply business rule regarding 'Final' status for score/attendance
        #Establish the resulting status following this update
        resulting_status = status if status is not None else target.get("game_status")

        #If attempting to modify score/attendance, the resulting status must be 'Final'
        wants_score_or_attendance_change = (score is not None) or (
            attendance is not None
        )
        if wants_score_or_attendance_change and resulting_status != "Final":
            payload = {
                    "error": "Cannot change score or attendance unless the game status is 'Final' "
                    "(either already Final or set to 'Final' in this request)."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #5) Implement updates in a deterministic manner (only specified fields)
        if status is not None:
            target["game_status"] = status
        if score is not None:
            target["final_score"] = score
        if attendance is not None:
            target["attendance"] = attendance
        payload = target
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateGameDetails",
                "description": (
                    "Update a game's status, score, and/or attendance by exact gamepk. "
                    "At least one of the optional fields must be provided. "
                    "Score and attendance may only be changed when the resulting status is 'Final'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "gamepk": {
                            "type": "integer",
                            "description": "Exact game primary key to update.",
                        },
                        "status": {
                            "type": ["string", "null"],
                            "description": "New game status (e.g., 'Scheduled', 'Final', 'Postponed') or null.",
                        },
                        "score": {
                            "type": ["string", "null"],
                            "description": "New final score text (e.g., '5-3') or null. "
                            "Can only be changed when status is 'Final'.",
                        },
                        "attendance": {
                            "type": ["integer", "null"],
                            "description": "New attendance value or null. "
                            "Can only be changed when status is 'Final'.",
                        },
                    },
                    "required": ["gamepk"],
                },
            },
        }


class CreateNewGame(Tool):
    """
    Establish a new game row.
      Inputs (exact names):
        - date (YYYY-MM-DD)
        - venue_id (int)
        - home_team_id (int)
        - away_team_id (int)
      Behavior:
        - game_pk is automatically generated (max existing game_pk + 1; starts at 1 if none).
        - game_status defaults to "Scheduled".
        - final_score and attendance default to null.
    """

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None, venue_id: int = None, home_team_id: int = None, away_team_id: int = None) -> str:
        #1) Confirm required inputs
        missing = []
        if not isinstance(date, str) or date == "":
            missing.append("date")
        if venue_id is None:
            missing.append("venue_id")
        if home_team_id is None:
            missing.append("home_team_id")
        if away_team_id is None:
            missing.append("away_team_id")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB using provided data
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Create a new unique game_pk in a deterministic manner based on DB state

        #4) Establish the new game row with default values
        new_row = {
            "game_pk": get_next_game_id(data),
            "game_date": date,
            "venue_id": venue_id,
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_status": "Scheduled",
            "final_score": None,
            "attendance": None,
        }

        #5) Add
        games.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNewGame",
                "description": (
                    "Create a new game. Generates game_pk automatically (max existing + 1). "
                    "Defaults game_status to 'Scheduled'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Game date in YYYY-MM-DD.",
                        },
                        "venue_id": {"type": "integer", "description": "Venue ID."},
                        "home_team_id": {
                            "type": "integer",
                            "description": "Home team ID.",
                        },
                        "away_team_id": {
                            "type": "integer",
                            "description": "Away team ID.",
                        },
                    },
                    "required": ["date", "venue_id", "home_team_id", "away_team_id"],
                },
            },
        }


class FindGamesOnDate(Tool):
    """Retrieve all games planned for a specific date (YYYY-MM-DD)."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        #1) Confirm validity
        if not isinstance(date, str) or date == "":
            payload = {"error": "Missing required field: date (YYYY-MM-DD)"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Exact match on game_date (without normalization)
        matching = [g for g in games.values() if g.get("game_date") == date]

        if not matching:
            payload = {"error": f"No games found on date {date}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindGamesOnDate",
                "description": "Fetch all games that have game_date equal to the given date (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Target date in YYYY-MM-DD (exact match against game_date).",
                        }
                    },
                    "required": ["date"],
                },
            },
        }


class GetNextGame(Tool):
    """
    Retrieve the next Scheduled game that occurs strictly after a specified date.
    If team_id is provided, only consider games where that team is either home or away.

    Inputs:
      - current_date (YYYY-MM-DD) [required]
      - team_id (int) [optional]

    Selection criteria:
      - Only games with game_status == "Scheduled"
      - game_date must be > current_date (strictly after)
      - If there are multiple options, select the earliest game_date; use smallest game_pk
        as a tie-breaker for determinism.
    """

    @staticmethod
    def invoke(data: dict[str, Any], current_date: str = None, team_id: str = None) -> str:
        #1) Confirm validity
        if not isinstance(current_date, str) or current_date == "":
            payload = {"error": "Missing required field: current_date (YYYY-MM-DD)"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Filter future games that are eligible
        def is_eligible(g: dict[str, Any]) -> bool:
            if g.get("game_status") != "Scheduled":
                return False
            if g.get("game_date", "") <= current_date:
                return False
            if team_id is None:
                return True
            return g.get("home_team_id") == team_id or g.get("away_team_id") == team_id

        future = [g for g in games.values() if is_eligible(g)]

        if not future:
            target = (
                f"after {current_date}"
                if team_id is None
                else f"for team_id {team_id} after {current_date}"
            )
            payload = {"error": f"No next scheduled game {target}"}
            out = json.dumps(payload, indent=2)
            return out

        #4) Deterministic selection: earliest date first, then smallest game_pk
        future.sort(key=lambda g: (g.get("game_date", ""), g.get("game_pk", 0)))
        payload = future[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextGame",
                "description": "Return the next Scheduled game strictly after current_date; optionally filter by team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {
                            "type": "string",
                            "description": "Current date in YYYY-MM-DD; next game must be strictly after this date.",
                        },
                        "team_id": {
                            "type": "integer",
                            "description": "Optional team filter; include games where this team is home or away.",
                        },
                    },
                    "required": ["current_date"],
                },
            },
        }


class GetGameByHomeAway(Tool):
    """
    Retrieve a single game using exact home/away team IDs.

    Inputs (exact names; case-sensitive):
      - home (int)  : home team ID
      - awy  (int)  : away team ID

    Behavior:
      - Exact match on home_team_id and away_team_id.
      - If multiple games match, return the one with the earliest game_date;
        use smallest game_pk as a tie-breaker for determinism.
      - Returns a structured error if no match is found.
    """

    @staticmethod
    def invoke(data: dict[str, Any], home_id: str = None, away_id: str = None) -> str:
        import json

        home = home_id
        away = away_id

        #1) Confirm required inputs
        missing = []
        if home is None:
            missing.append("home")
        if away is None:
            missing.append("awy")
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Access DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Filter for exact matches
        matches = [
            g
            for g in games
            if g.get("home_team_id") == home and g.get("away_team_id") == away
        ]

        if not matches:
            payload = {
                    "error": f"No game found with home_team_id {home} and away_team_id {away}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Deterministic selection: earliest date first, then smallest game_pk
        matches.sort(key=lambda g: (g.get("game_date", ""), int(g.get("game_pk", 0))))
        payload = matches[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGameByHomeAway",
                "description": "Fetch a single game by exact home and away team IDs. If multiple, returns the earliest by date, then smallest game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_id": {
                            "type": "integer",
                            "description": "Exact home team ID.",
                        },
                        "away_id": {
                            "type": "integer",
                            "description": "Exact away team ID.",
                        },
                    },
                    "required": ["home_id", "away_id"],
                },
            },
        }


class GetVenueById(Tool):
    """Retrieve a venue record using its venue_id."""

    @staticmethod
    def invoke(data: dict[str, Any], venue_id: str = None) -> str:
        #1) Confirm validity
        if venue_id is None:
            payload = {"error": "Missing required field: venue_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        venues: list[dict[str, Any]] = data.get("venues", {}).values()

        #3) Lookup for exact matches
        for venue in venues:
            if venue.get("venue_id") == venue_id:
                payload = venue
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No venue found with ID {venue_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVenueById",
                "description": "Fetch a single venue's full details by venue_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "venue_id": {
                            "type": "integer",
                            "description": "Exact venue ID to retrieve.",
                        }
                    },
                    "required": ["venue_id"],
                },
            },
        }


class GetVenueByName(Tool):
    """Retrieve a venue record using its venue_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        venues: list[dict[str, Any]] = data.get("venues", {}).values()

        #3) Exact match (without normalization)
        for venue in venues:
            if venue.get("venue_name") == name:
                payload = venue
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No venue found with name {name}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getVenueByName",
                "description": "Fetch a single venue's full details by exact venue_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact venue name to retrieve (e.g., 'Charlotte').",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class GetAllVenueInCity(Tool):
    """Retrieve all venues situated in a specific city (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], city: str = None) -> str:
        #1) Confirm validity
        if not isinstance(city, str) or city == "":
            payload = {"error": "Missing required field: city"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        venues: list[dict[str, Any]] = data.get("venues", {}).values()

        #3) Filter for exact city
        matching = [v for v in venues.values() if v.get("city") == city]

        if not matching:
            payload = {"error": f"No venues found in city {city}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllVenueInCity",
                "description": "Fetch all venue records whose city exactly matches the provided value (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "Exact city name (e.g., 'Kansas City').",
                        }
                    },
                    "required": ["city"],
                },
            },
        }


class GetUmpiresDetailsByName(Tool):
    """Retrieve an umpire record using full_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], full_name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(full_name, str) or full_name == "":
            payload = {"error": "Missing required field: full_name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", {}).values()

        #3) Exact match (without normalization)
        for ump in umpires:
            if ump.get("full_name") == full_name:
                payload = ump
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No umpire found with full_name {full_name}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUmpiresDetailsByName",
                "description": "Fetch a single umpire's full details by exact full_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact umpire full name to retrieve.",
                        }
                    },
                    "required": ["full_name"],
                },
            },
        }


class GetUmpiresDetailsById(Tool):
    """Retrieve an umpire record using umpire_id."""

    @staticmethod
    def invoke(data: dict[str, Any], umpire_id: str = None) -> str:
        #1) Confirm validity
        if umpire_id is None:
            payload = {"error": "Missing required field: umpire_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", {}).values()

        #3) Lookup for exact matches
        for ump in umpires:
            if ump.get("umpire_id") == umpire_id:
                payload = ump
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No umpire found with ID {umpire_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUmpiresDetailsById",
                "description": "Fetch a single umpire's full details by umpire_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "umpire_id": {
                            "type": "integer",
                            "description": "Exact umpire ID to retrieve.",
                        }
                    },
                    "required": ["umpire_id"],
                },
            },
        }


class GetUmpiresByExperience(Tool):
    """
    Retrieve all umpires with years_experience exceeding a specified threshold,
    sorted by years_experience in descending order (ties resolved by smallest umpire_id).
    """

    @staticmethod
    def invoke(data: dict[str, Any], min_experience: int = None) -> str:
        #1) Confirm validity
        if min_experience is None:
            payload = {"error": "Missing required field: experience"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", {}).values()

        #3) Filter for individuals with experience exceeding threshold
        filtered = [
            ump
            for ump in umpires
            if int(ump.get("years_experience", 0)) > min_experience
        ]

        if not filtered:
            payload = {
                    "error": f"No umpires found with experience greater than {min_experience}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Sort in a deterministic manner
        sorted_list = sorted(
            filtered,
            key=lambda u: (
                -int(u.get("years_experience", 0)),
                int(u.get("umpire_id", 0)),
            ),
        )
        payload = sorted_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUmpiresByExperience",
                "description": "Return all umpires with years_experience greater than the provided threshold, sorted in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "experience": {
                            "type": "integer",
                            "description": "Minimum years_experience threshold; only umpires with greater experience are returned.",
                        }
                    },
                    "required": ["min_experience"],
                },
            },
        }


class GetAllEevntsByGamePk(Tool):
    """
    Retrieve all game-day events for a specified game_pk.

    Notes:
      - Exact match on game_pk (without normalization).
      - Results are sorted deterministically by timestamp_utc ascending, then event_id ascending.
      - Expects the events array within data["game_day_events"].
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        events: list[dict[str, Any]] = data.get("game_day_events", {}).values()

        #3) Filter for exact game_pk
        matching = [e for e in events.values() if e.get("game_pk") == game_pk]

        if not matching:
            payload = {"error": f"No events found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matching.sort(
            key=lambda e: (e.get("timestamp_utc", ""), int(e.get("event_id", 0)))
        )
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllEevntsByGamePk",
                "description": "Fetch all game-day events for the specified game_pk (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key whose events should be returned.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }


class CreateGameDayEvent(Tool):
    """
    Establish a new game-day event.
    Inputs (exact names):
      - game_pk (int) [required]
      - pitch_id (int) [required]
      - leverage_index (float or int) [required]
      - is_manual_alert (bool) [required]
      - suggestion_text (string) [required]
    Behavior:
      - event_id is automatically generated (max existing event_id + 1; starts at 1 if none).
      - draft_status defaults to "Draft".
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        game_pk: int = None,
        pitch_id: int = None,
        leverage_index: float = None,
        is_manual_alert: bool = None,
        suggestion_text: str = None
    ) -> str:
        #1) Confirm required inputs
        missing = []
        if game_pk is None:
            missing.append("game_pk")
        if leverage_index is None:
            missing.append("leverage_index")
        if is_manual_alert is None:
            missing.append("is_manual_alert")
        if not isinstance(suggestion_text, str) or suggestion_text == "":
            missing.append("suggestion_text")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        events: list[dict[str, Any]] = data.get("game_day_events", {}).values()

        #4) Establish a new event row
        new_event = {
            "event_id": get_next_event_id(data),
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": get_current_timestamp(),  #May be populated later if necessary
            "leverage_index": leverage_index,
            "is_manual_alert": is_manual_alert,
            "suggestion_text": suggestion_text,
            "draft_status": "draft",
        }

        #5) Add to DB
        events.append(new_event)
        payload = new_event
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGameDayEvent",
                "description": (
                    "Create a new game-day event. event_id is generated automatically "
                    "(max existing + 1). draft_status defaults to 'Draft'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key this event belongs to.",
                        },
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID associated with the event.",
                        },
                        "leverage_index": {
                            "type": "number",
                            "description": "Leverage index for the event.",
                        },
                        "is_manual_alert": {
                            "type": "boolean",
                            "description": "True if the alert is manually triggered, else False.",
                        },
                        "suggestion_text": {
                            "type": "string",
                            "description": "Suggestion text for the event.",
                        },
                    },
                    "required": [
                        "game_pk",
                        "leverage_index",
                        "is_manual_alert",
                        "suggestion_text",
                    ],
                },
            },
        }


class UpdateGameEventStatus(Tool):
    """
    Modify the draft_status of a current game-day event.

    Inputs:
      - event_id (int) [required]
      - draft_status (string) [required]
    """

    @staticmethod
    def invoke(data: dict[str, Any], event_id: str = None, draft_status: str = None) -> str:
        #1) Confirm validity
        if event_id is None:
            payload = {"error": "Missing required field: event_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(draft_status, str) or draft_status == "":
            payload = {"error": "Missing required field: draft_status"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        events: list[dict[str, Any]] = data.get("game_day_events", {}).values()

        #3) Locate and modify
        for event in events:
            if event.get("event_id") == event_id:
                event["draft_status"] = draft_status
                payload = event
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No event found with event_id {event_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateGameEventStatus",
                "description": "Update the draft_status of a game-day event identified by event_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "integer",
                            "description": "Exact event ID to update.",
                        },
                        "draft_status": {
                            "type": "string",
                            "description": "New draft status for the event (e.g., 'draft', 'published', 'archived').",
                        },
                    },
                    "required": ["event_id", "draft_status"],
                },
            },
        }


class GetAllGoalsByForPlayer(Tool):
    """Retrieve all development goals associated with a specific player_id."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        goals: list[dict[str, Any]] = data.get("player_dev_goals", {}).values()

        #3) Filter goals related to player
        matching = [g for g in goals.values() if g.get("player_id") == player_id]

        if not matching:
            payload = {"error": f"No goals found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllGoalsByForPlayer",
                "description": "Fetch all development goals for a given player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve goals for.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }


class CreateNewGoal(Tool):
    """
    Establish a new player development goal.
    Required:
      - dev_report_id
      - player_id
      - goal_text
      - coach_id
      - target_review_date (YYYY-MM-DD)
    Defaults:
      - goal_id is auto-generated
      - goal_status = "Active"
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        dev_report_id: str = None,
        player_id: str = None,
        goal_text: str = None,
        coach_id: str = None,
        target_review_date: str = None
    ) -> str:
        # Confirm required
        missing = []
        for field, val in [
            ("dev_report_id", dev_report_id),
            ("player_id", player_id),
            (
                "goal_text",
                goal_text if isinstance(goal_text, str) and goal_text.strip() else None,
            ),
            ("coach_id", coach_id),
            (
                "target_review_date",
                (
                    target_review_date
                    if isinstance(target_review_date, str)
                    and target_review_date.strip()
                    else None
                ),
            ),
        ]:
            if val is None:
                missing.append(field)

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        goals: list[dict[str, Any]] = data.get("player_dev_goals", {}).values()

        new_goal = {
            "goal_id": get_next_player_goal_id(data),
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": "Active",
            "coach_id": coach_id,
            "target_review_date": target_review_date,
        }
        goals.append(new_goal)
        payload = new_goal
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewGoal",
                "description": "Create a new player development goal. goal_id auto-generated; goal_status defaults to 'Active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {
                            "type": "integer",
                            "description": "Development report ID associated with the goal.",
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the goal is for.",
                        },
                        "goal_text": {
                            "type": "string",
                            "description": "Description of the development goal.",
                        },
                        "coach_id": {
                            "type": "integer",
                            "description": "Coach ID who set the goal.",
                        },
                        "target_review_date": {
                            "type": "string",
                            "description": "Target review date in YYYY-MM-DD.",
                        },
                    },
                    "required": [
                        "dev_report_id",
                        "player_id",
                        "goal_text",
                        "coach_id",
                        "target_review_date",
                    ],
                },
            },
        }


class CreateNewReport(Tool):
    """
    Establish a new player development report.
    Required inputs (exact names):
      - player_id (int)
      - week_of_date (string, YYYY-MM-DD)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
    Behavior:
      - dev_report_id is auto-generated: max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, week_of_date: str = None) -> str:
        #1) Confirm required inputs
        missing = []
        if player_id is None:
            missing.append("player_id")
        if not isinstance(week_of_date, str) or week_of_date == "":
            missing.append("week_of_date")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("player_dev_reports", {}).values()

        new_id = get_next_dev_report_goal_id(data)

        #4) Construct and add the row
        new_row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": get_current_timestamp(),
            "s3_pdf_path": f"s3://reports/development/{new_id}.pdf",
        }
        reports.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewReport",
                "description": "Create a new player development report. dev_report_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the report belongs to.",
                        },
                        "week_of_date": {
                            "type": "string",
                            "description": "Week-of date in YYYY-MM-DD.",
                        },
                    },
                    "required": ["player_id", "week_of_date"],
                },
            },
        }


class GetAllReportForPlayer(Tool):
    """
    Retrieve all development reports associated with a specific player_id.
    Results are sorted deterministically by week_of_date in descending order, then dev_report_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("player_dev_reports", {}).values()

        #3) Filter and arrange
        matching = [r for r in reports.values() if r.get("player_id") == player_id]

        if not matching:
            payload = {"error": f"No reports found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllReportForPlayer",
                "description": "Fetch all development reports for the specified player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve reports for.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }


class GetPitchDetailsById(Tool):
    """Retrieve a single pitch using its pitch_id."""

    @staticmethod
    def invoke(data: dict[str, Any], pitch_id: str = None) -> str:
        #1) Confirm validity
        if pitch_id is None:
            payload = {"error": "Missing required field: pitch_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

        #3) Lookup for exact matches
        for p in pitches:
            if p.get("pitch_id") == pitch_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No pitch found with pitch_id {pitch_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPitchDetailsById",
                "description": "Fetch a single pitch's full details by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID to retrieve.",
                        }
                    },
                    "required": ["pitch_id"],
                },
            },
        }


class GetAllPitchesByPitcherIds(Tool):
    """Retrieve all pitches delivered by any pitcher in the supplied list of pitcher_ids."""

    @staticmethod
    def invoke(data: dict[str, Any], pitcher_ids: list[int] = None) -> str:
        #1) Confirm validity
        if not isinstance(pitcher_ids, list) or len(pitcher_ids) == 0:
            payload = {
                    "error": "Missing required field: pitcher_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

        #3) Apply filter
        id_set = set(pitcher_ids)
        matches = [p for p in pitches.values() if p.get("pitcher_id") in id_set]
        if not matches:
            payload = {"error": f"No pitches found for pitcher_ids {pitcher_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        #matches.sort(
        #key=lambda p: (
        #int(p.get("game_pk", 0)),
        #int(p.get("at_bat_index", 0)),
        #int(p.get("pitch_number", 0)),
        #int(p.get("pitch_id", 0)),
        #)
        #)
        pitch_ids = [int(p.get("pitch_id", 0)) for p in matches]
        #Remove duplicates while maintaining order, just in case
        pitch_ids = list(dict.fromkeys(pitch_ids))

        payload = {
            "pitch_ids": pitch_ids,
            "pitches": matches,
        }
        payload = payload
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesByPitcherIds",
                "description": "Fetch all pitches where pitcher_id is in pitcher_ids. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitcher IDs.",
                        }
                    },
                    "required": ["pitcher_ids"],
                },
            },
        }


class GetAllPitchesByHitterIds(Tool):
    """Retrieve all pitches encountered by any hitter in the supplied list of hitter_ids."""

    @staticmethod
    def invoke(data: dict[str, Any], hitter_ids: list[int] = None) -> str:
        #1) Confirm validity
        if not isinstance(hitter_ids, list) or len(hitter_ids) == 0:
            payload = {
                    "error": "Missing required field: hitter_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

        #3) Apply filter
        id_set = set(hitter_ids)
        matches = [p for p in pitches.values() if p.get("hitter_id") in id_set]
        if not matches:
            payload = {"error": f"No pitches found for hitter_ids {hitter_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        matches.sort(
            key=lambda p: (
                int(p.get("game_pk", 0)),
                int(p.get("at_bat_index", 0)),
                int(p.get("pitch_number", 0)),
                int(p.get("pitch_id", 0)),
            )
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesByHitterIds",
                "description": "Fetch all pitches where hitter_id is in the provided list. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hitter_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of hitter IDs.",
                        }
                    },
                    "required": ["hitter_ids"],
                },
            },
        }


class GetAllPitchesForGame(Tool):
    """Retrieve all pitches associated with a specific game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

        #3) Filter and order deterministically within the game
        result = [p for p in pitches.values() if p.get("game_pk") == game_pk]
        if not result:
            payload = {"error": f"No pitches found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        result.sort(
            key=lambda p: (
                p.get("at_bat_index", 0),
                p.get("pitch_number", 0),
                p.get("pitch_id", 0),
            )
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesForGame",
                "description": "Fetch all pitches belonging to a specific game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }


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

        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

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


class GetGradeByPitchId(Tool):
    """Retrieve the execution grade record for a specific pitch_id."""

    @staticmethod
    def invoke(data: dict[str, Any], pitch_id: str = None) -> str:
        #1) Confirm validity
        if pitch_id is None:
            payload = {"error": "Missing required field: pitch_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Lookup for exact matches
        for rec in grades:
            if rec.get("pitch_id") == pitch_id:
                payload = rec
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No grade found for pitch_id {pitch_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGradeByPitchId",
                "description": "Fetch a single pitch execution grade record by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID whose grade should be returned.",
                        }
                    },
                    "required": ["pitch_id"],
                },
            },
        }


class GetGradesByPitchIds(Tool):
    """
    Retrieve execution grade records for a collection of pitch IDs.
    Returns all matching rows sorted deterministically by pitch_id in ascending order, grade_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], pitch_ids: list[int] = None,
    grades: Any = None,
    ) -> str:
        #1) Confirm validity
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            payload = {
                    "error": "Missing required field: pitch_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Gather matches
        id_set = set(pitch_ids)
        matches = [rec for rec in grades.values() if rec.get("pitch_id") in id_set]

        if not matches:
            payload = {"No grades found": f"No grades found for pitch_ids {pitch_ids}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGradesByPitchIds",
                "description": "Fetch execution grade records for the given list of pitch IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of pitch IDs to retrieve grades for.",
                        }
                    },
                    "required": ["pitch_ids"],
                },
            },
        }


class GetFilteredGradesByPitchIds(Tool):
    """
    Retrieve execution grade records for a collection of pitch IDs, then EXCLUDE any rows
    whose execution_grade matches the provided grades list.

    Inputs (exact names; case-sensitive):
      - pitch_ids (List[int]) : Non-empty list of pitch IDs to search.
      - grades    (List[str]) : Non-empty list of grade labels to EXCLUDE
                                (exact, case-sensitive match, e.g., ["C", "D", "F"]).

    Behavior:
      - Looks up all rows where rec.pitch_id is in pitch_ids.
      - Excludes rows where rec.execution_grade is in grades.
      - Returns results sorted deterministically by (pitch_id in ascending order, grade_id in ascending order).
      - If no rows match the pitch_ids, returns a structured error.
      - If rows match pitch_ids but all are excluded by grades, returns a structured error.
    """

    @staticmethod
    def invoke(data: dict[str, Any], pitch_ids: list[int] = None, grades_to_exclude: list[str] = None,
    grades: Any = None,
    ) -> str:
        #---- 1) Confirm inputs
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            payload = {
                    "error": "Missing required field: pitch_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if not isinstance(grades_to_exclude, list) or len(grades_to_exclude) == 0:
            payload = {
                    "error": "Missing required field: grades (non-empty list of strings to EXCLUDE)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #---- 2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #---- 3) Gather matches based on pitch_ids
        id_set = set(pitch_ids)
        initial = [rec for rec in grades.values() if rec.get("pitch_id") in id_set]

        if not initial:
            payload = {"error": f"No grades found for pitch_ids {pitch_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #---- 4) Exclude records where execution_grade matches grades_to_exclude (exact, case-sensitive)
        excl_set = set(grades_to_exclude)
        filtered = [rec for rec in initial.values() if rec.get("execution_grade") in excl_set]

        if not filtered:
            payload = {
                    "error": (
                        "All grades were filtered out. No remaining records after excluding "
                        f"{sorted(excl_set)} for pitch_ids {pitch_ids}"
                    )
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #---- 5) Sort deterministically: pitch_id ASC, grade_id ASC
        filtered.sort(
            key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0)))
        )
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilteredGradesByPitchIds",
                "description": "Fetch execution grade records for given pitch IDs and EXCLUDE rows whose execution_grade matches any provided grade.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitch IDs to retrieve grades for.",
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Non-empty list of grade labels to EXCLUDE (exact, case-sensitive).",
                        },
                    },
                    "required": ["pitch_ids", "grades"],
                },
            },
        }


class CreateNewGrade(Tool):
    """
    Establish a new pitch execution grade.
    Required fields:
      - pitch_id (int)
      - game_pk (int)
      - intended_quadrant_model (string)
      - actual_quadrant (string)
      - miss_distance_inches (float)
      - execution_grade (string)
    Auto-generates grade_id as max existing + 1 (starting at 1).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        pitch_id: int = None,
        game_pk: int = None,
        intended_quadrant_model: str = None,
        actual_quadrant: str = None,
        miss_distance_inches: float = None,
        execution_grade: str = None
    ) -> str:
        #1) Confirm required fields
        missing = []
        if pitch_id is None:
            missing.append("pitch_id")
        if game_pk is None:
            missing.append("game_pk")
        if intended_quadrant_model is None:
            missing.append("intended_quadrant_model")
        if actual_quadrant is None:
            missing.append("actual_quadrant")
        if miss_distance_inches is None:
            missing.append("miss_distance_inches")
        if not isinstance(execution_grade, str) or execution_grade == "":
            missing.append("execution_grade")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Create a new grade_id
        new_id = get_next_grade_id(data)

        #4) Establish a new record
        new_record = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": execution_grade,
        }
        grades.append(new_record)
        payload = new_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewGrade",
                "description": "Create a new pitch execution grade with auto-generated grade_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID this grade belongs to.",
                        },
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key.",
                        },
                        "intended_quadrant_model": {
                            "type": "integer",
                            "description": "Intended quadrant from the model.",
                        },
                        "actual_quadrant": {
                            "type": "integer",
                            "description": "Actual quadrant observed.",
                        },
                        "miss_distance_inches": {
                            "type": "number",
                            "description": "Distance missed in inches.",
                        },
                        "execution_grade": {
                            "type": "string",
                            "description": "Execution grade value.",
                        },
                    },
                    "required": [
                        "pitch_id",
                        "game_pk",
                        "intended_quadrant_model",
                        "actual_quadrant",
                        "miss_distance_inches",
                        "execution_grade",
                    ],
                },
            },
        }


class GetGradesByGradeForGame(Tool):
    """
    Retrieve all pitch execution grade records for a specified game that match any of the
    provided grade values.

    Inputs:
      - game_pk (int)           [required]
      - grades (List[str])      [required] list of execution_grade values to match

    Behavior:
      - Exact (case-sensitive) match on execution_grade.
      - Filters records where record.game_pk equals game_pk AND record.execution_grade is in grades.
      - Deterministic ordering by pitch_id in ascending order, then grade_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None, grades: list[str] = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(grades, list) or len(grades) == 0:
            payload = {"error": "Missing required field: grades (non-empty list of strings)"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        records: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Apply filter (exact, case-sensitive)
        allowed = set(grades)
        matches = [
            r
            for r in records
            if r.get("game_pk") == game_pk and r.get("execution_grade") in allowed
        ]

        if not matches:
            payload = {
                    "error": f"No grades found for game_pk {game_pk} with execution_grade in {grades}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Order deterministically
        matches.sort(
            key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGradesByGradeForGame",
                "description": "Fetch pitch execution grade records for a game where execution_grade matches any of the provided values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key to filter on.",
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of execution_grade values to match (case-sensitive).",
                        },
                    },
                    "required": ["game_pk", "grades"],
                },
            },
        }


class GetHighlightsByName(Tool):
    """
    Retrieve a highlight playlist using its name.
    Inputs:
      - name (string) [required]  # The suffix; code will prepend 'Game Highlights - '
    Behavior:
      - Compute full_name = "Game Highlights - " + name and return the corresponding playlist.
      - If multiple matches occur (unlikely), return the one with the smallest playlist_id for determinism.
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        full_name = f"Game Highlights - {name}"

        #2) Retrieve DB
        playlists: list[dict[str, Any]] = data.get("video_playlists", {}).values()

        #3) Search for exact matches (without normalization)
        matches = [p for p in playlists.values() if p.get("playlist_name") == full_name]

        if not matches:
            payload = {"error": f"No playlist found with name '{full_name}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        payload = matches[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHighlightsByName",
                "description": "Return the 'Game Highlights - <name>' playlist (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix after 'Game Highlights - ' to look up.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class AddNewHighlight(Tool):
    """
    Increase an existing highlight playlist's clip_count, or establish a new one if it doesn't exist.

    Inputs (exact names):
      - name (string)       [required]  # The suffix; code will prepend 'Game Highlights - '
      - clip_count (integer) [required]

    Behavior:
      - Compute full_name = "Game Highlights - " + name (no normalization).
      - If a playlist with playlist_name == full_name exists, increase clip_count by clip_count.
      - Otherwise, create a new row with:
          playlist_id = max existing + 1 (or 1 if none),
          report_id = null,
          internal_portal_link = null,
        clip_count = clip_count.
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, clip_count: int = None, report_id: int = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out
        if clip_count is None:
            payload = {"error": "Missing required field: clip_count"}
            out = json.dumps(payload, indent=2)
            return out

        full_name = f"Game Highlights - {name}"

        #2) Retrieve DB
        playlists: list[dict[str, Any]] = data.get("video_playlists", {}).values()

        #3) Attempt to locate existing
        target = None
        for p in playlists:
            if p.get("playlist_name") == full_name:
                target = p
                break

        #4) Modify or establish
        if target is not None:
            #Increase clip_count
            current = int(target.get("clip_count", 0))
            target["clip_count"] = current + int(clip_count)
            payload = target
            out = json.dumps(payload, indent=2)
            return out

        #Establish new
        new_id = get_next_highlight_id(data)
        new_row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": full_name,
            "internal_portal_link": f"https://internal.baseball.com/playlists/{new_id}",
            "clip_count": int(clip_count),
        }
        playlists.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewHighlight",
                "description": "Add clip_count to an existing 'Game Highlights - <name>' playlist, or create it if missing. Optionally set report_id if creating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix to append after 'Game Highlights - '.",
                        },
                        "clip_count": {
                            "type": "integer",
                            "description": "Number of clips to add (used as initial count if created).",
                        },
                        "report_id": {
                            "type": ["integer", "null"],
                            "description": "Optional report ID to associate when creating new.",
                        },
                    },
                    "required": ["name", "clip_count"],
                },
            },
        }


class GetHighlightByReportId(Tool):
    """Retrieve all video playlists linked to a specific report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        playlists: list[dict[str, Any]] = data.get("video_playlists", {}).values()

        #3) Lookup for exact matches (without normalization)
        matches = [p for p in playlists.values() if p.get("report_id") == report_id]

        if not matches:
            payload = {"error": f"No video playlists found for report_id {report_id}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHighlightByReportId",
                "description": "Fetch all video playlists whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": ["integer", "string"],
                            "description": "Exact report ID to filter by.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }


class GetPlayerInsightsByPlayeridAndType(Tool):
    """
    Retrieve player insights using player_id and type filter.

    Inputs (exact names):
      - player_id (int) [required]
      - type (string)   [required]
          * Use "all" to return all insights for the player
          * Or provide an exact insight_type (e.g., "Performance", "Health", "Development", "Strategic", "Mechanical")

    Behavior:
      - Exact match (case-sensitive) on insight_type when type is not "all"
      - Deterministic ordering by insight_id in ascending order
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, type: str = None) -> str:
        type_filter = type
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(type_filter, str) or type_filter == "":
            payload = {"error": "Missing required field: type"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        insights: list[dict[str, Any]] = data.get("curated_insights", {}).values()

        #3) Filter based on player_id
        player_insights = [i for i in insights.values() if i.get("player_id") == player_id]

        if not player_insights:
            payload = {"error": f"No insights found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Implement type filter
        if type_filter != "all":
            player_insights = [
                i for i in player_insights if i.get("insight_type") == type_filter
            ]
            if not player_insights:
                payload = {
                        "error": f"No insights found for player_id {player_id} with type '{type_filter}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        #5) Order deterministically
        player_insights.sort(key=lambda i: int(i.get("insight_id", 0)))
        payload = player_insights
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlayerInsightsByPlayeridAndType",
                "description": (
                    "Fetch curated insights for a player. Pass type='All' to get all insights, "
                    "or an exact insight_type (e.g., 'Performance') for a specific subset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID whose insights to retrieve.",
                        },
                        "type": {
                            "type": "string",
                            "description": "Use 'All' or provide an exact insight_type (case-sensitive).",
                        },
                    },
                    "required": ["player_id", "type"],
                },
            },
        }


class CreateNewInsight(Tool):
    """
    Establish a new curated insight.

    Required inputs (exact names):
      - report_id (int)
      - player_id (int)
      - insight_text (string, non-empty)
      - insight_type (string, non-empty)
      - supporting_stat_value (number)

    Behavior:
      - insight_id is auto-generated as max existing + 1 (starting at 1).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        report_id: str = None,
        player_id: str = None,
        insight_text: str = None,
        insight_type: str = None,
        supporting_stat_value: Any = None
    ) -> str:
        #1) Confirm required inputs
        missing = []
        if report_id is None:
            missing.append("report_id")
        if player_id is None:
            missing.append("player_id")
        if not isinstance(insight_text, str) or insight_text.strip() == "":
            missing.append("insight_text")
        if not isinstance(insight_type, str) or insight_type.strip() == "":
            missing.append("insight_type")
        if supporting_stat_value is None:
            missing.append("supporting_stat_value")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        insights: list[dict[str, Any]] = data.get("curated_insights", {}).values()

        #3) Create a new insight_id in a deterministic manner
        new_id = get_next_insight_id(data)

        #4) Construct and add the row
        new_row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value,
        }
        insights.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewInsight",
                "description": "Create a new curated insight; insight_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Report ID this insight is associated with.",
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID this insight refers to.",
                        },
                        "insight_text": {
                            "type": "string",
                            "description": "Human-readable insight text.",
                        },
                        "insight_type": {
                            "type": "string",
                            "description": "Category/type of the insight (case-sensitive).",
                        },
                        "supporting_stat_value": {
                            "type": "number",
                            "description": "Numeric value that supports the insight.",
                        },
                    },
                    "required": [
                        "report_id",
                        "player_id",
                        "insight_text",
                        "insight_type",
                        "supporting_stat_value",
                    ],
                },
            },
        }


class GetInsightbyreportid(Tool):
    """Retrieve all curated insights linked to a specific report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        insights: list[dict[str, Any]] = data.get("curated_insights", {}).values()

        #3) Lookup for exact matches (without normalization)
        matches = [i for i in insights.values() if i.get("report_id") == report_id]

        if not matches:
            payload = {"error": f"No insights found for report_id {report_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda i: int(i.get("insight_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getInsightByReportId",
                "description": "Fetch all curated insights whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to filter insights by.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }


class GetScoutingReportByGamepkAndType(Tool):
    """
    Retrieve scouting reports using game_pk, with optional filtering by report_type.

    Inputs (exact names):
      - game_pk (int)       [required]
      - report_type (str)   [optional] exact, case-sensitive

    Behavior:
      - If report_type is provided, return only exact matches.
      - If not provided, return all reports for the game.
      - Deterministic ordering: created_at in ascending order, then report_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None, report_type: str = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Apply filter
        matches = [r for r in reports.values() if r.get("game_pk") == game_pk]
        if report_type is not None:
            matches = [r for r in matches.values() if r.get("report_type") == report_type]

        if not matches:
            if report_type is None:
                payload = {"error": f"No scouting reports found for game_pk {game_pk}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            payload = {
                    "error": f"No scouting reports found for game_pk {game_pk} with type '{report_type}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Sort in a deterministic manner
        matches.sort(
            key=lambda r: (r.get("created_at", ""), int(r.get("report_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getScoutingReportByGamepkAndType",
                "description": "Fetch scouting reports for a game; optionally filter by exact report_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key.",
                        },
                        "report_type": {
                            "type": "string",
                            "description": "Optional exact report type (case-sensitive).",
                        },
                    },
                    "required": ["game_pk"],
                },
            },
        }


class CreateScoutingReport(Tool):
    """
    Establish a new scouting report.

    Required inputs (exact names):
      - report_type (string)
      - game_pk (int)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
      - gslides_link (string)
      - core_narrative_text (string)

    Behavior:
      - report_id is auto-generated: max existing + 1 (starting at 1).
    """

    @staticmethod
    def invoke(data: dict[str, Any], report_type: str = None, game_pk: Any = None, core_narrative_text: str = None) -> str:
        #1) Confirm validity
        missing = []
        if not isinstance(report_type, str) or report_type == "":
            missing.append("report_type")
        if game_pk is None:
            missing.append("game_pk")
        if not isinstance(core_narrative_text, str) or core_narrative_text == "":
            missing.append("core_narrative_text")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Create a new id
        new_id = get_next_scouting_report_id(data)

        #4) Add
        new_row = {
            "report_id": new_id,
            "report_type": report_type,
            "game_pk": game_pk,
            "created_at": get_today_date(),
            "s3_pdf_path": f"s3://reports/scouting/{new_id}.pdf",
            "gslides_link": f"https://docs.google.com/presentation/d/{new_id}",
            "core_narrative_text": core_narrative_text,
        }
        reports.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        props = {
            "report_type": {
                "type": "string",
                "description": "e.g., 'Pre-Game', 'Post-Game', 'Opponent Analysis', 'Series Summary', 'Player Focus'",
            },
            "game_pk": {
                "type": "integer",
                "description": "Game primary key this report is about.",
            },
            "core_narrative_text": {
                "type": "string",
                "description": "Main narrative text for the report.",
            },
        }
        return {
            "type": "function",
            "function": {
                "name": "CreateScoutingReport",
                "description": "Create a new scouting report; report_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": props,
                    "required": list(props.keys()),
                },
            },
        }


class GetScoutingReportById(Tool):
    """Retrieve a single scouting report using its report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Lookup for exact matches
        for report in reports:
            if report.get("report_id") == report_id:
                payload = report
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No scouting report found with ID {report_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getScoutingReportById",
                "description": "Fetch a single scouting report's full details by its report_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to retrieve.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }


class CreateWorkflow(Tool):
    """
    Establish a new workflow run with deterministic behavior for the provided data.
    Inputs:
      - dag_name (str)    : DAG name
      - game_pk (int)     : Game PK (nullable)
      - status (str)      : Initial status
      - end_time_utc (str): End time in UTC (YYYY-MM-DD HH:MM:SS)
      - log_s3_path (str) : Optional log path, defaults to None
    Output:
      - Created workflow run object
    """

    @staticmethod
    def invoke(data: dict[str, Any], dag_name: str = None, game_pk: int = None, status: str = None) -> str:
        # Confirm required fields
        missing = [f for f in ["dag_name", "status"] if locals().get(f) is None]
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        workflows = data.get("workflow_runs", {}).values()
        run_id = get_next_workflow_run_id(data)
        start_time = get_log_start_timestamp()
        end_time = get_log_end_timestamp()
        log_path = f"s3://logs/workflows/{run_id}.log"

        new_entry = {
            "run_id": run_id,
            "dag_name": dag_name,
            "game_pk": game_pk,
            "status": status,
            "start_time_utc": start_time,
            "end_time_utc": end_time,
            "log_s3_path": log_path,
        }

        data["workflow_runs"][new_entry["workflow_run_id"]] = new_entry
        payload = new_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkflow",
                "description": "Create a new workflow run entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": ["integer", "null"]},
                        "status": {"type": "string"},
                    },
                    "required": ["dag_name", "status"],
                },
            },
        }


class GetBullpenSessionInfoForPlayer(Tool):
    """
    Retrieve bullpen sessions for a specified player with optional filters.

    Inputs (exact names; case-sensitive):
      - playerid (int)          : Required. Player ID to filter on (matches 'player_id').
      - date (str, optional)    : Exact session date 'YYYY-MM-DD' (matches 'session_date').
      - type (str, optional)    : Exact pitch type (matches 'pitch_type_canonical').

    Behavior:
      - Exact matching on the provided filters (without normalization).
      - Results are sorted deterministically by session_date in ascending order, then session_id in ascending order.
      - If no matching records are found, returns a structured error.
    """

    @staticmethod
    def invoke(data: dict[str, Any], playerid: str = None, date: str = None, type: str = None) -> str:
        pass
        date_filter = date
        type_filter = type

        #1) Confirm required input
        if playerid is None:
            payload = {"error": "Missing required field: playerid"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Access DB
        sessions: list[dict[str, Any]] = data.get("bullpen_sessions", {}).values()

        #3) Filter based on exact fields
        def match(session: dict[str, Any]) -> bool:
            pass
            if session.get("player_id") != playerid:
                return False
            if date_filter is not None and session.get("session_date") != date_filter:
                return False
            if (
                type_filter is not None
                and session.get("pitch_type_canonical") != type_filter
            ):
                return False
            return True

        matches = [s for s in sessions.values() if match(s)]

        if not matches:
            #Construct a clear, structured error
            parts = [f"player_id {playerid}"]
            if date_filter is not None:
                parts.append(f"date {date_filter}")
            if type_filter is not None:
                parts.append(f"type {type_filter}")
            payload = {"error": f"No bullpen sessions found for {'; '.join(parts)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(
            key=lambda s: (s.get("session_date", ""), int(s.get("session_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBullpenSessionInfoForPlayer",
                "description": "Fetch bullpen sessions for a player with optional exact filters on date and pitch type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "playerid": {
                            "type": "integer",
                            "description": "Exact player ID (matches 'player_id').",
                        },
                        "date": {
                            "type": "string",
                            "description": "Exact session date in YYYY-MM-DD (matches 'session_date').",
                        },
                        "type": {
                            "type": "string",
                            "description": "Exact pitch type (matches 'pitch_type_canonical').",
                        },
                    },
                    "required": ["playerid"],
                },
            },
        }


class CreateIngestionLog(Tool):
    """
    Establish a new ingestion log entry.

    Inputs (exact names; case-sensitive):
      - source_name (str)                [required]
      - status_code (int)                [required]
      - records_ingested (int)           [required]
      - request_timestamp_utc (str)      [optional] 'YYYY-MM-DD HH:MM:SS'
          If omitted, defaults deterministically to '2025-08-10 12:00:00'.

    Behavior:
      - ingestion_id is auto-generated as count(ingestion_logs) + 1.
      - Exact types are required; no coercion.
      - Appends the new record to data["ingestion_logs"] and returns it.
    """

    @staticmethod
    def invoke(data: dict[str, Any], source_name: str = None, status_code: int = None, records_ingested: int = None, request_timestamp_utc: str = "2025-08-10 12:00:00") -> str:
        #1) Confirm required fields
        missing = []
        if source_name is None:
            missing.append("source_name")
        if status_code is None:
            missing.append("status_code")
        if records_ingested is None:
            missing.append("records_ingested")
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Access DB
        logs: list[dict[str, Any]] = data.get("ingestion_logs", {}).values()

        #3) Create a new ingestion_id in a deterministic manner
        new_id = get_next_ingestion_id(data)

        #4) Establish record
        new_row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": get_current_timestamp(),
            "status_code": status_code,
            "records_ingested": records_ingested,
        }

        #5) Add
        logs.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIngestionLog",
                "description": "Create a new ingestion log record; ingestion_id auto-generated (count + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "Name of the ingestion source (e.g., 'mlb_api', 'trackman').",
                        },
                        "status_code": {
                            "type": "integer",
                            "description": "HTTP-like status code of the ingestion attempt.",
                        },
                        "records_ingested": {
                            "type": "integer",
                            "description": "Number of records successfully ingested.",
                        },
                        "request_timestamp_utc": {
                            "type": "string",
                            "description": "UTC timestamp 'YYYY-MM-DD HH:MM:SS' (optional). Defaults to '2025-08-10 12:00:00' if omitted.",
                        },
                    },
                    "required": ["source_name", "status_code", "records_ingested"],
                },
            },
        }


class GetModelDetailByGame(Tool):
    """
    Retrieve per-game umpire model calibration details.

    Input:
      - game_pk (int): Exact game_pk to look up.

    Behavior:
      - Reads from data["umpire_game_models"].
      - Returns all matching rows, sorted deterministically by umpire_game_id in ascending order.
      - If no match is found, returns a clear error payload.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        models: list[dict[str, Any]] = data.get("umpire_game_models", {}).values()

        #3) Gather matches
        matches = [row for row in models.values() if row.get("game_pk") == game_pk]

        if not matches:
            payload = {"error": f"No model details found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda r: int(r.get("umpire_game_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelDetailByGame",
                "description": "Return umpire model calibration details for a given game_pk (sorted by umpire_game_id ASC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game identifier (game_pk).",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }


TOOLS = [
    GetPlayerDetailsByName(),
    GetPlayerDetailsById(),
    GetAllPlayersOfTeam(),
    UpdatePlayerDetails(),
    GetTeamDetailsById(),
    GetTeamDetailsByName(),
    GetTeamDetailsByAbbreviation(),
    GetAllTeamsInLeague(),
    GetGameDetailsByGamePk(),
    UpdateGameDetails(),
    CreateNewGame(),
    FindGamesOnDate(),
    GetNextGame(),
    GetGameByHomeAway(),
    GetVenueById(),
    GetVenueByName(),
    GetAllVenueInCity(),
    GetUmpiresDetailsByName(),
    GetUmpiresDetailsById(),
    GetUmpiresByExperience(),
    GetAllEevntsByGamePk(),
    CreateGameDayEvent(),
    UpdateGameEventStatus(),
    GetAllGoalsByForPlayer(),
    CreateNewGoal(),
    CreateNewReport(),
    GetAllReportForPlayer(),
    GetPitchDetailsById(),
    GetAllPitchesByPitcherIds(),
    GetAllPitchesByHitterIds(),
    GetAllPitchesForGame(),
    CreateNewPitch(),
    GetGradeByPitchId(),
    GetGradesByPitchIds(),
    GetFilteredGradesByPitchIds(),
    CreateNewGrade(),
    GetGradesByGradeForGame(),
    GetHighlightsByName(),
    AddNewHighlight(),
    GetHighlightByReportId(),
    GetPlayerInsightsByPlayeridAndType(),
    CreateNewInsight(),
    GetInsightbyreportid(),
    GetScoutingReportByGamepkAndType(),
    CreateScoutingReport(),
    GetScoutingReportById(),
    CreateWorkflow(),
    GetBullpenSessionInfoForPlayer(),
    CreateIngestionLog(),
    GetModelDetailByGame(),
]
#49
