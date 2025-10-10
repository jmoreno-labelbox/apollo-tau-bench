from domains.dto import Tool
import json
from typing import Dict, Any
from datetime import datetime, timedelta


class GetCampaigns(Tool):
    """Retrieves all advertising campaigns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaigns = data.get("campaigns", [])
        ids_ = []
        for i in campaigns:
            ids_ += [i.get("campaign_id")]
        return json.dumps({"campaigns_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_campaigns",
                "description": "Retrieves all advertising campaign ids.",
                "parameters": {},
            },
        }

class GetNameForCampaign(Tool):
    """Retrieves a specific campaign by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        campaigns = data.get("campaigns", [])
        
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                return json.dumps({"name": campaign.get('name')})
        
        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_campaign",
                "description": "Retrieves a specific campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }

class GetObjectiveForCampaign(Tool):
    """Retrieves the objective for a specific campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        campaigns = data.get("campaigns", [])
        
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                return json.dumps({"objective": campaign.get('objective')})
        
        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_objective_for_campaign",
                "description": "Retrieves the objective for a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }

class GetStatusForCampaign(Tool):
    """Retrieves the status for a specific campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        campaigns = data.get("campaigns", [])
        
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                return json.dumps({"status": campaign.get('status')})
        
        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_status_for_campaign",
                "description": "Retrieves the status for a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


class UpdateCampaignStatus(Tool):
    """Updates the status of a campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        new_status = kwargs.get("new_status")
        
        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                old_status = campaign['status']
                campaign['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Campaign status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Campaign {campaign_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_campaign_status",
                "description": "Updates the status of a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["campaign_id", "new_status"]
                }
            }
        }


class GetAdSets(Tool):
    """Retrieves all ad set IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adsets = data.get("adsets", [])
        ids_ = []
        for i in adsets:
            ids_ += [i.get("adset_id")]
        return json.dumps({"adset_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adsets",
                "description": "Retrieves all ad set IDs.",
                "parameters": {},
            },
        }

class GetNameForAdSet(Tool):
    """Retrieves the name for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"name": adset.get('name')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_adset",
                "description": "Retrieves the name for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }

class GetCampaignIdForAdSet(Tool):
    """Retrieves the campaign ID for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"campaign_id": adset.get('campaign_id')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_campaign_id_for_adset",
                "description": "Retrieves the campaign ID for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }

class GetDailyBudgetForAdSet(Tool):
    """Retrieves the daily budget for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"daily_budget": adset.get('daily_budget')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_daily_budget_for_adset",
                "description": "Retrieves the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }

class UpdateDailyBudgetForAdSet(Tool):
    """Updates the daily budget for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_budget = kwargs.get("new_budget")
        
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_budget = adset['daily_budget']
                adset['daily_budget'] = new_budget
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set budget updated from {old_budget} to {new_budget}"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_daily_budget_for_adset",
                "description": "Updates the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"}
                    },
                    "required": ["adset_id", "new_budget"]
                }
            }
        }

class GetAds(Tool):
    """Retrieves all ad IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = data.get("ads", [])
        ids_ = []
        for i in ads:
            ids_ += [i.get("ad_id")]
        return json.dumps({"ad_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_ads",
                "description": "Retrieves all ad IDs.",
                "parameters": {},
            },
        }

class GetNameForAd(Tool):
    """Retrieves the name for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        ads = data.get("ads", [])
        
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                return json.dumps({"name": ad.get('name')})
        
        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_ad",
                "description": "Retrieves the name for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }


class GetCreativeTypeForAd(Tool):
    """Retrieves the creative_type for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        ads = data.get("ads", [])
        
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                return json.dumps({"creative_type": ad.get('creative_type')})
        
        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_creative_type_for_ad",
                "description": "Retrieves the creative_type for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }


class GetStatusForAd(Tool):
    """Retrieves the status for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        ads = data.get("ads", [])
        
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                return json.dumps({"status": ad.get('status')})
        
        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_status_for_ad",
                "description": "Retrieves the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }

class UpdateAdStatus(Tool):
    """Updates the status for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        new_status = kwargs.get("new_status")
        
        ads = data.get("ads", [])
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                old_status = ad['status']
                ad['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Ad status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ad_status",
                "description": "Updates the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["ad_id", "new_status"]
                }
            }
        }


class GetProducts(Tool):
    """Retrieves all product IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("dim_product", [])
        ids_ = []
        for i in products:
            ids_ += [i.get("product_id")]
        return json.dumps({"product_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products",
                "description": "Retrieves all product IDs.",
                "parameters": {},
            },
        }

class GetNameForProduct(Tool):
    """Retrieves the name for a specific product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        products = data.get("dim_product", [])
        
        for product in products:
            if product.get("product_id") == product_id:
                return json.dumps({"name": product.get('name')})
        
        return json.dumps({"error": f"Product with ID '{product_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_product",
                "description": "Retrieves the name for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class GetPlans(Tool):
    """Retrieves all plan IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plans = data.get("plans", [])
        ids_ = []
        for i in plans:
            ids_ += [i.get("plan_id")]
        return json.dumps({"plan_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_plans",
                "description": "Retrieves all plan IDs.",
                "parameters": {},
            },
        }

class GetDateForPlan(Tool):
    """Retrieves the date for a specific plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        plans = data.get("plans", [])
        
        for plan in plans:
            if plan.get("plan_id") == plan_id:
                return json.dumps({"date": plan.get('date')})
        
        return json.dumps({"error": f"Plan with ID '{plan_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_date_for_plan",
                "description": "Retrieves the date for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }


class GetAutomationRuns(Tool):
    """Retrieves all automation run IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("automation_runs", [])
        ids_ = []
        for i in runs:
            ids_ += [i.get("run_id")]
        return json.dumps({"automation_run_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_automation_runs",
                "description": "Retrieves all automation run IDs.",
                "parameters": {},
            },
        }

class GetRunTypeForAutomationRun(Tool):
    """Retrieves the run type for a specific automation run."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        runs = data.get("automation_runs", [])
        
        for run in runs:
            if run.get("run_id") == run_id:
                return json.dumps({"run_type": run.get('run_type')})
        
        return json.dumps({"error": f"Automation run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_run_type_for_automation_run",
                "description": "Retrieves the run type for a specific automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        }
                    },
                    "required": ["run_id"],
                },
            },
        }



class GetBudgetChanges(Tool):
    """Retrieves all budget change IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        changes = data.get("budget_changes", [])
        ids_ = []
        for i in changes:
            ids_ += [i.get("change_id")]
        return json.dumps({"budget_change_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_budget_changes",
                "description": "Retrieves all budget change IDs.",
                "parameters": {},
            },
        }

class GetAdSetIdForBudgetChange(Tool):
    """Retrieves the ad set ID for a specific budget change."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        change_id = kwargs.get("change_id")
        changes = data.get("budget_changes", [])
        
        for change in changes:
            if change.get("change_id") == change_id:
                return json.dumps({"adset_id": change.get('adset_id')})
        
        return json.dumps({"error": f"Budget change with ID '{change_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adset_id_for_budget_change",
                "description": "Retrieves the ad set ID for a specific budget change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "change_id": {
                            "type": "string",
                            "description": "The unique ID of the budget change.",
                        }
                    },
                    "required": ["change_id"],
                },
            },
        }


class SearchCampaignsByObjective(Tool):
    """Searches for campaigns with a specific objective."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        objective = kwargs.get("objective")
        campaigns = data.get("campaigns", [])
        matching_campaigns = []
        
        for campaign in campaigns:
            if campaign.get("objective") == objective:
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_objective",
                "description": "Searches for campaigns with a specific objective.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "objective": {
                            "type": "string",
                            "description": "The objective to search for (e.g., Sales, Awareness, Traffic).",
                        }
                    },
                    "required": ["objective"],
                },
            },
        }

class SearchCampaignsByStatus(Tool):
    """Searches for campaigns with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        campaigns = data.get("campaigns", [])
        matching_campaigns = []
        
        for campaign in campaigns:
            if campaign.get("status") == status:
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_status",
                "description": "Searches for campaigns with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchAdSetsByCategory(Tool):
    """Searches for ad sets with a specific category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("category") == category:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_category",
                "description": "Searches for ad sets with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }

class SearchAdSetsByStatus(Tool):
    """Searches for ad sets with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("status") == status:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_status",
                "description": "Searches for ad sets with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchAdsByCreativeType(Tool):
    """Searches for ads with a specific creative type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        creative_type = kwargs.get("creative_type")
        ads = data.get("ads", [])
        matching_ads = []
        
        for ad in ads:
            if ad.get("creative_type") == creative_type:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_creative_type",
                "description": "Searches for ads with a specific creative type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type to search for (e.g., image, video, carousel).",
                        }
                    },
                    "required": ["creative_type"],
                },
            },
        }

class SearchAdsByStatus(Tool):
    """Searches for ads with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        ads = data.get("ads", [])
        matching_ads = []
        
        for ad in ads:
            if ad.get("status") == status:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_status",
                "description": "Searches for ads with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchProductsByCategory(Tool):
    """Searches for products with a specific category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        products = data.get("dim_product", [])
        matching_products = []
        
        for product in products:
            if product.get("category") == category:
                matching_products.append(product.get("product_id"))
        
        return json.dumps({"product_ids": matching_products})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_category",
                "description": "Searches for products with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }


class SearchAutomationRunsByType(Tool):
    """Searches for automation runs with a specific run type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        runs = data.get("automation_runs", [])
        matching_runs = []
        
        for run in runs:
            if run.get("run_type") == run_type:
                matching_runs.append(run.get("run_id"))
        
        return json.dumps({"automation_run_ids": matching_runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_automation_runs_by_type",
                "description": "Searches for automation runs with a specific run type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "The run type to search for (e.g., plan_freeze, budget_apply, creative_rotation).",
                        }
                    },
                    "required": ["run_type"],
                },
            },
        }

class SearchAutomationRunsByStatus(Tool):
    """Searches for automation runs with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        runs = data.get("automation_runs", [])
        matching_runs = []
        
        for run in runs:
            if run.get("status") == status:
                matching_runs.append(run.get("run_id"))
        
        return json.dumps({"automation_run_ids": matching_runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_automation_runs_by_status",
                "description": "Searches for automation runs with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., completed, failed).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchBudgetChangesByAdSet(Tool):
    """Searches for budget changes for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        changes = data.get("budget_changes", [])
        matching_changes = []
        
        for change in changes:
            if change.get("adset_id") == adset_id:
                matching_changes.append(change.get("change_id"))
        
        return json.dumps({"budget_change_ids": matching_changes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_budget_changes_by_adset",
                "description": "Searches for budget changes for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


# Campaign Delete/Add Tools
class DeleteCampaign(Tool):
    """Deletes a campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})

        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                data['campaigns'] = [d for d in data['campaigns'] if d['campaign_id'] != campaign_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Campaign with id {campaign_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_campaign",
                "description": "Deletes a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign to delete.",
                        },
                    },
                    "required": ["campaign_id"],
                },
            },
        }

class AddCampaign(Tool):
    """Adds a new campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        name = kwargs.get("name")
        objective = kwargs.get("objective")
        created_date = kwargs.get("created_date")
        status = kwargs.get("status")

        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not objective:
            return json.dumps({"error": "objective is a required parameter."})
        if not created_date:
            return json.dumps({"error": "created_date is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})

        new_campaign = {
            "campaign_id": campaign_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status
        }
        data['campaigns'] += [new_campaign]

        return json.dumps(
            {
                "status": "success",
                "message": f"New campaign was added: {new_campaign}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_campaign",
                "description": "Adds a new campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the new campaign.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the campaign.",
                        },
                        "objective": {
                            "type": "string",
                            "description": "The objective of the campaign (e.g., Sales, Awareness, Traffic).",
                        },
                        "created_date": {
                            "type": "string",
                            "description": "The creation date of the campaign (YYYY-MM-DD format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the campaign (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["campaign_id", "name", "objective", "created_date", "status"],
                },
            },
        }

# AdSet Delete/Add Tools
class DeleteAdSet(Tool):
    """Deletes an ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})

        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                data['adsets'] = [d for d in data['adsets'] if d['adset_id'] != adset_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Ad set with id {adset_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_adset",
                "description": "Deletes an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set to delete.",
                        },
                    },
                    "required": ["adset_id"],
                },
            },
        }

class AddAdSet(Tool):
    """Adds a new ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        campaign_id = kwargs.get("campaign_id")
        name = kwargs.get("name")
        category = kwargs.get("category")
        daily_budget = kwargs.get("daily_budget")
        bid_strategy = kwargs.get("bid_strategy")
        bid_amount = kwargs.get("bid_amount")
        status = kwargs.get("status")
        updated_at = kwargs.get("updated_at")

        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not category:
            return json.dumps({"error": "category is a required parameter."})
        if not daily_budget:
            return json.dumps({"error": "daily_budget is a required parameter."})
        if not bid_strategy:
            return json.dumps({"error": "bid_strategy is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not updated_at:
            return json.dumps({"error": "updated_at is a required parameter."})

        new_adset = {
            "adset_id": adset_id,
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": status,
            "updated_at": updated_at
        }
        data['adsets'] += [new_adset]

        return json.dumps(
            {
                "status": "success",
                "message": f"New ad set was added: {new_adset}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_adset",
                "description": "Adds a new ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad set.",
                        },
                        "campaign_id": {
                            "type": "string",
                            "description": "The ID of the campaign this ad set belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad set.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the ad set (e.g., Electronics, Apparel).",
                        },
                        "daily_budget": {
                            "type": "number",
                            "description": "The daily budget for the ad set.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy (e.g., lowest_cost, cost_cap).",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount (if applicable).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad set (e.g., active, paused).",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "The last update timestamp (ISO format).",
                        }
                    },
                    "required": ["adset_id", "campaign_id", "name", "category", "daily_budget", "bid_strategy", "status", "updated_at"],
                },
            },
        }

# Ad Delete/Add Tools
class DeleteAd(Tool):
    """Deletes an ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        if not ad_id:
            return json.dumps({"error": "ad_id is a required parameter."})

        ads = data.get("ads", [])
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                data['ads'] = [d for d in data['ads'] if d['ad_id'] != ad_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Ad with id {ad_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_ad",
                "description": "Deletes an ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad to delete.",
                        },
                    },
                    "required": ["ad_id"],
                },
            },
        }

class AddAd(Tool):
    """Adds a new ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        adset_id = kwargs.get("adset_id")
        name = kwargs.get("name")
        creative_type = kwargs.get("creative_type")
        status = kwargs.get("status")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not ad_id:
            return json.dumps({"error": "ad_id is a required parameter."})
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not creative_type:
            return json.dumps({"error": "creative_type is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not start_date:
            return json.dumps({"error": "start_date is a required parameter."})

        new_ad = {
            "ad_id": ad_id,
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date
        }
        data['ads'] += [new_ad]

        return json.dumps(
            {
                "status": "success",
                "message": f"New ad was added: {new_ad}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_ad",
                "description": "Adds a new ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad.",
                        },
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set this ad belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type (e.g., image, video, carousel).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad (e.g., active, paused, archived).",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the ad (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the ad (YYYY-MM-DD format, optional).",
                        }
                    },
                    "required": ["ad_id", "adset_id", "name", "creative_type", "status", "start_date"],
                },
            },
        }

# Product Delete/Add Tools
class DeleteProduct(Tool):
    """Deletes a product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        if not product_id:
            return json.dumps({"error": "product_id is a required parameter."})

        products = data.get("dim_product", [])
        for product in products:
            if product.get("product_id") == product_id:
                data['dim_product'] = [d for d in data['dim_product'] if d['product_id'] != product_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Product with id {product_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Product with ID '{product_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_product",
                "description": "Deletes a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product to delete.",
                        },
                    },
                    "required": ["product_id"],
                },
            },
        }

class AddProduct(Tool):
    """Adds a new product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        sku = kwargs.get("sku")
        name = kwargs.get("name")
        category = kwargs.get("category")

        if not product_id:
            return json.dumps({"error": "product_id is a required parameter."})
        if not sku:
            return json.dumps({"error": "sku is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not category:
            return json.dumps({"error": "category is a required parameter."})

        new_product = {
            "product_id": product_id,
            "sku": sku,
            "name": name,
            "category": category
        }
        data['dim_product'] += [new_product]

        return json.dumps(
            {
                "status": "success",
                "message": f"New product was added: {new_product}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_product",
                "description": "Adds a new product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the new product.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product (e.g., Electronics, Apparel).",
                        }
                    },
                    "required": ["product_id", "sku", "name", "category"],
                },
            },
        }


class SearchAdSetsByCampaignId(Tool):
    """Searches for ad sets belonging to a specific campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("campaign_id") == campaign_id:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_campaign_id",
                "description": "Searches for ad sets belonging to a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID to search for ad sets.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


# Calculation and Comparison Tools
class CalculateROAS(Tool):
    """Calculates Return on Ad Spend (ROAS) from revenue and spend."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        revenue = kwargs.get("revenue")
        spend = kwargs.get("spend")
        
        if revenue is None or spend is None:
            return json.dumps({"error": "revenue and spend are required parameters."})
        
        if spend == 0:
            return json.dumps({"error": "spend cannot be zero."})
        
        roas = revenue / spend
        return json.dumps({"roas": roas})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_roas",
                "description": "Calculates Return on Ad Spend (ROAS) from revenue and spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "revenue": {
                            "type": "number",
                            "description": "The revenue generated.",
                        },
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        }
                    },
                    "required": ["revenue", "spend"],
                },
            },
        }

class CalculateCPA(Tool):
    """Calculates Cost Per Acquisition (CPA) from spend and purchases."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        spend = kwargs.get("spend")
        purchases = kwargs.get("purchases")
        
        if spend is None or purchases is None:
            return json.dumps({"error": "spend and purchases are required parameters."})
        
        if purchases == 0:
            return json.dumps({"error": "purchases cannot be zero."})
        
        cpa = spend / purchases
        return json.dumps({"cpa": cpa})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_cpa",
                "description": "Calculates Cost Per Acquisition (CPA) from spend and purchases.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                        "purchases": {
                            "type": "number",
                            "description": "The number of purchases.",
                        }
                    },
                    "required": ["spend", "purchases"],
                },
            },
        }

class CompareValue(Tool):
    """Compares a value with a threshold using a specified operator."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        value = kwargs.get("value")
        threshold = kwargs.get("threshold")
        operator = kwargs.get("operator")
        
        if value is None or threshold is None or operator is None:
            return json.dumps({"error": "value, threshold, and operator are required parameters."})
        
        result = False
        if operator == "greater":
            result = value > threshold
        elif operator == "greater_equal":
            result = value >= threshold
        elif operator == "less":
            result = value < threshold
        elif operator == "less_equal":
            result = value <= threshold
        elif operator == "equal":
            result = value == threshold
        else:
            return json.dumps({"error": f"Unknown operator: {operator}"})
        
        return json.dumps({"result": result})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_value",
                "description": "Compares a value with a threshold using a specified operator.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The value to compare.",
                        },
                        "threshold": {
                            "type": "number",
                            "description": "The threshold value.",
                        },
                        "operator": {
                            "type": "string",
                            "description": "The comparison operator (greater, greater_equal, less, less_equal, equal).",
                        }
                    },
                    "required": ["value", "threshold", "operator"],
                },
            },
        }

class IncreaseValueWithPercent(Tool):
    """Increases a value by a specified percentage."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        value = kwargs.get("value")
        percent = kwargs.get("percent")
        
        if value is None or percent is None:
            return json.dumps({"error": "value and percent are required parameters."})
        
        new_value = value * (100 + percent) / 100
        return json.dumps({"new_value": new_value})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "increase_value_with_percent",
                "description": "Increases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to increase by.",
                        }
                    },
                    "required": ["value", "percent"],
                },
            },
        }

# Audit Logging Tools
class LogBudgetChange(Tool):
    """Adds a new entry to the budget_changes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        old_budget = kwargs.get("old_budget")
        new_budget = kwargs.get("new_budget")
        changed_at = kwargs.get("changed_at")
        reason = kwargs.get("reason")
        
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not old_budget:
            return json.dumps({"error": "old_budget is a required parameter."})
        if not new_budget:
            return json.dumps({"error": "new_budget is a required parameter."})
        if not changed_at:
            return json.dumps({"error": "changed_at is a required parameter."})
        if not reason:
            return json.dumps({"error": "reason is a required parameter."})

        new_budget_change = {
            "change_id": f"BC-{adset_id}",
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason
        }
        
        if "budget_changes" not in data:
            data["budget_changes"] = []
            
        data['budget_changes'].append(new_budget_change)

        return json.dumps(
            {
                "status": "success",
                "message": f"New budget change was added: {new_budget_change}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_budget_change",
                "description": "Adds a new entry to the budget_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_budget": {
                            "type": "number",
                            "description": "The old budget value.",
                        },
                        "new_budget": {
                            "type": "number",
                            "description": "The new budget value.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the budget change.",
                        }
                    },
                    "required": ["change_id", "adset_id", "old_budget", "new_budget", "changed_at", "reason"],
                },
            },
        }

class LogStrategyChange(Tool):
    """Adds a new entry to the strategy_changes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        old_strategy = kwargs.get("old_strategy")
        new_strategy = kwargs.get("new_strategy")
        old_bid = kwargs.get("old_bid")
        new_bid = kwargs.get("new_bid")
        changed_at = kwargs.get("changed_at")
        reason = kwargs.get("reason")
        
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not old_strategy:
            return json.dumps({"error": "old_strategy is a required parameter."})
        if not new_strategy:
            return json.dumps({"error": "new_strategy is a required parameter."})
        if not changed_at:
            return json.dumps({"error": "changed_at is a required parameter."})
        if not reason:
            return json.dumps({"error": "reason is a required parameter."})

        new_strategy_change = {
            "change_id": f"SC-{adset_id}",
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason
        }
        
        if "strategy_changes" not in data:
            data["strategy_changes"] = []
            
        data['strategy_changes'].append(new_strategy_change)

        return json.dumps(
            {
                "status": "success",
                "message": f"New strategy change was added: {new_strategy_change}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_strategy_change",
                "description": "Adds a new entry to the strategy_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_strategy": {
                            "type": "string",
                            "description": "The old bid strategy.",
                        },
                        "new_strategy": {
                            "type": "string",
                            "description": "The new bid strategy.",
                        },
                        "old_bid": {
                            "type": "number",
                            "description": "The old bid amount.",
                        },
                        "new_bid": {
                            "type": "number",
                            "description": "The new bid amount.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the strategy change.",
                        }
                    },
                    "required": ["adset_id", "old_strategy", "new_strategy", "changed_at", "reason"],
                },
            },
        }

class AddAutomationRun(Tool):
    """Adds a new entry to the automation_runs table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        run_type = kwargs.get("run_type")
        started_at = kwargs.get("started_at")
        ended_at = kwargs.get("ended_at")
        status = kwargs.get("status")
        input_ref = kwargs.get("input_ref")
        errors_json = kwargs.get("errors_json")
        reason = kwargs.get("reason")
        
        if not run_id:
            return json.dumps({"error": "run_id is a required parameter."})
        if not run_type:
            return json.dumps({"error": "run_type is a required parameter."})
        if not started_at:
            return json.dumps({"error": "started_at is a required parameter."})
        if not ended_at:
            return json.dumps({"error": "ended_at is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not input_ref:
            return json.dumps({"error": "input_ref is a required parameter."})
        if not errors_json:
            return json.dumps({"error": "errors_json is a required parameter."})

        new_automation_run = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json
        }
        
        if reason:
            new_automation_run["reason"] = reason
            
        if "automation_runs" not in data:
            data["automation_runs"] = []
            
        data['automation_runs'].append(new_automation_run)

        return json.dumps(
            {
                "status": "success",
                "message": f"New automation run was added: {new_automation_run}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_automation_run",
                "description": "Adds a new entry to the automation_runs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        },
                        "run_type": {
                            "type": "string",
                            "description": "The type of automation run.",
                        },
                        "started_at": {
                            "type": "string",
                            "description": "The start timestamp (ISO format).",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "The end timestamp (ISO format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the run.",
                        },
                        "input_ref": {
                            "type": "string",
                            "description": "The input reference for the run.",
                        },
                        "errors_json": {
                            "type": "string",
                            "description": "JSON string of any errors.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the automation run.",
                        }
                    },
                    "required": ["run_id", "run_type", "started_at", "ended_at", "status", "input_ref", "errors_json"],
                },
            },
        }

# Bid Strategy Tools
class UpdateBidStrategyForAdSet(Tool):
    """Updates the bid strategy for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_strategy = kwargs.get("new_strategy")
        new_bid = kwargs.get("new_bid")
        
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_strategy = adset['bid_strategy']
                old_bid = adset['bid_amount']
                adset['bid_strategy'] = new_strategy
                adset['bid_amount'] = new_bid
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set bid strategy updated from '{old_strategy}' to '{new_strategy}' with bid {new_bid}"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_bid_strategy_for_adset",
                "description": "Updates the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "new_bid": {"type": "number"}
                    },
                    "required": ["adset_id", "new_strategy", "new_bid"]
                }
            }
        }

# AdSet Status Tools
class UpdateAdSetStatus(Tool):
    """Updates the status for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_status = kwargs.get("new_status")
        
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_status = adset['status']
                adset['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_adset_status",
                "description": "Updates the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["adset_id", "new_status"]
                }
            }
        }

# Plan Management Tools
class CreatePlanAllocation(Tool):
    """Creates a plan allocation for an ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        budget = kwargs.get("budget")
        bid_strategy = kwargs.get("bid_strategy")
        bid_amount = kwargs.get("bid_amount")
        creative_type = kwargs.get("creative_type")
        
        # This tool would typically be used in the context of creating a full plan
        # For now, we'll just return the allocation details
        allocation = {
            "adset_id": adset_id,
            "budget": budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "creative_type": creative_type
        }
        
        return json.dumps({
            "status": "success",
            "allocation": allocation
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_plan_allocation",
                "description": "Creates a plan allocation for an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "budget": {
                            "type": "number",
                            "description": "The allocated budget.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy.",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type.",
                        }
                    },
                    "required": ["adset_id", "budget", "bid_strategy", "creative_type"],
                },
            },
        }


# Policy Parameter Tools
class GetPolicyParam(Tool):
    """Retrieves a policy parameter value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        policy_params = data.get("policy_params", [])
        
        for param in policy_params:
            if param.get("param_name") == param_name:
                return json.dumps({"param_value": param.get("param_value")})
        
        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_param",
                "description": "Retrieves a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {
                            "type": "string",
                            "description": "The name of the policy parameter.",
                        }
                    },
                    "required": ["param_name"],
                },
            },
        }

class UpdatePolicyParam(Tool):
    """Updates a policy parameter value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        param_value = kwargs.get("param_value")
        updated_at = kwargs.get("updated_at")
        
        policy_params = data.get("policy_params", [])
        for param in policy_params:
            if param.get("param_name") == param_name:
                old_value = param['param_value']
                param['param_value'] = param_value
                param['updated_at'] = updated_at
                return json.dumps({
                    "status": "success",
                    "message": f"Policy parameter '{param_name}' updated from '{old_value}' to '{param_value}'"
                })

        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_policy_param",
                "description": "Updates a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {"type": "string"},
                        "param_value": {"type": "string"},
                        "updated_at": {"type": "string"}
                    },
                    "required": ["param_name", "param_value", "updated_at"]
                }
            }
        }

# Additional helper tools
class CheckNoPurchases(Tool):
    """Checks if a list of purchase counts contains only zeros."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        purchases_list = kwargs.get("purchases_list")
        
        if purchases_list is None:
            return json.dumps({"error": "purchases_list is a required parameter."})
        
        all_zeros = all(purchase == 0 for purchase in purchases_list)
        return json.dumps({"all_zeros": all_zeros})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_no_purchases",
                "description": "Checks if a list of purchase counts contains only zeros.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "purchases_list": {
                            "type": "array",
                            "description": "List of purchase counts.",
                            "items": {
                                "type": "number"
                            }
                        }
                    },
                    "required": ["purchases_list"],
                },
            },
        }

class CalculatePercentageChange(Tool):
    """Calculates the percentage change in revenue between two values."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_value = kwargs.get("current_value")
        previous_value = kwargs.get("previous_value")
        
        if current_value is None or previous_value is None:
            return json.dumps({"error": "current_value and previous_value are required parameters."})
        
        if previous_value == 0:
            return json.dumps({"error": "previous_value cannot be zero."})
        
        change_percent = ((current_value - previous_value) / previous_value) * 100
        return json.dumps({"change_percent": change_percent})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_percentage_change",
                "description": "Calculates the percentage change between two values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_value": {
                            "type": "number",
                            "description": "The current value.",
                        },
                        "previous_value": {
                            "type": "number",
                            "description": "The previous value.",
                        }
                    },
                    "required": ["current_value", "previous_value"],
                },
            },
        }

class CalculateSpendVariance(Tool):
    """Calculates the variance percentage between planned and actual spend."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        planned_spend = kwargs.get("planned_spend")
        actual_spend = kwargs.get("actual_spend")
        
        if planned_spend is None or actual_spend is None:
            return json.dumps({"error": "planned_spend and actual_spend are required parameters."})
        
        if planned_spend == 0:
            return json.dumps({"error": "planned_spend cannot be zero."})
        
        variance_percent = ((actual_spend - planned_spend) / planned_spend) * 100
        return json.dumps({"variance_percent": variance_percent})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_spend_variance",
                "description": "Calculates the variance percentage between planned and actual spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "planned_spend": {
                            "type": "number",
                            "description": "The planned spend amount.",
                        },
                        "actual_spend": {
                            "type": "number",
                            "description": "The actual spend amount.",
                        }
                    },
                    "required": ["planned_spend", "actual_spend"],
                },
            },
        }



class CalculateCampaignROASForPeriod(Tool):
    """Calculates ROAS for a campaign over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        
        adsets = data.get("adsets", [])
        campaign_adsets = [adset for adset in adsets if adset.get("campaign_id") == campaign_id]
        adset_ids = [adset.get("adset_id") for adset in campaign_adsets]
        
        insights = data.get("f_insights", [])
        total_revenue = 0
        total_spend = 0
        
        for insight in insights:
            if insight.get("adset_id") in adset_ids and start_date <= insight.get("date") <= end_date:
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)
        
        if total_spend == 0:
            return json.dumps({"error": "No spend found for the period."})
        
        roas = total_revenue / total_spend
        return json.dumps({"roas": roas})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_campaign_roas_for_period",
                "description": "Calculates ROAS for a campaign over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["campaign_id", "start_date", "end_date"],
                },
            },
        }


class CalculateROASForAdSetForPeriod(Tool):
    """Calculates ROAS for a specific ad set over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        insights = data.get("f_insights", [])
        total_revenue = 0
        total_spend = 0
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and start_date <= insight.get("date") <= end_date:
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)
        
        if total_spend == 0:
            return json.dumps({"error": "No spend found for the period."})
        
        roas = total_revenue / total_spend
        return json.dumps({"roas": roas})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_roas_for_period",
                "description": "Calculates ROAS for a specific ad set over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }

class CalculateCPAForAdSetForPeriod(Tool):
    """Calculates CPA for a specific ad set over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        insights = data.get("f_insights", [])
        total_spend = 0
        total_purchases = 0
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and start_date <= insight.get("date") <= end_date:
                total_spend += insight.get("spend", 0)
                total_purchases += insight.get("purchases", 0)
        
        if total_purchases == 0:
            return json.dumps({'cpa': 0})
            return json.dumps({"error": "No purchases found for the period."})
        
        cpa = total_spend / total_purchases
        return json.dumps({"cpa": cpa})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_cpa_for_period",
                "description": "Calculates CPA for a specific ad set over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }

class CalculateROASForAdSetForDay(Tool):
    """Calculates ROAS for a specific ad set on a specific day."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        date = kwargs.get("date")
        insights = data.get("f_insights", [])
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                revenue = insight.get("revenue", 0)
                spend = insight.get("spend", 0)
                if spend == 0:
                    return json.dumps({"error": "Spend is zero, cannot calculate ROAS."})
                roas = revenue / spend
                return json.dumps({"roas": roas})
        
        return json.dumps({"error": f"No insights found for ad set {adset_id} on date {date}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_roas_for_day",
                "description": "Calculates ROAS for a specific ad set on a specific day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }

class CalculateCPAForAdSetForDay(Tool):
    """Calculates CPA for a specific ad set on a specific day."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        date = kwargs.get("date")
        insights = data.get("f_insights", [])
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                spend = insight.get("spend", 0)
                purchases = insight.get("purchases", 0)
                if purchases == 0:
                    return json.dumps({"error": "No purchases, cannot calculate CPA."})
                cpa = spend / purchases
                return json.dumps({"cpa": cpa})
        
        return json.dumps({"error": f"No insights found for ad set {adset_id} on date {date}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_cpa_for_day",
                "description": "Calculates CPA for a specific ad set on a specific day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }


class SearchAdSetsByName(Tool):
    """Searches for ad sets with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if name_query.lower() in adset.get("name", "").lower():
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_name",
                "description": "Searches for ad sets with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad set names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchCampaignsByName(Tool):
    """Searches for campaigns with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        campaigns = data.get("campaigns", [])
        matching_campaigns = []
        
        for campaign in campaigns:
            if name_query.lower() in campaign.get("name", "").lower():
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_name",
                "description": "Searches for campaigns with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in campaign names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class GetCurrentTimestamp(Tool):
    """Returns a hardcoded current timestamp value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"timestamp": "2025-08-13T01:01:01Z"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_timestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }


class DeleteAutomationRun(Tool):
    """Deletes an automation run record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        if not run_id:
            return json.dumps({"error": "run_id is a required parameter."})

        runs = data.get("automation_runs", [])
        original_count = len(runs)
        data['automation_runs'] = [r for r in runs if r.get("run_id") != run_id]

        if len(data['automation_runs']) < original_count:
            return json.dumps({
                "status": "success",
                "message": f"Automation run with id {run_id} deleted successfully."
            })
        else:
            return json.dumps({"error": f"Automation run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_automation_run",
                "description": "Deletes an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run to delete.",
                        },
                    },
                    "required": ["run_id"],
                },
            },
        }


class AddPlan(Tool):
    """Adds a new plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        date = kwargs.get("date")
        author = kwargs.get("author")
        allocations = kwargs.get("allocations")

        if not all([plan_id, date, author, allocations]):
            return json.dumps({"error": "plan_id, date, author, and allocations are required parameters."})

        # Basic validation for allocations
        if not isinstance(allocations, list):
            return json.dumps({"error": "allocations must be a list."})

        total_budget = sum(alloc.get('budget', 0) for alloc in allocations)

        new_plan = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": "2025-08-13T01:01:01Z",  # Using hardcoded timestamp for consistency
            "checksum": "manual_override_checksum",
            "allocations": allocations
        }

        if "plans" not in data:
            data["plans"] = []
        data['plans'].append(new_plan)

        return json.dumps({
            "status": "success",
            "message": f"New plan was added: {new_plan}",
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_plan",
                "description": "Adds a new plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "author": {"type": "string"},
                        "allocations": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["plan_id", "date", "author", "allocations"],
                },
            },
        }

class GetStatusForAdSet(Tool):
    """Retrieves the status for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"status": adset.get('status')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_status_for_adset",
                "description": "Retrieves the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }

class DecreaseValueWithPercent(Tool):
    """Decreases a value by a specified percentage."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        value = kwargs.get("value")
        percent = kwargs.get("percent")
        
        if value is None or percent is None:
            return json.dumps({"error": "value and percent are required parameters."})
        
        new_value = value * (100 - percent) / 100
        return json.dumps({"new_value": new_value})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decrease_value_with_percent",
                "description": "Decreases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to decrease by.",
                        }
                    },
                    "required": ["value", "percent"],
                },
            },
        }


class RoundNumberToUnit(Tool):
    """Rounds a number to the nearest multiple of a specified unit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        number = kwargs.get("number")
        unit = kwargs.get("unit")
        
        if number is None or unit is None:
            return json.dumps({"error": "number and unit are required parameters."})
        
        if unit <= 0:
            return json.dumps({"error": "unit must be a positive number."})
        
        rounded_number = round(number / unit) * unit
        return json.dumps({"rounded_number": rounded_number})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "round_number_to_unit",
                "description": "Rounds a number to the nearest multiple of a specified unit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "number",
                            "description": "The number to round.",
                        },
                        "unit": {
                            "type": "number",
                            "description": "The unit to round to (e.g., 10 for rounding to nearest 10).",
                        }
                    },
                    "required": ["number", "unit"],
                },
            },
        }


class SearchAdsByName(Tool):
    """Searches for ads with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        ads = data.get("ads", [])
        matching_ads = []
        
        for ad in ads:
            if name_query.lower() in ad.get("name", "").lower():
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_name",
                "description": "Searches for ads with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }

class SearchAdsByAdSet(Tool):
    """Searches for ads belonging to a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        ads = data.get("ads", [])
        matching_ads = []
        
        for ad in ads:
            if ad.get("adset_id") == adset_id:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_adset",
                "description": "Searches for ads belonging to a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for ads.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetBidStrategyForAdSet(Tool):
    """Retrieves the bid strategy for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"bid_strategy": adset.get('bid_strategy')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bid_strategy_for_adset",
                "description": "Retrieves the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }

class GetBidAmountForAdSet(Tool):
    """Retrieves the bid amount for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"bid_amount": adset.get('bid_amount')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bid_amount_for_adset",
                "description": "Retrieves the bid amount for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetAllocationsForPlan(Tool):
    """Retrieves the allocations for a specific plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        plans = data.get("plans", [])
        
        for plan in plans:
            if plan.get("plan_id") == plan_id:
                return json.dumps({"allocations": plan.get('allocations', [])})
        
        return json.dumps({"error": f"Plan with ID '{plan_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_allocations_for_plan",
                "description": "Retrieves the allocations for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }


class GetCategoryForProduct(Tool):
    """Retrieves the category for a specific product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        products = data.get("dim_product", [])
        
        for product in products:
            if product.get("product_id") == product_id:
                return json.dumps({"category": product.get('category')})
        
        return json.dumps({"error": f"Product with ID '{product_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_category_for_product",
                "description": "Retrieves the category for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }

class SearchProductsByName(Tool):
    """Searches for products with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        products = data.get("dim_product", [])
        matching_products = []
        
        for product in products:
            if name_query.lower() in product.get("name", "").lower():
                matching_products.append(product.get("product_id"))
        
        return json.dumps({"product_ids": matching_products})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_name",
                "description": "Searches for products with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in product names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchAdSetsByBidStrategy(Tool):
    """Searches for ad sets with a specific bid strategy."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bid_strategy = kwargs.get("bid_strategy")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("bid_strategy") == bid_strategy:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_bid_strategy",
                "description": "Searches for ad sets with a specific bid strategy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy to search for (e.g., cost_cap, lowest_cost).",
                        }
                    },
                    "required": ["bid_strategy"],
                },
            },
        }

class GetBidStrategyForAdSet(Tool):
    """Retrieves the bid strategy for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = data.get("adsets", [])
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"bid_strategy": adset.get('bid_strategy')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bid_strategy_for_adset",
                "description": "Retrieves the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }



class GetViewershipForDateAndCategory(Tool):
    """Retrieves viewership data for a specific date and category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        category = kwargs.get("category")
        viewership_data = data.get("f_viewership", [])
        
        for entry in viewership_data:
            if entry.get("date") == date and entry.get("category") == category:
                return json.dumps({
                    "sessions": entry.get("sessions"),
                    "active_users": entry.get("active_users")
                })
        
        return json.dumps({"error": f"No viewership data found for category '{category}' on date '{date}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_viewership_for_date_and_category",
                "description": "Retrieves viewership data for a specific date and category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date to get viewership for (YYYY-MM-DD format).",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category to get viewership for.",
                        }
                    },
                    "required": ["date", "category"],
                },
            },
        }

class GetTotalViewershipForCategoryInPeriod(Tool):
    """Calculates total viewership for a category over a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        viewership_data = data.get("f_viewership", [])
        
        total_sessions = 0
        total_active_users = 0
        
        for entry in viewership_data:
            if (entry.get("category") == category and 
                start_date <= entry.get("date") <= end_date):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
        
        return json.dumps({
            "total_sessions": total_sessions,
            "total_active_users": total_active_users
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_total_viewership_for_category_in_period",
                "description": "Calculates total viewership for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        }
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }

class GetAverageViewershipForCategoryInPeriod(Tool):
    """Calculates average daily viewership for a category over a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        viewership_data = data.get("f_viewership", [])
        
        # Calculate the number of days in the period
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1
        
        total_sessions = 0
        total_active_users = 0
        days_with_data = 0
        
        for entry in viewership_data:
            if (entry.get("category") == category and 
                start_date <= entry.get("date") <= end_date):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
                days_with_data += 1
        
        # Calculate averages
        avg_sessions = total_sessions / days_in_period if days_in_period > 0 else 0
        avg_active_users = total_active_users / days_in_period if days_in_period > 0 else 0
        
        return json.dumps({
            "average_sessions": avg_sessions,
            "average_active_users": avg_active_users,
            "days_in_period": days_in_period,
            "days_with_data": days_with_data
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_average_viewership_for_category_in_period",
                "description": "Calculates average daily viewership for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        }
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }



class GetSalesForCategoryInPeriod(Tool):
    """Retrieves sales data for a specific category and date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        sales_data = data.get("f_sales", [])
        
        matching_sales = []
        
        for entry in sales_data:
            if (entry.get("category") == category and 
                entry.get("start_date") >= start_date and 
                entry.get("end_date") <= end_date):
                matching_sales.append(entry)
        
        return json.dumps({"sales_data": matching_sales})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sales_for_category_in_period",
                "description": "Retrieves sales data for a specific category and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        }
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


class GetAverageDailySalesForCategoryInPeriod(Tool):
    """Calculates average daily sales for a category over a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        sales_data = data.get("f_sales", [])
        
        # Calculate the number of days in the period
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1
        
        total_units = 0
        total_revenue = 0
        
        for entry in sales_data:
            if (entry.get("category") == category and 
                entry.get("start_date") >= start_date and 
                entry.get("end_date") <= end_date):
                total_units += entry.get("units", 0)
                total_revenue += entry.get("revenue", 0)
        
        # Calculate averages
        avg_units = total_units / days_in_period if days_in_period > 0 else 0
        avg_revenue = total_revenue / days_in_period if days_in_period > 0 else 0
        
        return json.dumps({
            "average_units": avg_units,
            "average_revenue": avg_revenue,
            "days_in_period": days_in_period
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_average_daily_sales_for_category_in_period",
                "description": "Calculates average daily sales for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        }
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


# --- List of all available tools ---
TOOLS = [
    GetCampaigns(),
    GetNameForCampaign(),
    GetObjectiveForCampaign(),
    GetStatusForCampaign(),
    UpdateCampaignStatus(),
    GetAdSets(),
    GetNameForAdSet(),
    GetCampaignIdForAdSet(),
    GetDailyBudgetForAdSet(),
    UpdateDailyBudgetForAdSet(),
    GetAds(),
    GetNameForAd(),
    GetStatusForAd(),
    UpdateAdStatus(),
    GetProducts(),
    GetNameForProduct(),
    GetPlans(),
    GetDateForPlan(),
    GetAutomationRuns(),
    GetRunTypeForAutomationRun(),
    GetBudgetChanges(),
    GetAdSetIdForBudgetChange(),
    SearchCampaignsByObjective(),
    SearchCampaignsByStatus(),
    SearchAdSetsByCategory(),
    SearchAdSetsByStatus(),
    SearchAdsByCreativeType(),
    SearchAdsByStatus(),
    SearchProductsByCategory(),
    SearchAutomationRunsByType(),
    SearchAutomationRunsByStatus(),
    SearchBudgetChangesByAdSet(),
    DeleteCampaign(),
    AddCampaign(),
    DeleteAdSet(),
    AddAdSet(),
    DeleteAd(),
    AddAd(),
    DeleteProduct(),
    AddProduct(),
    SearchAdSetsByCampaignId(),
    CalculateROAS(),
    CalculateCPA(),
    CompareValue(),
    IncreaseValueWithPercent(),
    LogBudgetChange(),
    LogStrategyChange(),
    AddAutomationRun(),
    UpdateBidStrategyForAdSet(),
    UpdateAdSetStatus(),
    CreatePlanAllocation(),
    GetPolicyParam(),
    UpdatePolicyParam(),
    CheckNoPurchases(),
    CalculatePercentageChange(),
    CalculateSpendVariance(),

    CalculateCampaignROASForPeriod(),
    CalculateROASForAdSetForPeriod(),
    CalculateCPAForAdSetForPeriod(),
    CalculateROASForAdSetForDay(),
    CalculateCPAForAdSetForDay(),

    SearchAdSetsByName(),
    SearchCampaignsByName(),

    GetCurrentTimestamp(),

    DeleteAutomationRun(),
    AddPlan(),
    GetStatusForAdSet(),
    DecreaseValueWithPercent(),
    RoundNumberToUnit(),
    SearchAdsByName(),
    SearchAdsByAdSet(),

    GetCreativeTypeForAd(),
    GetBidStrategyForAdSet(),
    GetBidAmountForAdSet(),
    GetAllocationsForPlan(),
    GetCategoryForProduct(),
    SearchProductsByName(),
    SearchAdSetsByBidStrategy(),
    GetBidStrategyForAdSet(),

    GetViewershipForDateAndCategory(),
    GetTotalViewershipForCategoryInPeriod(),
    GetAverageViewershipForCategoryInPeriod(),
    GetSalesForCategoryInPeriod(),
    GetAverageDailySalesForCategoryInPeriod(),
]