RULES = [
    # ————— Game selection, leverage, and gating —————
    "A 'post-game' analysis workflow must only run for games where games.game_status == 'Final'. Tools that create post-game reports must enforce this gate.",
    "High-leverage is defined as leverage_index > 1.5. Any in-game auto-bookmarking or post-game 'high leverage' analysis must filter on that threshold (strict >).",
    "When selecting the next scheduled game for a series query, choose the earliest games.game_date >= current_date with game_status == 'Scheduled'. If multiple games share the earliest date, choose the one with the smallest game_pk. The current_date argument MUST be explicit (no hidden 'today').",

    # ————— Statistical policy for trends and flags —————
    "Minimum samples for trend flags: >=50 pitches OR >=30 swings OR >=25 batted balls before a slice can be surfaced.",
    "Apply empirical-Bayes (EB) shrinkage to stabilize short-window rates toward a season baseline before flagging trends.",
    "Control for multiplicity via False Discovery Rate (FDR) and practical-effect thresholds; only retain statistically meaningful flags.",
    "Trend filtering must be executed via the dedicated tool(s) and persist a deterministic flags table tied to the thresholds used.",

    # ————— Canonicalization & spatial policy —————
    "All pitch-type labels must be mapped to a canonical schema (e.g., vendor 'Sweeper'→'SW', 'Sinker'→'SI') prior to computing mix/usage or spatial stats.",
    "Spatial pitch/miss locations must be standardized to a 12x12 catcher-perspective grid before zone-based statistics or heatmaps are computed. Grid bounds must be valid (max > min).",

    # ————— Execution grading policy —————
    "Pitch execution grades must be one of ['Executed','Minor miss','Major miss'] and derive deterministically from miss_distance_inches or quadrant deviation.",
    "Execution threshold policy: Executed if miss_distance_inches <= 3.0; Minor miss if 3.0 < miss_distance_inches <= 9.0; Major miss if miss_distance_inches > 9.0.",

    # ————— In-game events policy —————
    "Automatic in-game bookmarks must include leverage_index > 1.5 and a short narration; they must set is_manual_alert = false.",
    "Manual alerts must set is_manual_alert = true and can be created at any time (no leverage gate).",
    "Valid draft_status states for game_day_events are 'draft', 'published', 'archived'. State transitions must be explicit and recorded in an audit log.",

    # ————— Reporting, insights, and playlists —————
    "A 'post-game' scouting report must include a core_narrative_text and a gslides_link and should attach curated video_playlists linked to the report_id.",
    "When curating opponent/player insights for any report, prioritize high-leverage patterns and collapse redundant bullets into a single actionable directive.",
    "Curated insight text must use deterministic templates (no free-form sentences): '{category}_{metric}_{bucket}', where category ∈ {tendency, execution, stamina, situational, predictability}.",
    "When selecting insights to display and more than N fit, sort by supporting_stat_value DESC, then by player_id ASC as a stable tie-breaker.",
    "For 'next series probable pitchers' lists, order pitchers by full_name ASC to keep the presentation stable.",

    # ————— Player development —————
    "Weekly development reports run off a team off-day schedule; by default exclude players with roster_status LIKE 'IL%' or 'Taxi' from the active roster snapshot unless explicitly opted in.",
    "Each new player development report should be accompanied by exactly two video playlists: 'Positive Reinforcement' (3–5 clips) and 'Teaching Moments' (2–3 clips). Tools must enforce these ranges when those playlist names are used.",

    # ————— Determinism & IDs —————
    "All tool arguments must be explicitly specified in the instruction or deterministically derived from prior tool outputs or fixed rules; no hidden clocks or defaults for dates/IDs.",
    "IDs across new rows must be sequential integers based on max(existing_id)+1 per table (e.g., report_id, playlist_id, goal_id, run_id, ingestion_id, grade_id). Paths/links should be generated deterministically from inputs (e.g., S3 paths using player_id and week_of_date).",
    "workflow_runs entries must include dag_name, game_pk (when applicable), status, start_time_utc, end_time_utc, and a deterministic log_s3_path.",

    # ————— Consistency & single source-of-truth —————
    "Any tool that depends on non-present tables must return a structured error that names the missing table(s) rather than fabricating results.",
    "Where the schema provides overlapping sources (e.g., event log vs. box score), log a single source of truth decision in workflow_runs and proceed only after a QC pass.",
]
