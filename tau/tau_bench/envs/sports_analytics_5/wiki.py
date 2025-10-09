WIKI = """
"The 'post-game' analysis workflow is permitted to execute solely for games where games.game_status equals 'Final'. Any tools generating post-game reports must strictly enforce this condition.",
    "High-leverage applies when leverage_index exceeds 1.5. All in-game auto-bookmarking and post-game 'high leverage' analyses must apply this strict greater-than threshold as a filter.",
    "For series queries, to determine the next scheduled game, select the game with the earliest games.game_date that is greater than or equal to current_date and has game_status equal to 'Scheduled'. If several games occur on that earliest date, pick the one with the lowest game_pk. The current_date parameter must always be provided explicitly; implicit use of 'today' is not permitted.",
    "Trend flags require at least 50 pitches, or at least 30 swings, or at least 25 batted balls before a slice can be displayed.",
    "Before flagging trends, use empirical-Bayes (EB) shrinkage to stabilize short-window rates toward the season baseline.",
    "Address multiplicity by applying False Discovery Rate (FDR) and practical-effect thresholds; retain only those flags that are statistically meaningful.",
    "Execute trend filtering exclusively with the designated tool(s) and store a deterministic flags table associated with the applied thresholds.",
    "Before calculating mix/usage or spatial statistics, all pitch-type labels must be aligned to the canonical schema (for example, vendor 'Sweeper' mapped to 'SW', 'Sinker' to 'SI').",
    "Prior to generating zone-based statistics or heatmaps, spatial pitch and miss locations are required to be normalized onto a 12x12 grid from the catcher’s perspective, ensuring that the grid bounds are valid (maximum is greater than minimum).",
    "Pitch execution grades must be strictly selected from ['Executed', 'Minor miss', 'Major miss'
"""
