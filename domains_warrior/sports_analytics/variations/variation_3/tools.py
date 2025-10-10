import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict, List
from domains.dto import Tool


def get_next_game_id(data):
    ngames = len(data.get("games", []))
    next_num = 2024000000 + ngames + 1
    return next_num

def get_next_event_id(data):
    nevent = len(data.get("game_day_events", []))
    next_num = nevent + 1
    return next_num

def get_next_player_goal_id(data):
    ngoal = len(data.get("player_dev_goals", []))
    next_num = ngoal + 1
    return next_num

def get_next_dev_report_goal_id(data):
    ndev_report = len(data.get("player_dev_reports", []))
    next_num = ndev_report + 1
    return next_num

def get_next_pitch_id(data):
    npitch = len(data.get("pitches", []))
    next_num = npitch + 1
    return next_num

def get_next_grade_id(data):
    ngrade = len(data.get("pitch_execution_grades", []))
    next_num = ngrade + 1
    return next_num

def get_next_highlight_id(data):
    nhighlight = len(data.get("video_playlists", []))
    next_num = nhighlight + 1
    return next_num

def get_next_insight_id(data):
    ninsight = len(data.get("curated_insights", []))
    next_num = ninsight + 1
    return next_num

def get_next_scouting_report_id(data):
    nsr = len(data.get("scouting_reports", []))
    next_num = nsr + 1
    return next_num

def get_next_ingestion_id(data):
    nsr = len(data.get("ingestion_logs", []))
    next_num = nsr + 1
    return next_num

def get_next_workflow_run_id(data):
    nsr = len(data.get("workflow_runs", []))
    next_num = nsr + 1
    return  f"run_{next_num}"

def get_current_timestamp() -> str:
    return "2025-08-10T12:00:00Z" # per Now Time according to Rules

def get_log_start_timestamp() -> str:
    return "2025-08-10T12:00:00Z" # per Now Time according to Rules

def get_log_end_timestamp() -> str:
    return "2025-08-10T12:15:00Z" # per Now Time according to Rules


# def get_future_date() -> str:
#     return "2025-09-10"

def get_today_date() -> str:
    return "2025-08-10"


class GetPlayerDetailsByName(Tool):
    """Fetch a player record by its full_name (exact match, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        full_name = kwargs.get("full_name")

        # 1) Validate
        if not full_name:
            return json.dumps({"error": "Missing required field: full_name"}, indent=2)

        # 2) Get DB from passed-in data
        players = data.get("players", [])

        # 3) Exact match lookup (no normalization)
        for player in players:
            if player.get("full_name") == full_name:
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with full_name {full_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_details_by_name",
                "description": "Fetch a single player's full details by exact full_name (case-sensitive, no normalization).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact player full name to retrieve (e.g., 'Jennifer Roberts')."
                        }
                    },
                    "required": ["full_name"]
                }
            }
        }    

class GetPlayerDetailsById(Tool):
    """Fetch a player record by its player_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB from passed-in data
        players = data.get("players", [])

        # 3) Exact match lookup
        for player in players:
            if player.get("player_id") == player_id:
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with ID {player_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_details_by_id",
                "description": "Fetch a single player's full details by their player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
    
class GetAllPlayersOfTeam(Tool):
    """Fetch all players belonging to a given team_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")

        # 1) Validate
        if team_id is None:
            return json.dumps({"error": "Missing required field: team_id"}, indent=2)

        # 2) Get DB from passed-in data
        players: List[Dict[str, Any]] = data.get("players", [])

        # 3) Filter players by exact team_id
        matching_players = [
            player for player in players
            if player.get("current_team_id") == team_id
        ]

        if not matching_players:
            return json.dumps({"error": f"No players found for team_id {team_id}"}, indent=2)

        return json.dumps(matching_players, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_players_of_team",
                "description": "Fetch all player records belonging to the specified team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID whose players should be retrieved."
                        }
                    },
                    "required": ["team_id"]
                }
            }
        }
    
class UpdatePlayerDetails(Tool):

    """Update a player's details: primary_position, current_team_id, and/or roster_status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")
        primary_position = kwargs.get("primary_position")
        current_team_id = kwargs.get("current_team_id")
        roster_status = kwargs.get("roster_status")

        # 1) Validate: player_id must be provided
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # At least one of the optional fields should be present
        if all(v is None for v in [primary_position, current_team_id, roster_status]):
            return json.dumps({"error": "At least one of primary_position, current_team_id, or roster_status must be provided"}, indent=2)

        # 2) Get DB from passed-in data
        players = data.get("players", [])

        # 3) Find and update player
        for player in players:
            if player.get("player_id") == player_id:
                if primary_position is not None:
                    player["primary_position"] = primary_position
                if current_team_id is not None:
                    player["current_team_id"] = current_team_id
                if roster_status is not None:
                    player["roster_status"] = roster_status
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with ID {player_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_player_details",
                "description": (
                    "Update a player's primary_position, current_team_id, and/or roster_status. "
                    "At least one of these optional fields must be provided."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to update."
                        },
                        "primary_position": {
                            "type": "string",
                            "description": "New primary position of the player."
                        },
                        "current_team_id": {
                            "type": "integer",
                            "description": "New team ID for the player."
                        },
                        "roster_status": {
                            "type": "string",
                            "description": "New roster status for the player."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
    

class GetTeamDetailsById(Tool):
    """Fetch a team record by its team_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")

        # 1) Validate
        if team_id is None:
            return json.dumps({"error": "Missing required field: team_id"}, indent=2)

        # 2) Get DB from passed-in data
        teams = data.get("teams", [])

        # 3) Exact match lookup
        for team in teams:
            if team.get("team_id") == team_id:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with ID {team_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_id",
                "description": "Fetch a single team's full details by its team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID to retrieve."
                        }
                    },
                    "required": ["team_id"]
                }
            }
        }

class GetTeamDetailsByName(Tool):
    """Fetch a team record by its team_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        # 1) Validate
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        # 2) Get DB from passed-in data
        teams = data.get("teams", [])

        # 3) Exact match lookup (no normalization)
        for team in teams:
            if team.get("team_name") == name:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with name {name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_name",
                "description": "Fetch a single team's full details by exact team_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact team name to retrieve."
                        }
                    },
                    "required": ["name"]
                }
            }
        }

class GetTeamDetailsByAbbreviation(Tool):
    """Fetch a team record by its abbreviation (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        abbreviation = kwargs.get("abbreviation")

        # 1) Validate
        if not isinstance(abbreviation, str) or abbreviation == "":
            return json.dumps({"error": "Missing required field: abbreviation"}, indent=2)

        # 2) Get DB from passed-in data
        teams = data.get("teams", [])

        # 3) Exact match lookup (no normalization)
        for team in teams:
            if team.get("abbreviation") == abbreviation:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with abbreviation {abbreviation}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_abbreviation",
                "description": "Fetch a single team's full details by exact abbreviation (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "abbreviation": {
                            "type": "string",
                            "description": "Exact team abbreviation to retrieve (e.g., 'NYM')."
                        }
                    },
                    "required": ["abbreviation"]
                }
            }
        }

class GetAllTeamsInLeague(Tool):
    """Fetch all teams belonging to a given league."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        league = kwargs.get("league")

        # 1) Validate
        if not isinstance(league, str) or league == "":
            return json.dumps({"error": "Missing required field: league"}, indent=2)

        # 2) Get DB from passed-in data
        teams: List[Dict[str, Any]] = data.get("teams", [])

        # 3) Filter teams by exact league
        matching_teams = [
            team for team in teams
            if team.get("league") == league
        ]

        if not matching_teams:
            return json.dumps({"error": f"No teams found in league {league}"}, indent=2)

        return json.dumps(matching_teams, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_teams_in_league",
                "description": "Fetch all team records belonging to the specified league (exact, case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "league": {
                            "type": "string",
                            "description": "Exact league name to retrieve teams for (e.g., 'American League')."
                        }
                    },
                    "required": ["league"]
                }
            }
        }


class GetGameDetailsByGamePk(Tool):
    """Fetch a game record by its game_pk."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Exact match lookup
        for game in games:
            if game.get("game_pk") == game_pk:
                return json.dumps(game, indent=2)

        return json.dumps({"error": f"No game found with game_pk {game_pk}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_game_details_by_game_pk",
                "description": "Fetch a single game's full details by its game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key to retrieve."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }

class UpdateGameDetails(Tool):
    """
    Update a game's details using exact input names:
      - Required: gamepk
      - Optional (at least one must be provided): status, score, attendance

    Business rule:
      - final_score ("score") and attendance can be changed ONLY when the game's
        resulting status is 'Final'. This means:
          * If you pass score/attendance without passing status, the current game
            status must already be 'Final'.
          * If you pass status together with score/attendance, that status must be
            'Final' in the same request.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        gamepk = kwargs.get("gamepk")
        status = kwargs.get("status")
        score = kwargs.get("score")
        attendance = kwargs.get("attendance")

        # 1) Validate presence
        if gamepk is None:
            return json.dumps({"error": "Missing required field: gamepk"}, indent=2)

        if status is None and score is None and attendance is None:
            return json.dumps(
                {"error": "At least one of status, score, or attendance must be provided"},
                indent=2
            )

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Find the game
        target = None
        for game in games:
            if game.get("game_pk") == gamepk:
                target = game
                break

        if target is None:
            return json.dumps({"error": f"No game found with game_pk {gamepk}"}, indent=2)

        # 4) Enforce business rule about 'Final' status for score/attendance
        # Determine the resulting status after this update
        resulting_status = status if status is not None else target.get("game_status")

        # If trying to change score/attendance, resulting status must be 'Final'
        wants_score_or_attendance_change = (score is not None) or (attendance is not None)
        if wants_score_or_attendance_change and resulting_status != "Final":
            return json.dumps(
                {"error": "Cannot change score or attendance unless the game status is 'Final' "
                          "(either already Final or set to 'Final' in this request)."},
                indent=2
            )

        # 5) Apply updates deterministically (only provided fields)
        if status is not None:
            target["game_status"] = status
        if score is not None:
            target["final_score"] = score
        if attendance is not None:
            target["attendance"] = attendance

        return json.dumps(target, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_game_details",
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
                            "description": "Exact game primary key to update."
                        },
                        "status": {
                            "type": ["string", "null"],
                            "description": "New game status (e.g., 'Scheduled', 'Final', 'Postponed') or null."
                        },
                        "score": {
                            "type": ["string", "null"],
                            "description": "New final score text (e.g., '5-3') or null. "
                                           "Can only be changed when status is 'Final'."
                        },
                        "attendance": {
                            "type": ["integer", "null"],
                            "description": "New attendance value or null. "
                                           "Can only be changed when status is 'Final'."
                        }
                    },
                    "required": ["gamepk"]
                }
            }
        }

class CreateNewGame(Tool):
    """
    Create a new game row.
      Inputs (exact names):
        - date (YYYY-MM-DD)
        - venue_id (int)
        - home_team_id (int)
        - away_team_id (int)
      Behavior:
        - game_pk is generated automatically (max existing game_pk + 1; starts at 1 if empty).
        - game_status defaults to "Scheduled".
        - final_score and attendance default to null.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        venue_id = kwargs.get("venue_id")
        home_team_id = kwargs.get("home_team_id")
        away_team_id = kwargs.get("away_team_id")

        # 1) Validate required inputs
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
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB from passed-in data
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Generate a new unique game_pk deterministically from DB state
        

        # 4) Create the new game row with defaults
        new_row = {
            "game_pk": get_next_game_id(data),
            "game_date": date,
            "venue_id": venue_id,
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_status": "Scheduled",
            "final_score": None,
            "attendance": None
        }

        # 5) Insert
        games.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_game",
                "description": (
                    "Create a new game. Generates game_pk automatically (max existing + 1). "
                    "Defaults game_status to 'Scheduled'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Game date in YYYY-MM-DD."
                        },
                        "venue_id": {
                            "type": "integer",
                            "description": "Venue ID."
                        },
                        "home_team_id": {
                            "type": "integer",
                            "description": "Home team ID."
                        },
                        "away_team_id": {
                            "type": "integer",
                            "description": "Away team ID."
                        }
                    },
                    "required": ["date", "venue_id", "home_team_id", "away_team_id"]
                }
            }
        }

class FindGamesOnDate(Tool):
    """Fetch all games scheduled on an exact date (YYYY-MM-DD)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")

        # 1) Validate
        if not isinstance(date, str) or date == "":
            return json.dumps({"error": "Missing required field: date (YYYY-MM-DD)"}, indent=2)

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Exact match on game_date (no normalization)
        matching = [g for g in games if g.get("game_date") == date]

        if not matching:
            return json.dumps({"error": f"No games found on date {date}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_games_on_date",
                "description": "Fetch all games that have game_date equal to the given date (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Target date in YYYY-MM-DD (exact match against game_date)."
                        }
                    },
                    "required": ["date"]
                }
            }
        }

class GetNextGame(Tool):
    """
    Return the next Scheduled game strictly after a given date.
    If team_id is provided, only consider games where that team is home or away.

    Inputs:
      - current_date (YYYY-MM-DD) [required]
      - team_id (int) [optional]

    Selection rule:
      - Only games with game_status == "Scheduled"
      - game_date must be > current_date (strictly after)
      - If multiple candidates, pick the earliest game_date; tie-break by smallest game_pk
        for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_date= kwargs.get("current_date")
        team_id= kwargs.get("team_id")

        # 1) Validate
        if not isinstance(current_date, str) or current_date == "":
            return json.dumps({"error": "Missing required field: current_date (YYYY-MM-DD)"}, indent=2)

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Filter eligible future games
        def is_eligible(g: Dict[str, Any]) -> bool:
            if g.get("game_status") != "Scheduled":
                return False
            if g.get("game_date", "") <= current_date:
                return False
            if team_id is None:
                return True
            return g.get("home_team_id") == team_id or g.get("away_team_id") == team_id

        future = [g for g in games if is_eligible(g)]

        if not future:
            target = f"after {current_date}" if team_id is None else f"for team_id {team_id} after {current_date}"
            return json.dumps({"error": f"No next scheduled game {target}"}, indent=2)

        # 4) Deterministic selection: earliest date, then smallest game_pk
        future.sort(key=lambda g: (g.get("game_date", ""), g.get("game_pk", 0)))
        return json.dumps(future[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_next_game",
                "description": "Return the next Scheduled game strictly after current_date; optionally filter by team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {
                            "type": "string",
                            "description": "Current date in YYYY-MM-DD; next game must be strictly after this date."
                        },
                        "team_id": {
                            "type": "integer",
                            "description": "Optional team filter; include games where this team is home or away."
                        }
                    },
                    "required": ["current_date"]
                }
            }
        }
    
class GetGameByHomeAway(Tool):
    """
    Fetch a single game by exact home/away team IDs.

    Inputs (exact names; case-sensitive):
      - home (int)  : home team ID
      - awy  (int)  : away team ID

    Behavior:
      - Exact match on home_team_id and away_team_id.
      - If multiple games match, return the one with the earliest game_date;
        tie-break by smallest game_pk for determinism.
      - Returns a structured error if no match is found.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json

        home = kwargs.get("home_id")
        away = kwargs.get("away_id")

        # 1) Validate required inputs
        missing = []
        if home is None:
            missing.append("home")
        if away is None:
            missing.append("awy")
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Access DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Filter by exact match
        matches = [
            g for g in games
            if g.get("home_team_id") == home and g.get("away_team_id") == away
        ]

        if not matches:
            return json.dumps(
                {"error": f"No game found with home_team_id {home} and away_team_id {away}"},
                indent=2
            )

        # 4) Deterministic selection: earliest date, then smallest game_pk
        matches.sort(key=lambda g: (g.get("game_date", ""), int(g.get("game_pk", 0))))
        return json.dumps(matches[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_game_by_home_away",
                "description": "Fetch a single game by exact home and away team IDs. If multiple, returns the earliest by date, then smallest game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_id": {
                            "type": "integer",
                            "description": "Exact home team ID."
                        },
                        "away_id": {
                            "type": "integer",
                            "description": "Exact away team ID."
                        }
                    },
                    "required": ["home_id", "away_id"]
                }
            }
        }



class GetVenueById(Tool):
    """Fetch a venue record by its venue_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        venue_id = kwargs.get("venue_id")

        # 1) Validate
        if venue_id is None:
            return json.dumps({"error": "Missing required field: venue_id"}, indent=2)

        # 2) Get DB from passed-in data
        venues: List[Dict[str, Any]] = data.get("venues", [])

        # 3) Exact match lookup
        for venue in venues:
            if venue.get("venue_id") == venue_id:
                return json.dumps(venue, indent=2)

        return json.dumps({"error": f"No venue found with ID {venue_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_venue_by_id",
                "description": "Fetch a single venue's full details by venue_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "venue_id": {
                            "type": "integer",
                            "description": "Exact venue ID to retrieve."
                        }
                    },
                    "required": ["venue_id"]
                }
            }
        }

class GetVenueByName(Tool):
    """Fetch a venue record by its venue_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        # 1) Validate
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        # 2) Get DB
        venues: List[Dict[str, Any]] = data.get("venues", [])

        # 3) Exact match (no normalization)
        for venue in venues:
            if venue.get("venue_name") == name:
                return json.dumps(venue, indent=2)

        return json.dumps({"error": f"No venue found with name {name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_venue_by_name",
                "description": "Fetch a single venue's full details by exact venue_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact venue name to retrieve (e.g., 'New York Stadium')."
                        }
                    },
                    "required": ["name"]
                }
            }
        }

class GetAllVenueInCity(Tool):
    """Fetch all venues located in a given city (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")

        # 1) Validate
        if not isinstance(city, str) or city == "":
            return json.dumps({"error": "Missing required field: city"}, indent=2)

        # 2) Get DB
        venues: List[Dict[str, Any]] = data.get("venues", [])

        # 3) Filter by exact city
        matching = [v for v in venues if v.get("city") == city]

        if not matching:
            return json.dumps({"error": f"No venues found in city {city}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_venue_in_city",
                "description": "Fetch all venue records whose city exactly matches the provided value (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "Exact city name (e.g., 'Boston')."
                        }
                    },
                    "required": ["city"]
                }
            }
        }


class GetUmpiresDetailsByName(Tool):
    """Fetch an umpire record by full_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        full_name = kwargs.get("full_name")

        # 1) Validate
        if not isinstance(full_name, str) or full_name == "":
            return json.dumps({"error": "Missing required field: full_name"}, indent=2)

        # 2) Get DB
        umpires: List[Dict[str, Any]] = data.get("umpires", [])

        # 3) Exact match (no normalization)
        for ump in umpires:
            if ump.get("full_name") == full_name:
                return json.dumps(ump, indent=2)

        return json.dumps({"error": f"No umpire found with full_name {full_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_details_by_name",
                "description": "Fetch a single umpire's full details by exact full_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact umpire full name to retrieve."
                        }
                    },
                    "required": ["full_name"]
                }
            }
        }

class GetUmpiresDetailsById(Tool):
    """Fetch an umpire record by umpire_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        umpire_id = kwargs.get("umpire_id")

        # 1) Validate
        if umpire_id is None:
            return json.dumps({"error": "Missing required field: umpire_id"}, indent=2)

        # 2) Get DB
        umpires: List[Dict[str, Any]] = data.get("umpires", [])

        # 3) Exact match
        for ump in umpires:
            if ump.get("umpire_id") == umpire_id:
                return json.dumps(ump, indent=2)

        return json.dumps({"error": f"No umpire found with ID {umpire_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_details_by_id",
                "description": "Fetch a single umpire's full details by umpire_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "umpire_id": {
                            "type": "integer",
                            "description": "Exact umpire ID to retrieve."
                        }
                    },
                    "required": ["umpire_id"]
                }
            }
        }

class GetUmpiresByExperience(Tool):
    """
    Return all umpires with years_experience greater than a given threshold,
    sorted by years_experience in descending order (ties broken by smallest umpire_id).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exp_threshold = kwargs.get("min_experience")

        # 1) Validate
        if exp_threshold is None:
            return json.dumps({"error": "Missing required field: experience"}, indent=2)

        # 2) Get DB
        umpires: List[Dict[str, Any]] = data.get("umpires", [])

        # 3) Filter for those with experience > threshold
        filtered = [
            ump for ump in umpires
            if int(ump.get("years_experience", 0)) > exp_threshold
        ]

        if not filtered:
            return json.dumps({"error": f"No umpires found with experience greater than {exp_threshold}"}, indent=2)

        # 4) Sort deterministically
        sorted_list = sorted(
            filtered,
            key=lambda u: (-int(u.get("years_experience", 0)), int(u.get("umpire_id", 0)))
        )

        return json.dumps(sorted_list, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_by_experience",
                "description": "Return all umpires with years_experience greater than the provided threshold, sorted in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "experience": {
                            "type": "integer",
                            "description": "Minimum years_experience threshold; only umpires with greater experience are returned."
                        }
                    },
                    "required": ["min_experience"]
                }
            }
        }


class GetAllEevntsByGamePk(Tool):
    """
    Return all game-day events for a given game_pk.

    Notes:
      - Exact match on game_pk (no normalization).
      - Results are sorted deterministically by timestamp_utc asc, then event_id asc.
      - Expects the events array under data["game_day_events"].
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB from passed-in data
        events: List[Dict[str, Any]] = data.get("game_day_events", [])

        # 3) Filter by exact game_pk
        matching = [e for e in events if e.get("game_pk") == game_pk]

        if not matching:
            return json.dumps({"error": f"No events found for game_pk {game_pk}"}, indent=2)

        # 4) Deterministic ordering
        matching.sort(key=lambda e: (e.get("timestamp_utc", ""), int(e.get("event_id", 0))))

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_eevnts_by_game_pk",
                "description": "Fetch all game-day events for the specified game_pk (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key whose events should be returned."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }

class CreateGameDayEvent(Tool):
    """
    Create a new game-day event.
    Inputs (exact names):
      - game_pk (int) [required]
      - pitch_id (int) [required]
      - leverage_index (float or int) [required]
      - is_manual_alert (bool) [required]
      - suggestion_text (string) [required]
    Behavior:
      - event_id is generated automatically (max existing event_id + 1; starts at 1 if empty).
      - draft_status defaults to "Draft".
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        pitch_id = kwargs.get("pitch_id")
        leverage_index = kwargs.get("leverage_index")
        is_manual_alert = kwargs.get("is_manual_alert")
        suggestion_text = kwargs.get("suggestion_text")

        # 1) Validate required inputs
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
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB
        events: List[Dict[str, Any]] = data.get("game_day_events", [])

        # 4) Create new event row
        new_event = {
            "event_id": get_next_event_id(data),
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": get_current_timestamp(),  # Could be filled later if needed
            "leverage_index": leverage_index,
            "is_manual_alert": is_manual_alert,
            "suggestion_text": suggestion_text,
            "draft_status": "draft"
        }

        # 5) Insert into DB
        events.append(new_event)

        return json.dumps(new_event, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_game_day_event",
                "description": (
                    "Create a new game-day event. event_id is generated automatically "
                    "(max existing + 1). draft_status defaults to 'Draft'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key this event belongs to."
                        },
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID associated with the event."
                        },
                        "leverage_index": {
                            "type": "number",
                            "description": "Leverage index for the event."
                        },
                        "is_manual_alert": {
                            "type": "boolean",
                            "description": "True if the alert is manually triggered, else False."
                        },
                        "suggestion_text": {
                            "type": "string",
                            "description": "Suggestion text for the event."
                        }
                    },
                    "required": [
                        "game_pk",
                        "leverage_index",
                        "is_manual_alert",
                        "suggestion_text"
                    ]
                }
            }
        }

class UpdateGameEventStatus(Tool):
    """
    Update the draft_status of an existing game-day event.

    Inputs:
      - event_id (int) [required]
      - draft_status (string) [required]
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        event_id = kwargs.get("event_id")
        draft_status = kwargs.get("draft_status")

        # 1) Validate
        if event_id is None:
            return json.dumps({"error": "Missing required field: event_id"}, indent=2)
        if not isinstance(draft_status, str) or draft_status == "":
            return json.dumps({"error": "Missing required field: draft_status"}, indent=2)

        # 2) Get DB
        events: List[Dict[str, Any]] = data.get("game_day_events", [])

        # 3) Find and update
        for event in events:
            if event.get("event_id") == event_id:
                event["draft_status"] = draft_status
                return json.dumps(event, indent=2)

        return json.dumps({"error": f"No event found with event_id {event_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_game_event_status",
                "description": "Update the draft_status of a game-day event identified by event_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "integer",
                            "description": "Exact event ID to update."
                        },
                        "draft_status": {
                            "type": "string",
                            "description": "New draft status for the event (e.g., 'draft', 'published', 'archived')."
                        }
                    },
                    "required": ["event_id", "draft_status"]
                }
            }
        }


class GetAllGoalsByForPlayer(Tool):
    """Fetch all development goals for a given player_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB
        goals: List[Dict[str, Any]] = data.get("player_dev_goals", [])

        # 3) Filter goals for player
        matching = [g for g in goals if g.get("player_id") == player_id]

        if not matching:
            return json.dumps({"error": f"No goals found for player_id {player_id}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_goals_by_for_player",
                "description": "Fetch all development goals for a given player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve goals for."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }

class CreateNewGoal(Tool):
    """
    Create a new player development goal.
    Required:
      - dev_report_id
      - player_id
      - goal_text
      - coach_id
      - target_review_date (YYYY-MM-DD)
    Defaults:
      - goal_id auto-generated
      - goal_status = "Active"
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dev_report_id = kwargs.get("dev_report_id")
        player_id = kwargs.get("player_id")
        goal_text = kwargs.get("goal_text")
        coach_id = kwargs.get("coach_id")
        target_review_date = kwargs.get("target_review_date")

        # Validate required
        missing = []
        for field, val in [
            ("dev_report_id", dev_report_id),
            ("player_id", player_id),
            ("goal_text", goal_text if isinstance(goal_text, str) and goal_text.strip() else None),
            ("coach_id", coach_id),
            ("target_review_date", target_review_date if isinstance(target_review_date, str) and target_review_date.strip() else None),
        ]:
            if val is None:
                missing.append(field)

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        goals: List[Dict[str, Any]] = data.get("player_dev_goals", [])


        new_goal = {
            "goal_id": get_next_player_goal_id(data),
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": "Active",
            "coach_id": coach_id,
            "target_review_date": target_review_date
        }
        goals.append(new_goal)

        return json.dumps(new_goal, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_goal",
                "description": "Create a new player development goal. goal_id auto-generated; goal_status defaults to 'Active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {
                            "type": "integer",
                            "description": "Development report ID associated with the goal."
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the goal is for."
                        },
                        "goal_text": {
                            "type": "string",
                            "description": "Description of the development goal."
                        },
                        "coach_id": {
                            "type": "integer",
                            "description": "Coach ID who set the goal."
                        },
                        "target_review_date": {
                            "type": "string",
                            "description": "Target review date in YYYY-MM-DD."
                        }
                    },
                    "required": ["dev_report_id", "player_id", "goal_text", "coach_id", "target_review_date"]
                }
            }
        }


class CreateNewReport(Tool):
    """
    Create a new player development report.
    Required inputs (exact names):
      - player_id (int)
      - week_of_date (string, YYYY-MM-DD)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
    Behavior:
      - dev_report_id is auto-generated: max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")
        week_of_date = kwargs.get("week_of_date")


        # 1) Validate required inputs
        missing = []
        if player_id is None: missing.append("player_id")
        if not isinstance(week_of_date, str) or week_of_date == "": missing.append("week_of_date")


        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = data.get("player_dev_reports", [])

        new_id = get_next_dev_report_goal_id(data)

        # 4) Build and insert the row
        new_row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": get_current_timestamp(),
            "s3_pdf_path": f"s3://reports/development/{new_id}.pdf"
        }
        reports.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_report",
                "description": "Create a new player development report. dev_report_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the report belongs to."
                        },
                        "week_of_date": {
                            "type": "string",
                            "description": "Week-of date in YYYY-MM-DD."
                        },
                    },
                    "required": ["player_id", "week_of_date"]
                }
            }
        }

class GetAllReportForPlayer(Tool):
    """
    Fetch all development reports for a given player_id.
    Results are sorted deterministically by week_of_date DESC, then dev_report_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = data.get("player_dev_reports", [])

        # 3) Filter and sort
        matching = [r for r in reports if r.get("player_id") == player_id]

        if not matching:
            return json.dumps({"error": f"No reports found for player_id {player_id}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_report_for_player",
                "description": "Fetch all development reports for the specified player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve reports for."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }


class GetPitchDetailsById(Tool):
    """Fetch a single pitch by its pitch_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_id = kwargs.get("pitch_id")

        # 1) Validate
        if pitch_id is None:
            return json.dumps({"error": "Missing required field: pitch_id"}, indent=2)

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Exact match
        for p in pitches:
            if p.get("pitch_id") == pitch_id:
                return json.dumps(p, indent=2)

        return json.dumps({"error": f"No pitch found with pitch_id {pitch_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pitch_details_by_id",
                "description": "Fetch a single pitch's full details by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {"type": "integer", "description": "Exact pitch ID to retrieve."}
                    },
                    "required": ["pitch_id"]
                }
            }
        }
    
class GetAllPitchesByPitcherIds(Tool):
    """Fetch all pitches thrown by any pitcher in the provided list of pitcher_ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitcher_ids = kwargs.get("pitcher_ids")

        # 1) Validate
        if not isinstance(pitcher_ids, list) or len(pitcher_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: pitcher_ids (non-empty list of integers)"},
                indent=2
            )

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Filter
        id_set = set(pitcher_ids)
        matches = [p for p in pitches if p.get("pitcher_id") in id_set]
        if not matches:
            return json.dumps({"error": f"No pitches found for pitcher_ids {pitcher_ids}"}, indent=2)

        # 4) Deterministic order: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        # matches.sort(
        #     key=lambda p: (
        #         int(p.get("game_pk", 0)),
        #         int(p.get("at_bat_index", 0)),
        #         int(p.get("pitch_number", 0)),
        #         int(p.get("pitch_id", 0)),
        #     )
        # )
        pitch_ids = [int(p.get("pitch_id", 0)) for p in matches]
        # Deduplicate while preserving order, just in case
        pitch_ids = list(dict.fromkeys(pitch_ids))

        payload = {
            "pitch_ids": pitch_ids,
            "pitches": matches,
        }

        # 5) Return list of pitch records only
        return json.dumps(payload, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_by_pitcher_ids",
                "description": "Fetch all pitches where pitcher_id is in pitcher_ids. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitcher IDs."
                        }
                    },
                    "required": ["pitcher_ids"]
                }
            }
        }

class GetAllPitchesByHitterIds(Tool):
    """Fetch all pitches faced by any hitter in the provided list of hitter_ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hitter_ids = kwargs.get("hitter_ids")

        # 1) Validate
        if not isinstance(hitter_ids, list) or len(hitter_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: hitter_ids (non-empty list of integers)"},
                indent=2
            )

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Filter
        id_set = set(hitter_ids)
        matches = [p for p in pitches if p.get("hitter_id") in id_set]
        if not matches:
            return json.dumps({"error": f"No pitches found for hitter_ids {hitter_ids}"}, indent=2)

        # 4) Deterministic order: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        matches.sort(
            key=lambda p: (
                int(p.get("game_pk", 0)),
                int(p.get("at_bat_index", 0)),
                int(p.get("pitch_number", 0)),
                int(p.get("pitch_id", 0)),
            )
        )

        # 5) Return list of pitch records only
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_by_hitter_ids",
                "description": "Fetch all pitches where hitter_id is in the provided list. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hitter_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of hitter IDs."
                        }
                    },
                    "required": ["hitter_ids"]
                }
            }
        }

class GetAllPitchesForGame(Tool):
    """Fetch all pitches for a given game_pk."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Filter and deterministic order within game
        result = [p for p in pitches if p.get("game_pk") == game_pk]
        if not result:
            return json.dumps({"error": f"No pitches found for game_pk {game_pk}"}, indent=2)

        result.sort(key=lambda p: (p.get("at_bat_index", 0), p.get("pitch_number", 0), p.get("pitch_id", 0)))
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_for_game",
                "description": "Fetch all pitches belonging to a specific game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer", "description": "Exact game primary key."}
                    },
                    "required": ["game_pk"]
                }
            }
        }

class CreateNewPitch(Tool):
    """
    Insert a new pitch row with full details.
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required_fields = [
            "game_pk","at_bat_index","pitch_number","pitcher_id","hitter_id",
            "pitch_type_raw","pitch_type_canonical","velocity_mph","spin_rate_rpm",
            "release_x","release_z","plate_x","plate_z",
            "exit_velocity_mph","launch_angle_deg","leverage_index"
        ]
        missing = [f for f in required_fields if kwargs.get(f) is None]
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # Generate new pitch_id deterministically
        new_id = get_next_pitch_id(data)

        new_pitch = {"pitch_id": new_id}
        for f in required_fields:
            new_pitch[f] = kwargs.get(f)

        pitches.append(new_pitch)
        return json.dumps(new_pitch, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Build JSON schema properties
        props: Dict[str, Any] = {
            "game_pk": {"type": "integer"}, "at_bat_index": {"type": "integer"},
            "pitch_number": {"type": "integer"}, "pitcher_id": {"type": "integer"},
            "hitter_id": {"type": "integer"}, "pitch_type_raw": {"type": "string"},
            "pitch_type_canonical": {"type": "string"}, "velocity_mph": {"type": "number"},
            "spin_rate_rpm": {"type": "number"}, "release_x": {"type": "number"},
            "release_z": {"type": "number"}, "plate_x": {"type": "number"},
            "plate_z": {"type": "number"}, "exit_velocity_mph": {"type": "number"},
            "launch_angle_deg": {"type": "number"}, "leverage_index": {"type": "number"}
        }
        return {
            "type": "function",
            "function": {
                "name": "create_new_pitch",
                "description": "Insert a new pitch with full details; pitch_id auto-generated.",
                "parameters": {
                    "type": "object",
                    "properties": props,
                    "required": list(props.keys())
                }
            }
        }


class GetGradeByPitchId(Tool):
    """Fetch the execution grade record for a single pitch_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_id = kwargs.get("pitch_id")

        # 1) Validate
        if pitch_id is None:
            return json.dumps({"error": "Missing required field: pitch_id"}, indent=2)

        # 2) Get DB
        grades: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # 3) Exact match
        for rec in grades:
            if rec.get("pitch_id") == pitch_id:
                return json.dumps(rec, indent=2)

        return json.dumps({"error": f"No grade found for pitch_id {pitch_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grade_by_pitch_id",
                "description": "Fetch a single pitch execution grade record by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID whose grade should be returned."
                        }
                    },
                    "required": ["pitch_id"]
                }
            }
        }

class GetGradesByPitchIds(Tool):
    """
    Fetch execution grade records for a list of pitch IDs.
    Returns all matching rows sorted deterministically by pitch_id ASC, grade_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_ids = kwargs.get("pitch_ids")

        # 1) Validate
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            return json.dumps({"error": "Missing required field: pitch_ids (non-empty list of integers)"}, indent=2)

        # 2) Get DB
        grades: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # 3) Collect matches
        id_set = set(pitch_ids)
        matches = [rec for rec in grades if rec.get("pitch_id") in id_set]

        if not matches:
            return json.dumps({"No grades found": f"No grades found for pitch_ids {pitch_ids}"}, indent=2)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grades_by_pitch_ids",
                "description": "Fetch execution grade records for the given list of pitch IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of pitch IDs to retrieve grades for."
                        }
                    },
                    "required": ["pitch_ids"]
                }
            }
        }

class GetFilteredGradesByPitchIds(Tool):
    """
    Fetch execution grade records for a list of pitch IDs, then EXCLUDE any rows
    whose execution_grade is in the provided grades list.

    Inputs (exact names; case-sensitive):
      - pitch_ids (List[int]) : Non-empty list of pitch IDs to search.
      - grades    (List[str]) : Non-empty list of grade labels to EXCLUDE
                                (exact, case-sensitive match, e.g., ["C", "D", "F"]).

    Behavior:
      - Looks up all rows where rec.pitch_id ∈ pitch_ids.
      - Filters OUT rows where rec.execution_grade ∈ grades.
      - Returns results sorted deterministically by (pitch_id ASC, grade_id ASC).
      - If no rows match the pitch_ids at all, returns a structured error.
      - If rows match pitch_ids but all are filtered out by grades, returns a structured error.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # ---- 1) Validate inputs
        pitch_ids = kwargs.get("pitch_ids")
        grades_to_exclude = kwargs.get("grades")

        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: pitch_ids (non-empty list of integers)"},
                indent=2
            )
        if not isinstance(grades_to_exclude, list) or len(grades_to_exclude) == 0:
            return json.dumps(
                {"error": "Missing required field: grades (non-empty list of strings to EXCLUDE)"},
                indent=2
            )

        # ---- 2) Get DB
        grades: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # ---- 3) Collect matches by pitch_ids
        id_set = set(pitch_ids)
        initial = [rec for rec in grades if rec.get("pitch_id") in id_set]

        if not initial:
            return json.dumps(
                {"error": f"No grades found for pitch_ids {pitch_ids}"},
                indent=2
            )

        # ---- 4) Filter OUT records whose execution_grade is in grades_to_exclude (exact, case-sensitive)
        excl_set = set(grades_to_exclude)
        filtered = [rec for rec in initial if rec.get("execution_grade") in excl_set]

        if not filtered:
            return json.dumps(
                {
                    "error": (
                        "All grades were filtered out. No remaining records after excluding "
                        f"{sorted(excl_set)} for pitch_ids {pitch_ids}"
                    )
                },
                indent=2
            )

        # ---- 5) Deterministic sort: pitch_id ASC, grade_id ASC
        filtered.sort(key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0))))

        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_filtered_grades_by_pitch_ids",
                "description": "Fetch execution grade records for given pitch IDs and EXCLUDE rows whose execution_grade matches any provided grade.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitch IDs to retrieve grades for."
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Non-empty list of grade labels to EXCLUDE (exact, case-sensitive)."
                        }
                    },
                    "required": ["pitch_ids", "grades"]
                }
            }
        }


class CreateNewGrade(Tool):
    """
    Create a new pitch execution grade.
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_id = kwargs.get("pitch_id")
        game_pk = kwargs.get("game_pk")
        intended_quadrant_model = kwargs.get("intended_quadrant_model")
        actual_quadrant = kwargs.get("actual_quadrant")
        miss_distance_inches = kwargs.get("miss_distance_inches")
        execution_grade = kwargs.get("execution_grade")

        # 1) Validate required fields
        missing = []
        if pitch_id is None: missing.append("pitch_id")
        if game_pk is None: missing.append("game_pk")
        if intended_quadrant_model is None: missing.append("intended_quadrant_model")
        if  actual_quadrant is None: missing.append("actual_quadrant")
        if miss_distance_inches is None: missing.append("miss_distance_inches")
        if not isinstance(execution_grade, str) or execution_grade == "": missing.append("execution_grade")

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB
        grades: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # 3) Generate new grade_id
        new_id = get_next_grade_id(data)

        # 4) Create new record
        new_record = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": execution_grade
        }
        grades.append(new_record)

        return json.dumps(new_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_grade",
                "description": "Create a new pitch execution grade with auto-generated grade_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID this grade belongs to."
                        },
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key."
                        },
                        "intended_quadrant_model": {
                            "type": "integer",
                            "description": "Intended quadrant from the model."
                        },
                        "actual_quadrant": {
                            "type": "integer",
                            "description": "Actual quadrant observed."
                        },
                        "miss_distance_inches": {
                            "type": "number",
                            "description": "Distance missed in inches."
                        },
                        "execution_grade": {
                            "type": "string",
                            "description": "Execution grade value."
                        }
                    },
                    "required": [
                        "pitch_id",
                        "game_pk",
                        "intended_quadrant_model",
                        "actual_quadrant",
                        "miss_distance_inches",
                        "execution_grade"
                    ]
                }
            }
        }

class GetGradesByGradeForGame(Tool):
    """
    Return all pitch execution grade records for a given game that match any of the
    provided grade values.

    Inputs:
      - game_pk (int)           [required]
      - grades (List[str])      [required] list of execution_grade values to match

    Behavior:
      - Exact (case-sensitive) match on execution_grade.
      - Filters records where record.game_pk == game_pk AND record.execution_grade in grades.
      - Deterministic ordering by pitch_id ASC, then grade_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        grades_filter = kwargs.get("grades")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)
        if not isinstance(grades_filter, list) or len(grades_filter) == 0:
            return json.dumps({"error": "Missing required field: grades (non-empty list of strings)"}, indent=2)

        # 2) Get DB
        records: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # 3) Filter (exact, case-sensitive)
        allowed = set(grades_filter)
        matches = [
            r for r in records
            if r.get("game_pk") == game_pk and r.get("execution_grade") in allowed
        ]

        if not matches:
            return json.dumps(
                {"error": f"No grades found for game_pk {game_pk} with execution_grade in {grades_filter}"},
                indent=2
            )

        # 4) Deterministic ordering
        matches.sort(key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0))))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grades_by_grade_for_game",
                "description": "Fetch pitch execution grade records for a game where execution_grade matches any of the provided values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key to filter on."
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of execution_grade values to match (case-sensitive)."
                        }
                    },
                    "required": ["game_pk", "grades"]
                }
            }
        }


class GetHighlightsByName(Tool):
    """
    Fetch a highlight playlist by name.
    Inputs:
      - name (string) [required]  # The suffix; code will prepend 'Game Highlights - '
    Behavior:
      - Compute full_name = "Game Highlights - " + name and return the matching playlist.
      - If multiple match (unlikely), return the one with the smallest playlist_id for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        # 1) Validate
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        full_name = f"Game Highlights - {name}"

        # 2) Get DB
        playlists: List[Dict[str, Any]] = data.get("video_playlists", [])

        # 3) Exact match search (no normalization)
        matches = [p for p in playlists if p.get("playlist_name") == full_name]

        if not matches:
            return json.dumps({"error": f"No playlist found with name '{full_name}'"}, indent=2)

        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        return json.dumps(matches[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_highlights_by_name",
                "description": "Return the 'Game Highlights - <name>' playlist (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix after 'Game Highlights - ' to look up."
                        }
                    },
                    "required": ["name"]
                }
            }
        }

class AddNewHighlight(Tool):
    """
    Add to an existing highlight playlist'sclip_count, or create a new one if it doesn't exist.

    Inputs (exact names):
      - name (string)       [required]  # The suffix; code will prepend 'Game Highlights - '
      -clip_count (integer) [required]

    Behavior:
      - Compute full_name = "Game Highlights - " + name (no normalization).
      - If a playlist with playlist_name == full_name exists, incrementclip_count byclip_count.
      - Else, create a new row with:
          playlist_id = max existing + 1 (or 1 if none),
          report_id = null,
          internal_portal_link = null,
        clip_count =clip_count.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        clip_count = kwargs.get("clip_count")
        report_id = kwargs.get("report_id", None)

        # 1) Validate
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)
        if clip_count is None:
            return json.dumps({"error": "Missing required field: clip_count"}, indent=2)

        full_name = f"Game Highlights - {name}"

        # 2) Get DB
        playlists: List[Dict[str, Any]] = data.get("video_playlists", [])

        # 3) Try to find existing
        target = None
        for p in playlists:
            if p.get("playlist_name") == full_name:
                target = p
                break

        # 4) Update or create
        if target is not None:
            # Incrementclip_count
            current = int(target.get("clip_count", 0))
            target["clip_count"] = current + int(clip_count)
            return json.dumps(target, indent=2)

        # Create new
        new_id = get_next_highlight_id(data)
        new_row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": full_name,
            "internal_portal_link": f"https://internal.baseball.com/playlists/{new_id}",
            "clip_count": int(clip_count)
        }
        playlists.append(new_row)
        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_highlight",
                "description": "Add clip_count to an existing 'Game Highlights - <name>' playlist, or create it if missing. Optionally set report_id if creating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix to append after 'Game Highlights - '."
                        },
                        "clip_count": {
                            "type": "integer",
                            "description": "Number of clips to add (used as initial count if created)."
                        },
                        "report_id": {
                            "type": ["integer", "null"],
                            "description": "Optional report ID to associate when creating new."
                        }
                    },
                    "required": ["name", "clip_count"]
                }
            }
        }

class GetHighlightByReportId(Tool):
    """Fetch all video playlists associated with a given report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")

        # 1) Validate
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # 2) Get DB from passed-in data
        playlists: List[Dict[str, Any]] = data.get("video_playlists", [])

        # 3) Exact match lookup (no normalization)
        matches = [p for p in playlists if p.get("report_id") == report_id]

        if not matches:
            return json.dumps({"error": f"No video playlists found for report_id {report_id}"}, indent=2)

        # 4) Deterministic ordering
        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_highlight_by_report_id",
                "description": "Fetch all video playlists whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": ["integer", "string"],
                            "description": "Exact report ID to filter by."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }


class GetPlayerInsightsByPlayeridAndType(Tool):
    """
    Fetch player insights by player_id and type filter.

    Inputs (exact names):
      - player_id (int) [required]
      - type (string)   [required]
          * Use "all" to return all insights for the player
          * Or pass an exact insight_type (e.g., "Performance", "Health", "Development", "Strategic", "Mechanical")

    Behavior:
      - Exact match (case-sensitive) on insight_type when type != "all"
      - Deterministic ordering by insight_id ASC
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")
        type_filter = kwargs.get("type")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)
        if not isinstance(type_filter, str) or type_filter == "":
            return json.dumps({"error": "Missing required field: type"}, indent=2)

        # 2) Get DB
        insights: List[Dict[str, Any]] = data.get("curated_insights", [])

        # 3) Filter by player_id
        player_insights = [i for i in insights if i.get("player_id") == player_id]

        if not player_insights:
            return json.dumps({"error": f"No insights found for player_id {player_id}"}, indent=2)

        # 4) Apply type filter
        if type_filter != "all":
            player_insights = [i for i in player_insights if i.get("insight_type") == type_filter]
            if not player_insights:
                return json.dumps(
                    {"error": f"No insights found for player_id {player_id} with type '{type_filter}'"},
                    indent=2
                )

        # 5) Deterministic ordering
        player_insights.sort(key=lambda i: int(i.get("insight_id", 0)))

        return json.dumps(player_insights, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_insights_by_playerid_and_type",
                "description": (
                    "Fetch curated insights for a player. Pass type='All' to get all insights, "
                    "or an exact insight_type (e.g., 'Performance') for a specific subset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID whose insights to retrieve."
                        },
                        "type": {
                            "type": "string",
                            "description": "Use 'All' or provide an exact insight_type (case-sensitive)."
                        }
                    },
                    "required": ["player_id", "type"]
                }
            }
        }

class CreateNewInsight(Tool):
    """
    Create a new curated insight.

    Required inputs (exact names):
      - report_id (int)
      - player_id (int)
      - insight_text (string, non-empty)
      - insight_type (string, non-empty)
      - supporting_stat_value (number)

    Behavior:
      - insight_id is auto-generated as max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        player_id = kwargs.get("player_id")
        insight_text = kwargs.get("insight_text")
        insight_type = kwargs.get("insight_type")
        supporting_stat_value = kwargs.get("supporting_stat_value")

        # 1) Validate required inputs
        missing = []
        if report_id is None: missing.append("report_id")
        if player_id is None: missing.append("player_id")
        if not isinstance(insight_text, str) or insight_text.strip() == "": missing.append("insight_text")
        if not isinstance(insight_type, str) or insight_type.strip() == "": missing.append("insight_type")
        if supporting_stat_value is None: missing.append("supporting_stat_value")

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB
        insights: List[Dict[str, Any]] = data.get("curated_insights", [])

        # 3) Generate new insight_id deterministically
        new_id = get_next_insight_id(data)

        # 4) Build and insert the row
        new_row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value
        }
        insights.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_insight",
                "description": "Create a new curated insight; insight_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Report ID this insight is associated with."
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID this insight refers to."
                        },
                        "insight_text": {
                            "type": "string",
                            "description": "Human-readable insight text."
                        },
                        "insight_type": {
                            "type": "string",
                            "description": "Category/type of the insight (case-sensitive)."
                        },
                        "supporting_stat_value": {
                            "type": "number",
                            "description": "Numeric value that supports the insight."
                        }
                    },
                    "required": [
                        "report_id",
                        "player_id",
                        "insight_text",
                        "insight_type",
                        "supporting_stat_value"
                    ]
                }
            }
        }

class GetInsightbyreportid(Tool):
    """Fetch all curated insights associated with a given report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")

        # 1) Validate
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # 2) Get DB
        insights: List[Dict[str, Any]] = data.get("curated_insights", [])

        # 3) Exact match lookup (no normalization)
        matches = [i for i in insights if i.get("report_id") == report_id]

        if not matches:
            return json.dumps({"error": f"No insights found for report_id {report_id}"}, indent=2)

        # 4) Deterministic ordering
        matches.sort(key=lambda i: int(i.get("insight_id", 0)))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_insight_by_report_id",
                "description": "Fetch all curated insights whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to filter insights by."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }
    

class GetScoutingReportByGamepkAndType(Tool):
    """
    Fetch scouting reports by game_pk, optionally filtering by report_type.

    Inputs (exact names):
      - game_pk (int)       [required]
      - report_type (str)   [optional] exact, case-sensitive

    Behavior:
      - If report_type is provided, return only exact matches.
      - If not provided, return all reports for the game.
      - Deterministic ordering: created_at ASC, then report_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        report_type = kwargs.get("report_type")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = data.get("scouting_reports", [])

        # 3) Filter
        matches = [r for r in reports if r.get("game_pk") == game_pk]
        if report_type is not None:
            matches = [r for r in matches if r.get("report_type") == report_type]

        if not matches:
            if report_type is None:
                return json.dumps({"error": f"No scouting reports found for game_pk {game_pk}"}, indent=2)
            return json.dumps({"error": f"No scouting reports found for game_pk {game_pk} with type '{report_type}'"}, indent=2)

        # 4) Sort deterministically
        matches.sort(key=lambda r: (r.get("created_at", ""), int(r.get("report_id", 0))))
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scouting_report_by_gamepk_and_type",
                "description": "Fetch scouting reports for a game; optionally filter by exact report_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer", "description": "Game primary key."},
                        "report_type": {"type": "string", "description": "Optional exact report type (case-sensitive)."}
                    },
                    "required": ["game_pk"]
                }
            }
        }

class CreateScoutingReport(Tool):
    """
    Create a new scouting report.

    Required inputs (exact names):
      - report_type (string)
      - game_pk (int)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
      - gslides_link (string)
      - core_narrative_text (string)

    Behavior:
      - report_id auto-generated: max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_type = kwargs.get("report_type")
        game_pk = kwargs.get("game_pk")
        core_narrative_text = kwargs.get("core_narrative_text")

        # 1) Validate
        missing = []
        if not isinstance(report_type, str) or report_type == "": missing.append("report_type")
        if game_pk is None: missing.append("game_pk")
        if not isinstance(core_narrative_text, str) or core_narrative_text == "": missing.append("core_narrative_text")

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = data.get("scouting_reports", [])

        # 3) Generate new id
        new_id = get_next_scouting_report_id(data)

        # 4) Insert
        new_row = {
            "report_id": new_id,
            "report_type": report_type,
            "game_pk": game_pk,
            "created_at": get_today_date(),
            "s3_pdf_path": f"s3://reports/scouting/{new_id}.pdf",
            "gslides_link": f"https://docs.google.com/presentation/d/{new_id}",
            "core_narrative_text": core_narrative_text
        }
        reports.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        props = {
            "report_type": {"type": "string", "description": "e.g., 'Pre-Game', 'Post-Game', 'Opponent Analysis', 'Series Summary', 'Player Focus'"},
            "game_pk": {"type": "integer", "description": "Game primary key this report is about."},
            "core_narrative_text": {"type": "string", "description": "Main narrative text for the report."}
        }
        return {
            "type": "function",
            "function": {
                "name": "create_scouting_report",
                "description": "Create a new scouting report; report_id auto-generated (max existing + 1).",
                "parameters": {"type": "object", "properties": props, "required": list(props.keys())}
            }
        }

class GetScoutingReportById(Tool):
    """Fetch a single scouting report by its report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")

        # 1) Validate
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # 2) Get DB from passed-in data
        reports: List[Dict[str, Any]] = data.get("scouting_reports", [])

        # 3) Exact match lookup
        for report in reports:
            if report.get("report_id") == report_id:
                return json.dumps(report, indent=2)

        return json.dumps({"error": f"No scouting report found with ID {report_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scouting_report_by_id",
                "description": "Fetch a single scouting report's full details by its report_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Exact report ID to retrieve."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }


class CreateWorkflow(Tool):
    """
    Create a new workflow run with deterministic behavior for provided data.
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dag_name = kwargs.get("dag_name")
        game_pk = kwargs.get("game_pk") or None
        status = kwargs.get("status")
        

        # Validate required fields
        missing = [f for f in ["dag_name", "status"] if kwargs.get(f) is None]
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        workflows = data.get("workflow_runs", [])
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
            "log_s3_path": log_path
        }

        workflows.append(new_entry)
        return json.dumps(new_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_workflow",
                "description": "Create a new workflow run entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": ["integer", "null"]},
                        "status": {"type": "string"},
                    },
                    "required": ["dag_name", "status"]
                }
            }
        }


class GetBullpenSessionInfoForPlayer(Tool):
    """
    Return bullpen sessions for a given player with optional filters.

    Inputs (exact names; case-sensitive):
      - playerid (int)          : Required. Player ID to filter on (matches 'player_id').
      - date (str, optional)    : Exact session date 'YYYY-MM-DD' (matches 'session_date').
      - type (str, optional)    : Exact pitch type (matches 'pitch_type_canonical').

    Behavior:
      - Exact matching on the provided filters (no normalization).
      - Results are sorted deterministically by session_date ASC, then session_id ASC.
      - If no matching records are found, returns a structured error.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        playerid = kwargs.get("playerid")
        date_filter = kwargs.get("date")
        type_filter = kwargs.get("type")

        # 1) Validate required input
        if playerid is None:
            return json.dumps({"error": "Missing required field: playerid"}, indent=2)

        # 2) Access DB
        sessions: List[Dict[str, Any]] = data.get("bullpen_sessions", [])

        # 3) Filter by exact fields
        def match(session: Dict[str, Any]) -> bool:
            if session.get("player_id") != playerid:
                return False
            if date_filter is not None and session.get("session_date") != date_filter:
                return False
            if type_filter is not None and session.get("pitch_type_canonical") != type_filter:
                return False
            return True

        matches = [s for s in sessions if match(s)]

        if not matches:
            # Build an informative, structured error
            parts = [f"player_id {playerid}"]
            if date_filter is not None:
                parts.append(f"date {date_filter}")
            if type_filter is not None:
                parts.append(f"type {type_filter}")
            return json.dumps({"error": f"No bullpen sessions found for {'; '.join(parts)}"}, indent=2)

        # 4) Deterministic ordering
        matches.sort(key=lambda s: (s.get("session_date", ""), int(s.get("session_id", 0))))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bullpen_session_info_for_player",
                "description": "Fetch bullpen sessions for a player with optional exact filters on date and pitch type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "playerid": {
                            "type": "integer",
                            "description": "Exact player ID (matches 'player_id')."
                        },
                        "date": {
                            "type": "string",
                            "description": "Exact session date in YYYY-MM-DD (matches 'session_date')."
                        },
                        "type": {
                            "type": "string",
                            "description": "Exact pitch type (matches 'pitch_type_canonical')."
                        }
                    },
                    "required": ["playerid"]
                }
            }
        }
    
class CreateIngestionLog(Tool):
    """
    Create a new ingestion log entry.

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_name = kwargs.get("source_name")
        status_code = kwargs.get("status_code")
        records_ingested = kwargs.get("records_ingested")
        request_ts = kwargs.get("request_timestamp_utc", "2025-08-10 12:00:00")

        # 1) Validate required fields
        missing = []
        if source_name is None:
            missing.append("source_name")
        if status_code is None:
            missing.append("status_code")
        if records_ingested is None:
            missing.append("records_ingested")
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Access DB
        logs: List[Dict[str, Any]] = data.get("ingestion_logs", [])

        # 3) Generate new ingestion_id deterministically
        new_id = get_next_ingestion_id(data)

        # 4) Create record
        new_row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": get_current_timestamp(),
            "status_code": status_code,
            "records_ingested": records_ingested
        }

        # 5) Insert
        logs.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ingestion_log",
                "description": "Create a new ingestion log record; ingestion_id auto-generated (count + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "Name of the ingestion source (e.g., 'mlb_api', 'trackman')."
                        },
                        "status_code": {
                            "type": "integer",
                            "description": "HTTP-like status code of the ingestion attempt."
                        },
                        "records_ingested": {
                            "type": "integer",
                            "description": "Number of records successfully ingested."
                        },
                        "request_timestamp_utc": {
                            "type": "string",
                            "description": "UTC timestamp 'YYYY-MM-DD HH:MM:SS' (optional). Defaults to '2025-08-10 12:00:00' if omitted."
                        }
                    },
                    "required": ["source_name", "status_code", "records_ingested"]
                }
            }
        }
    
class GetModelDetailByGame(Tool):
    """
    Fetch per-game umpire model calibration details.

    Input:
      - game_pk (int): Exact game_pk to look up.

    Behavior:
      - Reads from data["umpire_game_models"].
      - Returns all matching rows, sorted deterministically by umpire_game_id ASC.
      - If no match, returns a clear error payload.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        models: List[Dict[str, Any]] = data.get("umpire_game_models", [])

        # 3) Collect matches
        matches = [row for row in models if row.get("game_pk") == game_pk]

        if not matches:
            return json.dumps({"error": f"No model details found for game_pk {game_pk}"}, indent=2)

        # 4) Deterministic order
        matches.sort(key=lambda r: int(r.get("umpire_game_id", 0)))

        # 5) Return
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_model_detail_by_game",
                "description": "Return umpire model calibration details for a given game_pk (sorted by umpire_game_id ASC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game identifier (game_pk)."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }
    


TOOLS =[
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





