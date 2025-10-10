import json
from datetime import datetime
from typing import Any, Dict, List, Optional
from domains.dto import Tool


# ==============================================================================
# 1. Planning & Policy Tools
# ==============================================================================

class GetPlanForDate(Tool):
    """Retrieves the entire frozen plan for a specific date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_date = kwargs.get("date")
        for plan in data.get('plans', []):
            if plan.get('date') == report_date:
                return json.dumps(plan)
        return json.dumps({"error": f"Plan for date '{report_date}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_plan_for_date", "description": "Retrieves the entire frozen plan for a specific date, including total budget and all ad set allocations.", "parameters": {"type": "object", "properties": {"date": {"type": "string", "description": "The date of the plan in YYYY-MM-DD format."}}, "required": ["date"]}}}

class GetAdsetAllocationFromPlan(Tool):
    """Retrieves a specific ad set's allocation from a plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        adset_id = kwargs.get("adset_id")
        for plan in data.get('plans', []):
            if plan.get('plan_id') == plan_id:
                for allocation in plan.get('allocations', []):
                    if allocation.get('adset_id') == adset_id:
                        return json.dumps(allocation)
        return json.dumps({"error": f"Allocation for ad set '{adset_id}' not found in plan '{plan_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan", "description": "Gets the planned budget, bid, and creative strategy for a single ad set from a specific plan.", "parameters": {"type": "object", "properties": {"plan_id": {"type": "string", "description": "The ID of the plan (e.g., 'plan_2025-08-13')."}, "adset_id": {"type": "string", "description": "The ID of the ad set to look up."}}, "required": ["plan_id", "adset_id"]}}}

class GetPolicyParameter(Tool):
    """Retrieves the value of a specific business rule."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        for param in data.get('policy_params', []):
            if param.get('param_name') == param_name:
                return json.dumps(param)
        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_policy_parameter", "description": "Retrieves the value of a specific business rule, like 'max_bid_amount'.", "parameters": {"type": "object", "properties": {"param_name": {"type": "string", "description": "The name of the policy parameter to retrieve."}}, "required": ["param_name"]}}}

# ==============================================================================
# 2. Campaign Management Tools
# ==============================================================================

class GetCampaignByName(Tool):
    """Retrieves a campaign's details by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for campaign in data.get('campaigns', []):
            if campaign.get('name') == name:
                return json.dumps(campaign)
        return json.dumps({"error": f"Campaign '{name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_campaign_by_name", "description": "Find a specific campaign by its exact name.", "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "The name of the campaign."}}, "required": ["name"]}}}

class CreateCampaign(Tool):
    """Creates a new advertising campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaigns = data.get('campaigns', [])
        new_id = max((int(c['campaign_id']) for c in campaigns), default=0) + 1
        new_campaign = {"campaign_id": str(new_id), "name": kwargs.get("name"), "objective": kwargs.get("objective"), "created_date": "2025-08-15", "status": "paused"}
        campaigns.append(new_campaign)
        data['campaigns'] = campaigns
        return json.dumps(new_campaign)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign", "description": "Creates a new advertising campaign. New campaigns always start with a 'paused' status.", "parameters": {"type": "object", "properties": {"name": {"type": "string"}, "objective": {"type": "string"}}, "required": ["name", "objective"]}}}

class UpdateCampaignStatus(Tool):
    """Changes the status of a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        new_status = kwargs.get("status")
        for campaign in data.get('campaigns', []):
            if campaign.get('campaign_id') == campaign_id:
                campaign['status'] = new_status
                return json.dumps(campaign)
        return json.dumps({"error": f"Campaign ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_campaign_status", "description": "Updates the status of a campaign (e.g., 'active', 'paused', 'archived').", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["campaign_id", "status"]}}}

class GetAdsetsByCampaignID(Tool):
    """Retrieves all ad sets belonging to a specific campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        adsets = [adset for adset in data.get('adsets', []) if adset.get('campaign_id') == campaign_id]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adsets_by_campaign_id", "description": "Retrieves a list of all ad sets that belong to a specific campaign ID.", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}}, "required": ["campaign_id"]}}}

# ==============================================================================
# 3. Ad Set & Ad Management Tools
# ==============================================================================

class GetAdsetDetailsByID(Tool):
    """Retrieves the details of a single ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_details_by_id", "description": "Retrieves the full details for a single ad set using its ID.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}}, "required": ["adset_id"]}}}

class CreateAdset(Tool):
    """Creates a new ad set within a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adsets = data.get('adsets', [])
        new_id = max((int(a['adset_id']) for a in adsets), default=100) + 1
        new_adset = {"adset_id": str(new_id), "campaign_id": kwargs.get("campaign_id"), "name": kwargs.get("name"), "category": kwargs.get("category"), "daily_budget": kwargs.get("daily_budget"), "bid_strategy": kwargs.get("bid_strategy"), "bid_amount": kwargs.get("bid_amount"), "status": "paused", "updated_at": "2025-08-15T00:00:00Z"}
        adsets.append(new_adset)
        data['adsets'] = adsets
        return json.dumps(new_adset)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset", "description": "Creates a new ad set within a specified campaign.", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}, "name": {"type": "string"}, "category": {"type": "string"}, "daily_budget": {"type": "number"}, "bid_strategy": {"type": "string"}, "bid_amount": {"type": "number"}}, "required": ["campaign_id", "name", "category", "daily_budget", "bid_strategy"]}}}

class UpdateAdsetBudget(Tool):
    """Updates the daily budget of an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_budget = kwargs.get("new_budget")
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                adset['daily_budget'] = new_budget
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_budget", "description": "Updates the daily budget for a specific ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "new_budget": {"type": "number"}}, "required": ["adset_id", "new_budget"]}}}

class UpdateAdsetBidStrategy(Tool):
    """Modifies the bid strategy for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                adset['bid_strategy'] = kwargs.get("bid_strategy")
                adset['bid_amount'] = kwargs.get("bid_amount")
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_bid_strategy", "description": "Updates the bidding strategy and bid amount for a given ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "bid_strategy": {"type": "string"}, "bid_amount": {"type": "number"}}, "required": ["adset_id", "bid_strategy"]}}}

class GetAdsByAdsetID(Tool):
    """Retrieves all ads within a specific ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        ads = [ad for ad in data.get('ads', []) if ad.get('adset_id') == adset_id]
        return json.dumps({"ads": ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ads_by_adset_id", "description": "Retrieves a list of all ads that belong to a specific ad set ID.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}}, "required": ["adset_id"]}}}

class CreateAd(Tool):
    """Creates a new ad creative."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = data.get('ads', [])
        new_id = max((int(a['ad_id']) for a in ads), default=1100) + 1
        new_ad = {"ad_id": str(new_id), "adset_id": kwargs.get("adset_id"), "name": kwargs.get("name"), "creative_type": kwargs.get("creative_type"), "status": "paused", "start_date": "2025-08-15", "end_date": None}
        ads.append(new_ad)
        data['ads'] = ads
        return json.dumps(new_ad)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_ad", "description": "Creates a new ad within a specified ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "name": {"type": "string"}, "creative_type": {"type": "string"}}, "required": ["adset_id", "name", "creative_type"]}}}

class UpdateAdStatus(Tool):
    """Changes the status of an individual ad."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        new_status = kwargs.get("status")
        for ad in data.get('ads', []):
            if ad.get('ad_id') == ad_id:
                ad['status'] = new_status
                return json.dumps(ad)
        return json.dumps({"error": f"Ad ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_ad_status", "description": "Updates the status of a single ad (e.g., 'active', 'paused').", "parameters": {"type": "object", "properties": {"ad_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["ad_id", "status"]}}}

class RotateAdCreative(Tool):
    """Pauses one ad and activates another."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_to_activate, ad_to_pause = kwargs.get("ad_id_to_activate"), kwargs.get("ad_id_to_pause")
        activated, paused = False, False
        for ad in data.get('ads', []):
            if ad.get('ad_id') == ad_to_activate:
                ad['status'], activated = 'active', True
            if ad.get('ad_id') == ad_to_pause:
                ad['status'], paused = 'paused', True
        if activated and paused:
            return json.dumps({"status": "success"})
        return json.dumps({"error": "One or both ad IDs not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "rotate_ad_creative", "description": "Activates one ad and pauses another, effectively rotating the active creative.", "parameters": {"type": "object", "properties": {"ad_id_to_activate": {"type": "string"}, "ad_id_to_pause": {"type": "string"}}, "required": ["ad_id_to_activate", "ad_id_to_pause"]}}}

# ==============================================================================
# 4. Performance & Analytics Tools
# ==============================================================================

class GetDailyInsightsForAdset(Tool):
    """Retrieves performance metrics for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id, report_date = kwargs.get("adset_id"), kwargs.get("date")
        for insight in data.get('f_insights', []):
            if insight.get('adset_id') == adset_id and insight.get('date') == report_date:
                return json.dumps(insight)
        return json.dumps({"error": "Insights not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset", "description": "Retrieves performance insights (spend, clicks, revenue) for one ad set on a specific date.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["adset_id", "date"]}}}

class CalculateAdsetRoasForDay(Tool):
    """Calculates Return On Ad Spend for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id, report_date = kwargs.get("adset_id"), kwargs.get("date")
        for insight in data.get('f_insights', []):
            if insight.get('adset_id') == adset_id and insight.get('date') == report_date:
                spend, revenue = insight.get('spend', 0), insight.get('revenue', 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                return json.dumps({"adset_id": adset_id, "roas": roas})
        return json.dumps({"error": "Could not calculate ROAS, insights not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_adset_roas_for_day", "description": "Calculates the Return On Ad Spend (Revenue / Spend) for an ad set on a specific date.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["adset_id", "date"]}}}

class GetAdsetSpendForDateRange(Tool):
    """Calculates total spend for an ad set over a range."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id, start_str, end_str = kwargs.get("adset_id"), kwargs.get("start_date"), kwargs.get("end_date")
        start, end = datetime.strptime(start_str, "%Y-%m-%d").date(), datetime.strptime(end_str, "%Y-%m-%d").date()
        total_spend = sum(i.get('spend', 0) for i in data.get('f_insights', []) if i.get('adset_id') == adset_id and start <= datetime.strptime(i['date'], "%Y-%m-%d").date() <= end)
        return json.dumps({"adset_id": adset_id, "start_date": start_str, "end_date": end_str, "total_spend": round(total_spend, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_spend_for_date_range", "description": "Calculates the total ad spend for a single ad set over an inclusive date range.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "start_date": {"type": "string"}, "end_date": {"type": "string"}}, "required": ["adset_id", "start_date", "end_date"]}}}

class GetWeeklySalesByCategory(Tool):
    """Retrieves weekly sales figures for a category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category, start_date = kwargs.get("category"), kwargs.get("start_date")
        for record in data.get('f_sales', []):
            if record.get('category') == category and record.get('start_date') == start_date:
                return json.dumps(record)
        return json.dumps({"error": "Sales data not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_weekly_sales_by_category", "description": "Retrieves the units sold and revenue for a product category for a specific week.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}, "start_date": {"type": "string"}}, "required": ["category", "start_date"]}}}

class GetViewershipForCategory(Tool):
    """Retrieves user engagement data for a category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category, report_date = kwargs.get("category"), kwargs.get("date")
        for record in data.get('f_viewership', []):
            if record.get('category') == category and record.get('date') == report_date:
                return json.dumps(record)
        return json.dumps({"error": "Viewership data not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category", "description": "Retrieves user session and engagement data for a category on a specific date.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}, "date": {"type": "string"}}, "required": ["category", "date"]}}}

class GetProductPriceOnDate(Tool):
    """Looks up the price of a product on a specific date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id, query_date = kwargs.get("product_id"), kwargs.get("date")
        for entry in data.get('f_price', []):
            if entry.get('product_id') == product_id and entry.get('date') == query_date:
                return json.dumps(entry)
        return json.dumps({"error": "Price not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_price_on_date", "description": "Retrieves the price of a specific product on a given date.", "parameters": {"type": "object", "properties": {"product_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["product_id", "date"]}}}

class FindUnderperformingAdsets(Tool):
    """Finds ad sets below a certain ROAS threshold."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        threshold, report_date = kwargs.get("roas_threshold"), kwargs.get("date")
        adsets = []
        for i in data.get('f_insights', []):
            if i.get('date') == report_date:
                spend, revenue = i.get('spend', 0), i.get('revenue', 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < threshold:
                    adsets.append({"adset_id": i['adset_id'], "roas": round(roas, 2)})
        return json.dumps({"underperforming_adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets", "description": "Finds all ad sets with a ROAS below a specified threshold for a given day.", "parameters": {"type": "object", "properties": {"roas_threshold": {"type": "number"}, "date": {"type": "string"}}, "required": ["roas_threshold", "date"]}}}

# ==============================================================================
# 5. Auditing & Logging Tools
# ==============================================================================

class GetAutomationRunHistory(Tool):
    """Retrieves automation run history for analysis and monitoring."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        status_filter = kwargs.get("status", None)
        limit = kwargs.get("limit", 10)

        runs = data.get('automation_runs', [])

        # Filter by run type if specified
        if run_type:
            runs = [r for r in runs if r.get('run_type') == run_type]

        # Filter by status if specified
        if status_filter:
            runs = [r for r in runs if r.get('status') == status_filter]

        # Sort by started_at (most recent first) and limit results
        runs.sort(key=lambda x: x.get('started_at', ''), reverse=True)
        runs = runs[:limit]

        # Calculate summary statistics
        total_runs = len(runs)
        success_count = len([r for r in runs if r.get('status') == 'completed'])
        failure_count = len([r for r in runs if r.get('status') == 'failed'])
        success_rate = round((success_count / total_runs * 100), 2) if total_runs > 0 else 0

        result = {
            "summary": {
                "total_runs": total_runs,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate_percent": success_rate
            },
            "runs": runs
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_automation_run_history", "description": "Retrieves automation run history with filtering and summary statistics for monitoring and analysis.", "parameters": {"type": "object", "properties": {"run_type": {"type": "string", "description": "Filter by specific automation type (e.g., 'plan_freeze', 'budget_apply')."}, "status": {"type": "string", "description": "Filter by run status (e.g., 'completed', 'failed', 'started')."}, "limit": {"type": "number", "description": "Maximum number of runs to return (default: 10)."}}, "required": []}}}

class GetLastSuccessfulRun(Tool):
    """Finds when a job type last completed successfully."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        successful_runs = [r for r in data.get('automation_runs', []) if r.get('run_type') == run_type and r.get('status') == 'completed']
        if not successful_runs:
            return json.dumps({"error": f"No successful run found for type '{run_type}'."})
        last_run = max(successful_runs, key=lambda x: x['ended_at'])
        return json.dumps(last_run)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_run", "description": "Reads the automation log to find when a specific job type last completed successfully.", "parameters": {"type": "object", "properties": {"run_type": {"type": "string"}}, "required": ["run_type"]}}}

class LogBudgetChange(Tool):
    """Adds an entry to the budget change log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        changes = data.get('budget_changes', [])
        new_id = f"BC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {"change_id": new_id, "adset_id": kwargs.get("adset_id"), "old_budget": kwargs.get("old_budget"), "new_budget": kwargs.get("new_budget"), "changed_at": "2025-08-15T01:00:00Z", "reason": kwargs.get("reason")}
        changes.append(new_log)
        data['budget_changes'] = changes
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_budget_change", "description": "Writes an audit log entry for an ad set budget change.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_budget": {"type": "number"}, "new_budget": {"type": "number"}, "reason": {"type": "string"}}, "required": ["adset_id", "old_budget", "new_budget", "reason"]}}}

class LogStrategyChange(Tool):
    """Adds an entry to the bid strategy change log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        changes = data.get('strategy_changes', [])
        new_id = f"SC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {"change_id": new_id, "adset_id": kwargs.get("adset_id"), "old_strategy": kwargs.get("old_strategy"), "new_strategy": kwargs.get("new_strategy"), "old_bid": kwargs.get("old_bid"), "new_bid": kwargs.get("new_bid"), "changed_at": "2025-08-15T02:00:00Z", "reason": kwargs.get("reason")}
        changes.append(new_log)
        data['strategy_changes'] = changes
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_strategy_change", "description": "Writes an audit log entry for an ad set bid strategy change.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_strategy": {"type": "string"}, "new_strategy": {"type": "string"}, "old_bid": {"type": "number"}, "new_bid": {"type": "number"}, "reason": {"type": "string"}}, "required": ["adset_id", "old_strategy", "new_strategy", "old_bid", "new_bid", "reason"]}}}

class LogCreativeRotation(Tool):
    """Adds an entry to the creative rotation log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rotations = data.get('creative_rotations', [])
        new_id = f"CR-{max((int(c['rotation_id'][3:]) for c in rotations), default=0) + 1}"
        new_log = {"rotation_id": new_id, "adset_id": kwargs.get("adset_id"), "old_ad_id": kwargs.get("old_ad_id"), "new_ad_id": kwargs.get("new_ad_id"), "rotated_at": "2025-08-15T03:00:00Z", "rationale": kwargs.get("rationale")}
        rotations.append(new_log)
        data['creative_rotations'] = rotations
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_creative_rotation", "description": "Writes an audit log entry for an ad creative rotation.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_ad_id": {"type": "string"}, "new_ad_id": {"type": "string"}, "rationale": {"type": "string"}}, "required": ["adset_id", "old_ad_id", "new_ad_id", "rationale"]}}}

# ==============================================================================
# 6. Data Lookup Tools
# ==============================================================================

class GetAdsetsByCategory(Tool):
    """Finds ad sets targeting a specific product category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        adsets = [adset for adset in data.get('adsets', []) if adset.get('category') == category]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adsets_by_category", "description": "Retrieves a list of ad sets that are targeting a specific product category.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}}, "required": ["category"]}}}


# ==============================================================================
# Final list of all 28 tools available to the agent
# ==============================================================================

TOOLS = [
    # Planning & Policy
    GetPlanForDate(),
    GetAdsetAllocationFromPlan(),
    GetPolicyParameter(),
    # Campaign Management
    GetCampaignByName(),
    CreateCampaign(),
    UpdateCampaignStatus(),
    GetAdsetsByCampaignID(),
    # Ad Set & Ad Management
    GetAdsetDetailsByID(),
    CreateAdset(),
    UpdateAdsetBudget(),
    UpdateAdsetBidStrategy(),
    GetAdsByAdsetID(),
    CreateAd(),
    UpdateAdStatus(),
    RotateAdCreative(),
    # Performance & Analytics
    GetDailyInsightsForAdset(),
    CalculateAdsetRoasForDay(),
    GetAdsetSpendForDateRange(),
    GetWeeklySalesByCategory(),
    GetViewershipForCategory(),
    GetProductPriceOnDate(),
    FindUnderperformingAdsets(),
    # Auditing & Logging
    GetAutomationRunHistory(),
    GetLastSuccessfulRun(),
    LogBudgetChange(),
    LogStrategyChange(),
    LogCreativeRotation(),
    # Data Lookups
    GetAdsetsByCategory(),
]
