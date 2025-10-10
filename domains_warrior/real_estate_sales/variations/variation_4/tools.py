from domains.dto import Tool
from typing import Dict, Any
import json


class FindListings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listings = data.get('listings', [])
        results = []
        
        status = kwargs.get('status')
        min_price = kwargs.get('min_price', 0)
        max_price = kwargs.get('max_price', float('inf'))
        property_id = kwargs.get('property_id')
        
        for listing in listings:
            if property_id and listing.get('property_id') != property_id:
                continue
            if status and listing.get('status') != status:
                continue
            
            price = listing.get('list_price', 0)
            if not (min_price <= price <= max_price):
                continue
                
            results.append(listing)
        
        return json.dumps(results, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_listings",
                "description": "find property listings matching specific criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Listing status (for_sale, sold, pending, etc.)"
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price range"
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price range"
                        },
                        "property_id": {
                            "type": "string",
                            "description": "Specific property ID to search for"
                        }
                    },
                    "required": []
                }
            }
        }


class FetchListingDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listing_id = kwargs.get('listing_id')
        if not listing_id:
            return json.dumps({"error": "listing_id is required"}, indent=2)
        
        listings = data.get('listings', [])
        listing = next((l for l in listings if l.get('listing_id') == listing_id), None)
        
        if not listing:
            return json.dumps({"error": f"Listing {listing_id} not found"}, indent=2)
        
        return json.dumps(listing, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listing_details",
                "description": "Fetch detailed information about a specific property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "The unique identifier for the listing"
                        }
                    },
                    "required": ["listing_id"]
                }
            }
        }


class FindClients(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        clients = data.get('client_preferences', [])
        if not clients:
            return json.dumps({"error": "No client data available"}, indent=2)
        
        results = []
        name_query = kwargs.get('name', '').lower()
        client_id = kwargs.get('client_id')
        
        for client in clients:
            if client_id and client.get('client_id') != client_id:
                continue
            if name_query and name_query not in client.get('name', '').lower():
                continue
            
            results.append(client)
        
        return json.dumps(results, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_clients",
                "description": "Find clients by name or ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Client name to find for (partial match)"
                        },
                        "client_id": {
                            "type": "string",
                            "description": "Specific client ID"
                        }
                    },
                    "required": []
                }
            }
        }


class CalculateMortgage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        principal = kwargs.get('principal')
        interest_rate = kwargs.get('interest_rate')
        loan_term_years = kwargs.get('loan_term_years', 30)
        
        if not principal or not interest_rate:
            return json.dumps({
                "error": "principal and interest_rate are required"
            }, indent=2)
        
        monthly_rate = interest_rate / 100 / 12
        num_payments = loan_term_years * 12
        
        if monthly_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
        
        result = {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(monthly_payment * num_payments, 2),
            "total_interest": round((monthly_payment * num_payments) - principal, 2),
            "loan_details": {
                "principal": principal,
                "interest_rate": interest_rate,
                "loan_term_years": loan_term_years
            }
        }
        
        return json.dumps(result, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_mortgage",
                "description": "Calculate monthly mortgage payment and loan details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "principal": {
                            "type": "number",
                            "description": "Loan amount in dollars"
                        },
                        "interest_rate": {
                            "type": "number",
                            "description": "Annual interest rate as percentage (e.g., 5.5 for 5.5%)"
                        },
                        "loan_term_years": {
                            "type": "integer",
                            "description": "Loan term in years (default: 30)"
                        }
                    },
                    "required": ["principal", "interest_rate"]
                }
            }
        }


class ScheduleOpenHouse(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        date = kwargs.get('date')
        start_time = kwargs.get('start_time')
        end_time = kwargs.get('end_time')
        
        if not all([property_id, date, start_time, end_time]):
            return json.dumps({
                "error": "property_id, date, start_time, and end_time are required"
            }, indent=2)
        
        listings = data.get('listings', [])
        property_exists = any(l.get('property_id') == property_id for l in listings)
        
        if not property_exists:
            return json.dumps({
                "error": f"Property {property_id} not found in listings"
            }, indent=2)
        
        open_house = {
            "property_id": property_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "message": f"Open house scheduled for property {property_id}",
            "open_house": open_house
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_open_house",
                "description": "Schedule an open house event for a property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to schedule open house for"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format"
                        },
                        "start_time": {
                            "type": "string",
                            "description": "Start time in HH:MM format"
                        },
                        "end_time": {
                            "type": "string",
                            "description": "End time in HH:MM format"
                        }
                    },
                    "required": ["property_id", "date", "start_time", "end_time"]
                }
            }
        }


class CreatePropertyReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        
        listings = data.get('listings', [])
        listing = next((l for l in listings if l.get('property_id') == property_id), None)
        
        if not listing:
            return json.dumps({
                "error": f"Property {property_id} not found"
            }, indent=2)
        
        comparables = data.get('comparables', [])
        property_comparables = [c for c in comparables if c.get('property_id') == property_id]
        
        all_prices = [c.get('comparable_price', 0) for c in property_comparables]
        if all_prices:
            avg_comparable_price = sum(all_prices) / len(all_prices)
            price_variance = listing.get('list_price', 0) - avg_comparable_price
        else:
            avg_comparable_price = 0
            price_variance = 0
        
        report = {
            "property_id": property_id,
            "listing_details": listing,
            "market_analysis": {
                "comparable_count": len(property_comparables),
                "average_comparable_price": round(avg_comparable_price, 2),
                "price_variance": round(price_variance, 2),
                "price_competitive": abs(price_variance) < 50000
            },
            "comparables": property_comparables,
            "report_generated_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps(report, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_property_report",
                "description": "Create a comprehensive property report with market analysis",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to generate report for"
                        }
                    },
                    "required": ["property_id"]
                }
            }
        }


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get('name')
        campaign_type = kwargs.get('type')
        created_by = kwargs.get('created_by')
        
        if not all([name, campaign_type, created_by]):
            return json.dumps({
                "error": "name, type, and created_by are required"
            }, indent=2)
        
        campaign = {
            "campaign_id": 101,
            "name": name,
            "type": campaign_type,
            "created_by": created_by,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "campaign_id": 101,
            "campaign": campaign
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_campaign",
                "description": "Create a marketing campaign for client outreach",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Campaign name"
                        },
                        "type": {
                            "type": "string",
                            "description": "Campaign type (likely_buyer, general_update, etc.)"
                        },
                        "created_by": {
                            "type": "integer",
                            "description": "Broker ID creating the campaign"
                        }
                    },
                    "required": ["name", "type", "created_by"]
                }
            }
        }


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        subject = kwargs.get('subject')
        template_code = kwargs.get('template_code')
        body_uri = kwargs.get('body_uri')
        campaign_id = kwargs.get('campaign_id')
        
        if not all([client_id, broker_id, subject, template_code]):
            return json.dumps({
                "error": "client_id, broker_id, subject, and template_code are required"
            }, indent=2)
        
        import time
        timestamp = str(int(time.time() * 1000))
        email_id = f"EMAIL-{client_id}-{timestamp}"
        email = {
            "email_id": email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "template_code": template_code,
            "body_uri": body_uri,
            "campaign_id": campaign_id,
            "sent_at": "2024-08-21T00:00:00Z",
            "status": "sent"
        }
        
        return json.dumps({
            "success": True,
            "email_id": email_id,
            "message": f"Email sent to client {client_id}",
            "email": email
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email to a client and record it",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to send email to"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID sending the email"
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject line"
                        },
                        "template_code": {
                            "type": "string",
                            "description": "Email template code"
                        },
                        "body_uri": {
                            "type": "string",
                            "description": "URI to email body content"
                        },
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to associate with email"
                        }
                    },
                    "required": ["client_id", "broker_id", "subject", "template_code"]
                }
            }
        }


class FetchEmailsForClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        if not client_id:
            return json.dumps({"error": "client_id is required"}, indent=2)
        
        emails = data.get('emails', [])
        client_emails = [e for e in emails if e.get('client_id') == client_id]
        
        return json.dumps({
            "client_id": client_id,
            "email_count": len(client_emails),
            "emails": client_emails
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_emails_for_client",
                "description": "Retrieve all emails sent to a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get emails for"
                        }
                    },
                    "required": ["client_id"]
                }
            }
        }


class CreateCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get('broker_id')
        client_id = kwargs.get('client_id')
        title = kwargs.get('title')
        start_at = kwargs.get('start_at')
        end_at = kwargs.get('end_at')
        location = kwargs.get('location')
        notes = kwargs.get('notes')
        source = kwargs.get('source')
        
        if not all([broker_id, client_id, title, start_at, end_at]):
            return json.dumps({
                "error": "broker_id, client_id, title, start_at, and end_at are required"
            }, indent=2)
        
        import time
        timestamp = str(int(time.time() * 1000))
        event_id = f"EVENT-{client_id}-{timestamp}"
        event = {
            "event_id": event_id,
            "broker_id": broker_id,
            "client_id": client_id,
            "title": title,
            "start_at": start_at,
            "end_at": end_at,
            "location": location,
            "notes": notes,
            "source": source,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "event_id": event_id,
            "message": f"Calendar event created for client {client_id}",
            "event": event
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_calendar_event",
                "description": "Create a calendar event for client meetings or appointments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the event"
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the event"
                        },
                        "title": {
                            "type": "string",
                            "description": "Event title"
                        },
                        "start_at": {
                            "type": "string",
                            "description": "Start time in ISO format"
                        },
                        "end_at": {
                            "type": "string",
                            "description": "End time in ISO format"
                        },
                        "location": {
                            "type": "string",
                            "description": "Event location"
                        },
                        "notes": {
                            "type": "string",
                            "description": "Event notes"
                        },
                        "source": {
                            "type": "string",
                            "description": "Event source (client_meeting, follow_up, viewing, etc.)"
                        }
                    },
                    "required": ["broker_id", "client_id", "title", "start_at", "end_at"]
                }
            }
        }


class GetCalendarEventsForClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        if not client_id:
            return json.dumps({"error": "client_id is required"}, indent=2)
        
        events = data.get('calendar_events', [])
        client_events = [e for e in events if e.get('client_id') == client_id]
        
        return json.dumps({
            "client_id": client_id,
            "event_count": len(client_events),
            "events": client_events
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_calendar_events_for_client",
                "description": "Retrieve calendar events for a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get events for"
                        }
                    },
                    "required": ["client_id"]
                }
            }
        }


class GetCampaignDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get('campaign_id')
        if not campaign_id:
            return json.dumps({"error": "campaign_id is required"}, indent=2)
        
        campaigns = data.get('campaigns', [])
        campaign = next((c for c in campaigns if c.get('campaign_id') == campaign_id), None)
        
        if not campaign:
            mock_campaign = {
                "campaign_id": campaign_id,
                "name": f"Campaign {campaign_id}",
                "type": "general_update",
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z"
            }
            return json.dumps(mock_campaign, indent=2)
        
        return json.dumps(campaign, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_campaign_details",
                "description": "Get details about a specific marketing campaign",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to get details for"
                        }
                    },
                    "required": ["campaign_id"]
                }
            }
        }


class BuildRoute(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        date = kwargs.get('date')
        stops_ordered_json = kwargs.get('stops_ordered_json')
        map_url = kwargs.get('map_url')
        created_by_broker_id = kwargs.get('created_by_broker_id')
        
        if not all([client_id, date, stops_ordered_json, created_by_broker_id]):
            return json.dumps({
                "error": "client_id, date, stops_ordered_json, and created_by_broker_id are required"
            }, indent=2)
        
        route = {
            "route_id": 401,
            "client_id": client_id,
            "date": date,
            "stops_ordered": stops_ordered_json,
            "map_url": map_url,
            "created_by_broker_id": created_by_broker_id,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "route_id": 401,
            "message": f"Route created for client {client_id}",
            "route": route
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_route",
                "description": "Build a property showing route for clients",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the route"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date for the route in YYYY-MM-DD format"
                        },
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Ordered list of property IDs to visit"
                        },
                        "map_url": {
                            "type": "string",
                            "description": "URL to the route map"
                        },
                        "created_by_broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the route"
                        }
                    },
                    "required": ["client_id", "date", "stops_ordered_json", "created_by_broker_id"]
                }
            }
        }


class GetRouteDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        route_id = kwargs.get('route_id')
        if not route_id:
            return json.dumps({"error": "route_id is required"}, indent=2)
        
        routes = data.get('routes', [])
        route = next((r for r in routes if r.get('route_id') == route_id), None)
        
        if not route:
            mock_route = {
                "route_id": route_id,
                "client_id": 5,
                "date": "2024-09-25",
                "stops_ordered": ["HTX007", "HTX008", "HTX009"],
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z"
            }
            return json.dumps(mock_route, indent=2)
        
        return json.dumps(route, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_route_details",
                "description": "Get details about a specific property route",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {
                            "type": "integer",
                            "description": "Route ID to get details for"
                        }
                    },
                    "required": ["route_id"]
                }
            }
        }


class PostAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        actor_id = kwargs.get('actor_id')
        action = kwargs.get('action')
        entity_type = kwargs.get('entity_type')
        entity_id = kwargs.get('entity_id')
        metadata_json = kwargs.get('metadata_json')
        
        if not all([actor_id, action, entity_type, entity_id]):
            return json.dumps({
                "error": "actor_id, action, entity_type, and entity_id are required"
            }, indent=2)
        
        audit_event = {
            "audit_id": 501,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "metadata": metadata_json,
            "timestamp": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "audit_id": 501,
            "message": f"Audit event recorded: {action}",
            "audit_event": audit_event
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_audit_event",
                "description": "Record an audit event for tracking system actions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "integer",
                            "description": "ID of the user performing the action"
                        },
                        "action": {
                            "type": "string",
                            "description": "Action being performed"
                        },
                        "entity_type": {
                            "type": "string",
                            "description": "Type of entity being acted upon"
                        },
                        "entity_id": {
                            "type": "integer",
                            "description": "ID of the entity being acted upon"
                        },
                        "metadata_json": {
                            "type": "object",
                            "description": "Additional metadata about the action"
                        }
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"]
                }
            }
        }


class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_ids = kwargs.get('property_ids')
        max_minutes = kwargs.get('max_minutes', 30)
        
        if not property_ids:
            return json.dumps({
                "error": "property_ids is required"
            }, indent=2)
        
        feasible = len(property_ids) <= 4
        
        result = {
            "feasible": feasible,
            "property_count": len(property_ids),
            "max_minutes_per_hop": max_minutes,
            "estimated_total_time": len(property_ids) * 25,
            "properties_checked": property_ids
        }
        
        return json.dumps(result, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_drive_time_constraints",
                "description": "Check if properties can be visited within time constraints",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of property IDs to check"
                        },
                        "max_minutes": {
                            "type": "integer",
                            "description": "Maximum minutes allowed between stops"
                        }
                    },
                    "required": ["property_ids"]
                }
            }
        }


class ListListingsByIds(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listing_ids = kwargs.get('listing_ids')
        if not listing_ids:
            return json.dumps({"error": "listing_ids is required"}, indent=2)
        
        listings = data.get('listings', [])
        found_listings = []
        
        for listing_id in listing_ids:
            listing = next((l for l in listings if l.get('listing_id') == listing_id), None)
            if listing:
                found_listings.append(listing)
        
        return json.dumps({
            "requested_ids": listing_ids,
            "found_count": len(found_listings),
            "listings": found_listings
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_listings_by_ids",
                "description": "Get multiple listings by their IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of listing IDs to retrieve"
                        }
                    },
                    "required": ["listing_ids"]
                }
            }
        }


class UpdateListingStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listing_id = kwargs.get('listing_id')
        new_status = kwargs.get('new_status')
        updated_by = kwargs.get('updated_by')
        
        if not all([listing_id, new_status, updated_by]):
            return json.dumps({
                "error": "listing_id, new_status, and updated_by are required"
            }, indent=2)
        
        result = {
            "success": True,
            "listing_id": listing_id,
            "previous_status": "for_sale",
            "new_status": new_status,
            "updated_by": updated_by,
            "updated_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps(result, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_listing_status",
                "description": "Update the status of a property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "Listing ID to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status (for_sale, pending, sold, etc.)"
                        },
                        "updated_by": {
                            "type": "integer",
                            "description": "Broker ID making the update"
                        }
                    },
                    "required": ["listing_id", "new_status", "updated_by"]
                }
            }
        }


class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        
        if not all([client_id, broker_id]):
            return json.dumps({
                "error": "client_id and broker_id are required"
            }, indent=2)
        
        import time
        timestamp = str(int(time.time() * 1000))
        document_id = f"DOC-{client_id}-{timestamp}"
        document = {
            "document_id": document_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "document_type": "briefing",
            "title": f"Client Briefing - Client {client_id}",
            "file_path": f"https://storage.example.com/briefings/client_{client_id}_briefing.pdf",
            "status": "generated",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "document_id": document_id,
            "message": f"Briefing document generated for client {client_id}",
            "document": document
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_briefing_doc",
                "description": "Generate a briefing document for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to generate briefing for"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID generating the briefing"
                        }
                    },
                    "required": ["client_id", "broker_id"]
                }
            }
        }


class AttachDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        document_id = kwargs.get('document_id')
        
        if not all([client_id, document_id]):
            return json.dumps({
                "error": "client_id and document_id are required"
            }, indent=2)
        
        attachment = {
            "attachment_id": 701,
            "client_id": client_id,
            "document_id": document_id,
            "attached_at": "2024-08-21T00:00:00Z",
            "status": "attached"
        }
        
        return json.dumps({
            "success": True,
            "attachment_id": 701,
            "message": f"Document {document_id} attached to client {client_id}",
            "attachment": attachment
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_document_to_client",
                "description": "Attach a document to a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to attach document to"
                        },
                        "document_id": {
                            "type": "integer",
                            "description": "Document ID to attach"
                        }
                    },
                    "required": ["client_id", "document_id"]
                }
            }
        }


class GetMortgageRates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loan_type = kwargs.get('loan_type', 'conventional')
        term_years = kwargs.get('term_years', 30)
        
        rates = data.get('mortgage_rates', [])
        filtered_rates = []
        
        for rate in rates:
            if (rate.get('loan_type') == loan_type and 
                rate.get('term_years') == term_years):
                filtered_rates.append(rate)
        
        return json.dumps({
            "loan_type": loan_type,
            "term_years": term_years,
            "rate_count": len(filtered_rates),
            "rates": filtered_rates
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mortgage_rates",
                "description": "Get current mortgage rates from available lenders",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_type": {
                            "type": "string",
                            "description": "Type of loan (conventional, fha, va, etc.)"
                        },
                        "term_years": {
                            "type": "integer",
                            "description": "Loan term in years (15, 30, etc.)"
                        }
                    },
                    "required": []
                }
            }
        }


class SearchNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get('city')
        min_avg_price = kwargs.get('min_avg_price', 0)
        max_avg_price = kwargs.get('max_avg_price', float('inf'))
        
        neighborhoods = data.get('neighborhoods', [])
        results = []
        
        for neighborhood in neighborhoods:
            avg_price = neighborhood.get('avg_home_price', 0)
            if city and city.lower() not in neighborhood.get('city', '').lower():
                continue
            if not (min_avg_price <= avg_price <= max_avg_price):
                continue
            results.append(neighborhood)
        
        return json.dumps({
            "search_criteria": {
                "city": city,
                "min_avg_price": min_avg_price,
                "max_avg_price": max_avg_price
            },
            "neighborhood_count": len(results),
            "neighborhoods": results
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_neighborhoods",
                "description": "Search for neighborhoods based on criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City to search in"
                        },
                        "min_avg_price": {
                            "type": "number",
                            "description": "Minimum average home price"
                        },
                        "max_avg_price": {
                            "type": "number",
                            "description": "Maximum average home price"
                        }
                    },
                    "required": []
                }
            }
        }


class CreateClientNote(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        note_text = kwargs.get('note_text')
        note_type = kwargs.get('note_type', 'general')
        
        if not all([client_id, broker_id, note_text]):
            return json.dumps({
                "error": "client_id, broker_id, and note_text are required"
            }, indent=2)
        
        note = {
            "note_id": 801,
            "client_id": client_id,
            "broker_id": broker_id,
            "note_text": note_text,
            "note_type": note_type,
            "created_at": "2024-08-21T00:00:00Z",
            "status": "active"
        }
        
        return json.dumps({
            "success": True,
            "note_id": 801,
            "message": f"Note created for client {client_id}",
            "note": note
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_client_note",
                "description": "Create a note for a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to create note for"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the note"
                        },
                        "note_text": {
                            "type": "string",
                            "description": "Content of the note"
                        },
                        "note_type": {
                            "type": "string",
                            "description": "Type of note (general, follow_up, concern, etc.)"
                        }
                    },
                    "required": ["client_id", "broker_id", "note_text"]
                }
            }
        }


class GetComparableProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        
        comparables = data.get('comparables', [])
        property_comps = [c for c in comparables if c.get('property_id') == property_id]
        
        return json.dumps({
            "property_id": property_id,
            "comparable_count": len(property_comps),
            "comparables": property_comps
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_comparable_properties",
                "description": "Get comparable properties for a specific property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to get comparables for"
                        }
                    },
                    "required": ["property_id"]
                }
            }
        }


class SchedulePropertyShowing(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        scheduled_time = kwargs.get('scheduled_time')
        duration_minutes = kwargs.get('duration_minutes', 60)
        
        if not all([property_id, client_id, broker_id, scheduled_time]):
            return json.dumps({
                "error": "property_id, client_id, broker_id, and scheduled_time are required"
            }, indent=2)
        
        showing = {
            "showing_id": 901,
            "property_id": property_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "scheduled_time": scheduled_time,
            "duration_minutes": duration_minutes,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "showing_id": 901,
            "message": f"Showing scheduled for property {property_id}",
            "showing": showing
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_property_showing",
                "description": "Schedule a private property showing for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to show"
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the showing"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID conducting the showing"
                        },
                        "scheduled_time": {
                            "type": "string",
                            "description": "Scheduled time in ISO format"
                        },
                        "duration_minutes": {
                            "type": "integer",
                            "description": "Duration of showing in minutes"
                        }
                    },
                    "required": ["property_id", "client_id", "broker_id", "scheduled_time"]
                }
            }
        }
class AddCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get("title")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        return json.dumps({"status": "success", "event_title": title, "start": start_time, "end": end_time}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_calendar_event",
            "description":"Adds a new event to the calendar.",
            "parameters":{"type":"object","properties":{"title": {"type":"string"}, "start_time": {"type":"string"}, "end_time": {"type":"string"}},"required":["title", "start_time", "end_time"]}
        }}

class GetCalendarEvents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        if date:
            return json.dumps({"date": date, "events": [{"title": "Meeting", "time": "10:00 AM"}, {"title": "Lunch", "time": "1:00 PM"}]}, indent=2)
        else:
            return json.dumps({"date": "today", "events": [{"title": "Team Sync", "time": "9:00 AM"}]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_calendar_events",
            "description":"Retrieves calendar events, optionally for a specific date.",
            "parameters":{"type":"object","properties":{"date": {"type":"string", "description": "The date for which to retrieve events (e.g., '2025-08-23')."}},"required":[]}
        }}
class CreateSellerBrokerEmailDrafts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        props = kwargs.get("property_ids") or []
        client_id = kwargs.get("client_id")
        drafts_uri = f"https://storage.example.com/drafts/client_{client_id}_props_{len(props)}.pdf"
        return json.dumps({"client_id": client_id, "property_ids": props, "drafts_uri": drafts_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_seller_broker_email_drafts",
            "description":"Generate a drafts bundle for seller broker emails.",
            "parameters":{"type":"object","properties":{
                "client_id":{"type":"integer"},
                "property_ids":{"type":"array","items":{"type":"string"}}
            },"required":["client_id","property_ids"]}
        }}
class FetchBrokerDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get("broker_id")
        br = next((b for b in data.get("brokers", []) if b.get("broker_id") == broker_id), None)
        if not br:
            return json.dumps({"error": f"Broker {broker_id} not found"}, indent=2)
        return json.dumps(br, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_broker_details",
            "description":"Fetch a broker profile.",
            "parameters":{"type":"object","properties":{"broker_id":{"type":"integer"}},"required":["broker_id"]}
        }}
class FetchBorderingNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        nid = kwargs.get("neighborhood_id")
        n = next((n for n in data.get("neighborhoods", []) if n.get("neighborhood_id") == nid), None)
        if not n:
            return json.dumps({"error": f"Neighborhood {nid} not found"}, indent=2)
        return json.dumps({"neighborhood_id": nid, "bordering": n.get("bordering_ids_json") or []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_bordering_neighborhoods",
            "description":"List bordering neighborhood IDs for a given neighborhood.",
            "parameters":{"type":"object","properties":{"neighborhood_id":{"type":"integer"}},"required":["neighborhood_id"]}
        }}
class FindListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kwargs["neighborhood_ids"] = kwargs.get("neighborhood_ids") or []
        return FindListings.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_listings_in_neighborhoods",
            "description":"Find listings within the provided neighborhoods.",
            "parameters":{
                "type":"object","properties":{
                    "neighborhood_ids":{"type":"array","items":{"type":"integer"}},
                    "price_min":{"type":"integer"},"price_max":{"type":"integer"},
                    "beds":{"type":"integer"},"baths":{"type":"integer"},"limit":{"type":"integer"}
                },"required":["neighborhood_ids"]
            }
        }}

TOOLS = [
    FindListings(),
    FetchListingDetails(),
    FindClients(),
    CalculateMortgage(),
    ScheduleOpenHouse(),
    CreatePropertyReport(),
    CreateCampaign(),
    SendEmail(),
    FetchEmailsForClient(),
    CreateCalendarEvent(),
    GetCalendarEventsForClient(),
    GetCampaignDetails(),
    BuildRoute(),
    GetRouteDetails(),
    PostAuditEvent(),
    CheckDriveTimeConstraints(),
    ListListingsByIds(),
    UpdateListingStatus(),
    GenerateBriefingDoc(),
    AttachDocumentToClient(),
    GetMortgageRates(),
    SearchNeighborhoods(),
    CreateClientNote(),
    GetComparableProperties(),
    SchedulePropertyShowing(),
    AddCalendarEvent(),
    GetCalendarEvents(),
    CreateSellerBrokerEmailDrafts(),
    FetchBrokerDetails(),
    FetchBorderingNeighborhoods(),
    FindListingsInNeighborhoods()
]