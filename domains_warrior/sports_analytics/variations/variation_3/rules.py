RULES = [
    # 1) Scope & time
    "Operate only through the provided APIs to manage players, teams, games, venues, umpires, pitches, grades, events, reports, goals, and video playlists.",
    "Treat “now” as 2025-08-10T12:00:00Z, and “today” as 2025-08-10. Timestamps or dates you generate must use these anchors.",
    
    # 2) Determinism & ID generation
    "All writes must be deterministic: the same inputs yield the same DB updates and IDs.",
    "New IDs are generated deterministically from the current table length (no randomness).",
    "New game primary keys use: 2024000000 + count(games) + 1 (first new game is 2024000001).",
    "For other entities, new IDs are count(table) + 1 at creation time: event_id, goal_id, dev_report_id, pitch_id, grade_id, playlist_id.",
    "Workflow run IDs must be generated in the format 'run_<N>', where <N> is the total number of existing workflow_runs plus 1, using a deterministic count from the data store."

    # 3) Matching & validation
    "Perform exact, case-sensitive matching for lookups (names, abbreviations, IDs).",
    "Validate required fields; if any required input is missing or malformed, return a concise, structured error that names the missing field(s).",
    "Respect exact parameter names as implemented; do not normalize or infer alternates.",

    # 4) Defaults on create
    "New games: status = “Scheduled”; final_score = null; attendance = null.",
    "New player dev goals: goal_status = “Active”.",
    "New game-day events: draft_status = “draft”.",
    "New reports: dev_report_id auto-generated; s3_pdf_path = s3://reports/development/<dev_report_id>.pdf.",
    "New workflows: run_id auto-generated; log_s3_path= s3://logs/workflows/<run_id>.log",
    "Default value of 'records_ingested' is 500 unless specified, while creating new  ingestion logs"
    "Default value of 'status_code' is 200 unless specified, while creating new  ingestion logs"
    "Default values of workflow status is success"


    # 5) Business rules for updates
    "For games, final score and attendance may be changed only when the resulting status is “Final”. If status isn’t “Final” (either already or in the same update), reject score/attendance changes with a structured error.",
    "Update operations modify only the fields explicitly provided; leave all others unchanged.",

    # 6) Date & time handling
    "Accept dates as YYYY-MM-DD (and YYYY-MM-DD HH:MM:SS where applicable).",
    "Comparisons are strict and string-based where specified (e.g., next-game selection requires game_date > current_date).",

    # 7) Query semantics & tie-breaks
    "When filters return multiple records, apply deterministic ordering as defined by each operation (e.g., by date then ID; by pitch sequence; by pitch_id then grade_id).",
    "For “next scheduled game,” consider only status = “Scheduled”, strictly after the provided current_date; tie-break by earliest date, then smallest game_pk.",
    "For event and pitch collections, ensure stable sort orders (e.g., timestamp asc then event_id; or at_bat_index → pitch_number → pitch_id).",

    # 8) Computed fields & naming conventions
    "Where a computed name is required, build it exactly as specified. Example: video playlist lookups and creations use \"Game Highlights - \" + <name> as the exact playlist_name.",
    "When incrementing counters (e.g., adding clips to an existing highlights playlist), add to the current value; otherwise create a new playlist with the deterministic ID and generated link.",

    # 9) Error handling
    "If no match is found for a lookup or filter, return a structured error that includes the search key(s).",
    "For numeric fields and typed inputs, reject invalid types with a structured error rather than coercing silently.",

    # 10) Lists & pagination behavior
    "When returning multiple results, return the complete filtered list in deterministic order (no implicit paging unless explicitly specified by the caller).",

    # 11) Consistency & casing
    "Use exact casing required by the schema for statuses and string enums (e.g., “Final”, “Scheduled”, “draft”, “Active”), as enforced by each operation.",

    # 12) Idempotency expectations
    "Re-running a “create” with identical inputs should not produce duplicate logical rows unless the contract explicitly allows it; ID generation must still remain deterministic based on table state.",

    # 13) Security & integrity
    "Never modify unrelated entities as side-effects. Each operation must only affect the targeted records and fields described by its inputs.",

    "For wrokflow run logs Start time is '2025-08-10T12:00:00Z' and end time is '2025-08-10T12:15:00Z'"
    "Good/High grade pitches have the following grades: A+, A, A-, B+,B-, B, "
    "Bad/Low grade pitches have the following grades: F,D"
    "Average grade pitches have the following grades: C+,C,C-"
    "Best and good performances have good/high grades"
    "Worst and bad performances have Bad/Low grades"
    "Average performances have Average grades"

    "Assume that every player can be both, a pitcher and hitter"
    "intended_quadrant_model, actual_quadrant, and miss_distance_inches should be explicitly mentioned in instruction while creating grades"
    "Always consider week_of_date = 2025-08-10 as valid and default for creating reports"
    "Consider past performance of player also for the reports, so ther is no need to filter pitch by the week."
    "number of clips are independent of the number of pitches, so use clipcount as mentioned in instructions for creating highlights"
    "There is no need to filter games and pitches by the date or week. Consider all data for the available."
    "Ignore player's roster_status and primary_position to consider all as active player and pitcher."
    "Default supporting_stat_value value for creating new insight is 30.0"
    "For every task involving pitch's grades, use 'hawkeye' as ingestion log's source by default"
    "For every task involving player's data analysis, use 'snowflake' as ingestion log's source by default"
    "If there are multiple ingestiom logs then the Order of ingestion logs is 'snowflake' followed by 'hawkeye'"
    "For Tasks including report generation the default value of dag_name is 'generate_reports' for create_workflow, unless explicitly specified in instruction"
    "Create new player dev report using 'create_new_report'"
    "Default value of dag_name is 'generate_reports'"
    "Default value of coach_id is '10', default value of goal_text is 'Need to improve' and default value of target_review_date is '2025-09-07' while creating new goals."
    "Consider the clips are given and the clip count is provided in the instruction"

]

#30