# --- Tripwire Policy Addendum (constants the code can also import) ---
CANONICAL_PRICE_BUCKET = "prices"
REQUIRE_AVAILABLE_APPLIES_TO_WRITES_ONLY = True
ASSIGNMENT_VISIBILITY_REQUIRED = True
PRESERVE_REASON_PUNCTUATION = True
TAXES_FEES_UNCHANGED_BY_DEFAULT = True
RESPECT_PREVIEW_CAP = True
IDEMPOTENT_WRITES_REQUIRED = True


RULES = [
    "The agent is required to generate an identical sequence of tool calls and outputs when provided with the same inputs and data snapshot, ensuring deterministic behavior.",
    "Each task is single-turn; every parameter supplied to tools must originate from the prompt or from outputs of previous tools, with no fabricated literals permitted.",
    "All write tools are to function deterministically: random IDs and non-deterministic timestamps are not allowed; any IDs or timestamps must be deterministically derived from the inputs or from predefined sequences.",
    "Write tools MAY modify existing objects in-memory (such as flights[].dates[].prices), but they must NOT create new top-level datasets.",
    "Policy overrides any individual task instruction. If policy forbids an action, the agent is required to reject it with a deterministic error.",
    "Write operations are required to be idempotent: when a value already matches the requested value, perform a no-op while returning the same tool response structure.",
    "Dates are required to follow the ISO 'YYYY-MM-DD' format. If a date cannot be parsed, it should be ranked lowest for tie-breaking purposes and must return {'error':'invalid_date_format'} when relevant.",
    "Monetary values must be rounded to two decimal places using HALF-UP rounding for all internal calculations and comparisons, including final selection processes such as min or sort, which must utilize these rounded numbers. Output values can be provided as standard JSON numbers, and trailing zeros should not be appended. Do not convert values to fixed two-decimal-place strings. When an input or intermediate value contains more than two digits after the decimal, round it to two decimals; if it has two or fewer, retain the value unchanged without adding zeros. For example: 224.205 becomes 224.21; 224.2 remains 224.2; 224 remains 224.",
    "If a required tool invocation yields an 'error', the agent must halt any subsequent dependent calls and include that error in the final output.",
    "Normalize frequent errors as follows: flight_not_found, reservation_not_found, price_not_available_for_date, fare_class_not_found, no_priced_legs, invalid_date_format, unsupported_by_dataset, operating_dates_unavailable.",
    "When possible, outputs are required to specify the price source for each leg (either 'reservation' or 'flights_json') to facilitate audit trails in price comparison tasks.",
    "The 'Operating Dates Procedure' must be applied whenever the next operating date is required: list all keys in flights[flight_number].dates, filter for entries where status=='available', sort these by ISO date in ascending order, and choose the earliest date in the future (or the earliest date overall if there is no 'current date' context). If the 'dates' field is absent, return {'error':'operating_dates_unavailable'}.",
    "The definitive source for reservation leg prices is reservations[].flights[].price. The agent is permitted to use flights.json buckets only if the tool flag 'fallback_to_flights=True' is set or if the task instruction specifically permits fallback.",
    "For pricing fallbacks, the cabin must be sourced from reservations[].cabin (in lowercase) and must correspond to a key present in flights[].dates[day].prices.",
    "When utilizing flights.json as a fallback, if the task or tool flag requires availability, confirm that flights[].dates[day].status is equal to 'available'.",
    "Execute the 'Cheapest-Leg Protocol' whenever a task requests the cheapest leg within a reservation; this protocol invokes get_cheapest_flight_from_reservation(reservation_id, require_available=True, return_all=True).",
    "For tie-breaking, prioritize by lowest price first, followed by earliest date, and then by the token 'lexicographic_flight_number' applied to flight_number.",
    "The 'Staleness Check Protocol' first calls get_cheapest_flight_from_reservation, then invokes get_current_ticket_price with (flight_number, date, fare_class=reservation.cabin). Both prices are rounded to two decimal places; 'stale_price_detected' is set to True if the rounded prices are not equal.",
    "The 'Itinerary Reprice Recommendation Protocol' evaluates the reservation's cheapest and current buckets for every leg; a 'REPRICE' is recommended only if the current cheapest (after rounding) is strictly less expensive, or if a different leg presents a lower rounded price.",
    "The 'Bucket Price Lookup Procedure' invokes get_current_ticket_price with the following parameters: flight_number, date (formatted as YYYY-MM-DD), and fare_class from the set {'basic_economy','economy','business'}. The procedure requires that the flight exists, the date exists with status equal to 'available', and that the fare_class key is present.",
    "Unless explicitly indicated otherwise, all pricing statistics utilize the price_component 'base_fare'.",
    "The default outlier filter utilizes the 'iqr' method with k set to 1.5.",
    "Statistics tools can output the fields: average_price, median_price, and sample_size, provided that include={'median':True,'count':True} is specified.",
    "Revert operations intended to reverse a previously applied discount MUST indicate the target audit_id and assign strict=True, except when the task specifically states otherwise. If audit_id is not provided, deterministically choose the most recent matching audit based on monotonic id order, and strict=True must still be applied.",
    "If several action sequences are viable, the agent is required to select the sequence determined by policy tie-breakers to ensure reproducibility.",
    "Each per-cabin pricing write operation MUST affect only a single cabin. Any bulk updates involving multiple cabins MUST be performed as individual writes, with one cabin per operation.",
    "Every no-charge upgrade MUST generate an audit record containing: reservation_id (string), date (ISO YYYY-MM-DD), flight_number, from_cabin, to_cabin, and reason. Any state transition that constitutes a no-charge upgrade without this audit record is considered invalid.",
    "If a task’s goal includes an aircraft assignment, the terminal state MUST contain a clear assignment record for that specific flight-date (idempotent), and verification MUST retrieve and confirm this record.",
    "Composite price adjustments MUST be executed in the specified sequence. When both a discount (markdown) and a seasonal multiplier are involved, the required order is: discount applied first, followed by the seasonal multiplier. Both steps MUST be represented in trace logs and previews.",
    "Price or inventory modifications are NOT allowed unless the status of the target flight-date is 'available'. The only exception is when a tool provides an explicit override flag (such as require_available=False) and the task instruction grants authorization.",
    "Enumerated values (such as statuses or cabin names) MUST appear in their canonical lowercase forms as specified in this policy. Any free-text literals required by the task (including reasons/rationales, route arrows ‘→’, or en dashes ‘–’) MUST be reproduced exactly, preserving all punctuation and spacing.",
    "Status Policy --------------------------- All status values are required to be saved and returned using their canonical lowercase representation. Tools MUST apply norm_status() to normalize any input status string and check it against the appropriate enum before writing. Tasks MUST utilize only lowercase literals. Canonical enums: • Flight statuses: {\"available\", \"cancelled\", \"delayed\", \"diverted\", \"landed\"} • Aircraft statuses: {\"active\", \"maintenance\", \"in maintenance\", \"stored\"} • Crew member statuses: {\"active\", \"inactive\", \"on leave\"} • Operational event statuses/types: {\"active\", \"resolved\"} Rules:",
    "Inputs are not case-sensitive, and any input with mixed case is normalized.",
    "The require_available flag is relevant EXCLUSIVELY to pricing WRITE actions (such as set_ticket_price). READ utilities (like get_current_ticket_price) cannot process unknown params and are required to reject them.",
    "Aircraft assignment should be executed through assign_aircraft_to_flight and reflected on the specific dated flight instance; modifying schedule.aircraft does not serve the same audit function.",
    "The precise punctuation used in reasons or rationales must remain intact (for instance, distinguishing between an en dash and a hyphen).",
    "Unless explicitly specified, taxes/fees remain the same; only base_fare is affected.",
    "When max_preview is specified, preview caps must be enforced precisely as given.",
    "Every write operation must be idempotent; if the current values are already correct, tools must perform a no-op and return an identical response structure.",
]
