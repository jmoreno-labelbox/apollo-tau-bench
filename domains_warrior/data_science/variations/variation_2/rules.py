RULES = [
    "Protocol Name: City Status Compilation Protocol",
    "When the user requests a city status compilation, the agent must apply this protocol.",
    "The protocol defines: (a) resolving location via project_config+geocoding, "
    "(b) retrieving the primary NOAA station only, (c) summarizing processed_timeseries, "
    "(d) retrieving predictions and metrics, (e) appending a deterministic terminal_log entry.",
    "The log entry must include command='status_compilation_<city_slug>', exit_code=0, "
    "printed_message='<command> completed', and printed_ts sourced deterministically from the database.",
    "stdout and stderr must be empty unless read verbatim from existing tables.",
    "Outputs must be strictly structured data (no narratives), including city, primary_station_id, "
    "processed_timeseries summary, predictions summary, metrics summary, and terminal_log confirmation.",
    "Protocol Override: City Status Compilation Protocol may be overridden per task by explicitly stated, deterministic conditions.",
    "Override: Station selection may specify a condition on tide_predictions.method; if the condition is met, use station A; otherwise use station B. The decision must be resolved via database reads (no guesses).",
    "Protocol Name: Model Variant Selection Protocol",
    "When a user requests selecting the best model variant for a city, apply this protocol.",
    "Selection criteria (default): choose the model with the highest AUC; if AUC ties, choose the one with higher Accuracy; if still tied, choose the one with the most recent metrics.generated_ts.",
    "The protocol must resolve candidates via deterministic reads from metrics and predictions tables; no values may be invented.",
    "After selecting a single winner, append one deterministic terminal log entry with: command='model_selection_<city_slug>', exit_code=0, printed_message='<command> completed', printed_ts taken from the winner's metrics.generated_ts; stdout='' and stderr=''.",
    "Outputs returned to user must be strictly data-bearing and limited to fields explicitly requested in the instruction.",
    "Protocol Override: tasks may override the tie-breaker by specifying a maximum AUC difference threshold under which recency (metrics.generated_ts) becomes the primary tie-breaker.",
    "Protocol Name: Primary Station Determination Protocol",
    "When a user requests determining the primary NOAA station for a city and compiling a compact run summary, apply this protocol.",
    "Default selection: choose the station marked 'primary' among candidates returned by station search; if not present, use the first station in deterministic ordering.",
    "Always resolve candidates via deterministic reads from station search results; do not invent values.",
    "After selecting a single primary station, summarize the processed dataset for the city and retrieve the active model's predictions and metrics for that city.",
    "Append one deterministic terminal log entry with: command='station_determination_<city_slug>', exit_code=0, printed_message='<command> completed', printed_ts sourced deterministically from an existing database timestamp for that city (e.g., dataset_split.split_ts); stdout='' and stderr=''.",
    "Outputs to the user must be strictly the fields explicitly requested in the instruction (no narratives).",
    "Protocol Override: tasks may override the primary-station rule by specifying a datum-based condition on recent water levels. Example: if water_levels.datum for a candidate station equals a specific datum value, force selection of that station; otherwise follow the default selection. The decision must be resolved via database reads only."
    "Protocol Override: When the target city has no dataset_split timestamp, derive the terminal log printed_ts from processed_timeseries.created_ts for that city's dataset.",
    "Protocol Override: A task may constrain the candidate set by requiring validation of a specific station's tide predictions over a fixed window before final primary selection.",
    "Protocol Name: City Risk Snapshot Protocol",
    "When a user requests a risk snapshot for a city, the agent must: (a) resolve nearby NOAA stations deterministically, (b) choose exactly one primary station, (c) summarize core artifacts (processed dataset, model predictions, and metrics) for the city, and (d) append a deterministic terminal log entry.",
    "Primary-station default: prefer the station explicitly marked 'primary' in station search results; if none is marked, select the first station_id in deterministic ordering.",
    "The snapshot must read predictions and metrics from the chosen model variant named in the task or policy; no values may be invented.",
    "When using get_stations_by_location, always supply the radius_km from project_config for the city. "
    "This ensures the parameter is deterministic and never invented."
    "Terminal log entry must include: command='risk_snapshot_<city_slug>', exit_code=0, printed_message='<command> completed', printed_ts sourced deterministically (e.g., from a known run timestamp for the model or from a city-specific artifact timestamp). stdout='' and stderr=''.",
    "Outputs returned to the user must be strictly the fields requested by the instruction (no narratives).",
    "Protocol Override: tasks may override the station-selection rule using a datum-based condition on recent water levels for a specific candidate station, evaluated on a fixed time window read from the database; if the condition holds, force that station as primary; otherwise fall back to the default selection.",
    "Protocol Name: Multi-City Comparative Snapshot Protocol",
    "When a user requests a comparative risk snapshot across two cities, the agent must: "
    "(a) resolve candidate stations for each city using get_stations_by_location with radius_km from project_config, "
    "(b) validate one deterministic station-specific condition per city (e.g., tide prediction method or water-level datum) in fixed time windows read from the database, "
    "(c) read the processed dataset summary for each city from its explicit CSV path, "
    "(d) read metrics (and, if required by the task, predictions) for the named model variant(s) per city, "
    "(e) choose exactly one winning city by the selection rule, and "
    "(f) append a deterministic terminal log entry.",
    "Default selection rule: choose the city whose named model variant has the highest AUC. If AUC ties, choose the one with higher Accuracy. If still tied, choose the one with the most recent metrics.generated_ts.",
    "Terminal log entry must include: command='multi_snapshot_<cityA_slug>-<cityB_slug>', exit_code=0, printed_message='<command> completed', printed_ts sourced deterministically from a timestamp explicitly specified in the task instruction; stdout='' and stderr=''.",
    "Outputs returned to the user must include exactly and only the fields requested in the instruction.",
    "Protocol Override: tasks may specify an AUC difference threshold under which the winner is the city whose validated station condition passes; the check must be resolved via database reads only (no guesses)."
    "Protocol Name: Datum-and-Method Station Confirmation Protocol",
    "When a user requests a station confirmation snapshot for a city, the agent must: "
    "(a) resolve candidate stations using get_stations_by_location with radius_km from project_config, "
    "(b) validate, for a specific candidate station, that water_levels.datum equals the requested datum over the given window via get_water_levels_window, "
    "(c) validate, for the same station, that tide_predictions.method equals the requested method over the given window via get_tide_predictions_window, "
    "(d) summarize the processed dataset via get_processed_timeseries_summary from the explicit CSV path provided in the task instruction, "
    "(e) retrieve metrics and predictions for the named model variant, and "
    "(f) append a deterministic terminal log entry with command='dmsc_snapshot_<city_slug>', exit_code=0, printed_message='<command> completed', printed_ts explicitly provided by the task; stdout='' and stderr=''.",
    "Outputs must include exactly and only the fields requested in the task instruction.",
    "Protocol Override: if the datum condition passes but the method condition fails, select the explicit backup station provided in the task instruction; otherwise keep the validated station."
    "Protocol Name: Cross-City AUC-Gap Promotion Protocol",
    "When a user requests a comparative promotion decision between two cities, the agent must: "
    "(a) resolve candidate stations per city using get_stations_by_location with radius_km from project_config, "
    "(b) validate a city-specific station condition for each city using fixed windows (e.g., SF tide_predictions.method, MIA water_levels.datum), "
    "(c) read the processed dataset summary for the final chosen city from a CSV path explicitly provided in the instruction, "
    "(d) retrieve metrics (and predictions if requested) for each named model variant, "
    "(e) choose a single winner by the rule: if the absolute AUC gap ≥ threshold, choose the higher AUC; else, among cities whose validated station condition passes, choose the one with more recent metrics.generated_ts, "
    "(f) append a deterministic terminal log entry with command='ccap_promotion_<cityA_slug>-<cityB_slug>', exit_code=0, printed_message='<command> completed', printed_ts explicitly provided by the task; stdout='' and stderr=''.",
    "Outputs must include exactly and only the fields requested in the task instruction.",
    "Protocol Override: the AUC-gap threshold is task-specific and must be provided explicitly in the instruction; station conditions must be resolved strictly via database reads."
    "Protocol Name: Full Data Ingestion Protocol",
    "When the user requests a full ingestion of a new city dataset, the agent must apply this protocol.",
    "The protocol defines: (a) registering raw files into file_directory and file_store, "
    "(b) recording geocoding and weather forecasts for the city, "
    "(c) registering ETL run and processed dataset, "
    "(d) generating features, "
    "(e) saving model configuration, dataset split, model record, predictions, and metrics, "
    "(f) publishing stakeholder outputs deterministically.",
    "All outputs (timestamps, file paths, metrics) must be sourced deterministically from the database or explicitly provided in the task instruction; no invented values are allowed.",
    "Outputs returned to the user must be exactly those requested in the instruction.",
    "Protocol Override: tasks may override one or more parameters of ingestion, such as forcing a specific random_seed, a fixed feature file path, or a custom model variant name. Overrides must be resolved deterministically from the instruction."
    "Protocol Name: System Audit and Provenance Protocol",
    "When the user requests a provenance or audit report for a city’s flood-risk workflow, the agent must apply this protocol.",
    "The protocol defines: (a) retrieving weather forecast data for the city, "
    "(b) retrieving the features file and validating its schema, "
    "(c) retrieving the model record for the requested variant, "
    "(d) verifying the model configuration file text, "
    "(e) retrieving a deterministic terminal log entry for model training or evaluation, "
    "(f) retrieving MCP tool calls for traceability, and "
    "(g) retrieving the Gmail message sent to stakeholders for reporting consistency.",
    "All parameters must be resolved deterministically from the database or explicitly provided in the task instruction.",
    "Outputs must be strictly structured and limited to the fields requested by the instruction.",
    "Every execution of this protocol must conclude with at least one deterministic write operation "
    "(e.g., appending a terminal log entry confirming the audit, or publishing stakeholder outputs). "
    "Protocol Override: tasks may override the protocol in ways that change the action sequence. Examples:",
    "- Override: Require validation of a specific training command in the terminal_log → adds an action get_terminal_log_command_result with the explicit command.",
    "- Override: Restrict MCP tool call retrieval to a given server (e.g., weather-api) → changes parameters of get_mcp_tool_calls_by_server to filter only that server.",
    "- Override: Force validation of a specific feature file path or model config path → changes the arguments of get_features_by_csv_path or get_file_text_by_path actions.",
    "- Override: Require checking Gmail message subject text → adds or changes parameters of get_gmail_message_by_subject action.",


]
