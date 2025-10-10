RULES = [
    """
    You can call tools when needed in order to do the required task.
    """,
    """
    When using update_adset_status tool you can use "paused" for new_status parameter to pause an adset and "active" to activate it.
    """,
    """
    When using get_policy_param tool, available parameters are default_bid_strategy, max_daily_budget_total, min_roas_threshold_7d,
    creative_rotation_window_days, video_cpa_advantage_pct, budget_rounding_unit, currency, timezone,   
    max_bid_amount, min_budget_allocation,  canonical_bid_strategies, canonical_creative_types
    """,
    """
    When using add_automation_run tool, use for started_at and ended_at the timestamp returned by get_current_timestamp tool.
    """,
    """
    When using add_automation_run tool, use for status "completed" unless it is specififed otherwise.
    """,
    """
    When using add_automation_run tool, use for errors_json "{}" unless it is specififed otherwise.
    """,
    """
    When using add_campaign tool use id "12" unless it is specified otherwise
    """,
    """
    When using add_campaign tool use for created_date "2025-08-14" unless it is specified otherwise
    """,
    """
    When using add_campaign tool use for status "active" unless it is specified otherwise
    """,
    """
    When using add_adset tool to create a new adset, use id "114" unless it is specified otherwise
    """,
    """
    When using add_adset tool to create a new adset, for bid_strategy use "lowest_cost" unless it is specified otherwise
    """,
    """
    When using add_adset tool to create a new adset, for bid_amount use None unless it is specified otherwise
    """,
    """
    When using add_automation_run tool, for run_id use 'AR-APPLY-202508-01' unless it is specified otherwise
    """,
    """
    When using add_ads tool to create a new ad, for start_date use "2025-08-14" unless it is specified otherwise
    """,
    """
    When using add_ad tool to create a new ad, for end_date use None unless it is specified otherwise
    """,


    





]