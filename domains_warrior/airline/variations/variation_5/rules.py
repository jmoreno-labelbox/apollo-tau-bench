# --- Tripwire Policy Addendum (constants the code can also import) ---
CANONICAL_PRICE_BUCKET = "prices"
REQUIRE_AVAILABLE_APPLIES_TO_WRITES_ONLY = True
ASSIGNMENT_VISIBILITY_REQUIRED = True            
ASSIGNMENT_READBACK_REQUIRED = True              
PRESERVE_REASON_PUNCTUATION = True
TAXES_FEES_UNCHANGED_BY_DEFAULT = True
RESPECT_PREVIEW_CAP = True
IDEMPOTENT_WRITES_REQUIRED = True                
ALLOW_BULK_CABIN_WRITES = True                   
REPEAT_SAFE_RELATIVE_TOOLS_REQUIRED = True       
SEASONAL_MULTIPLIER_AUDIT_DEDUPE = True          
ALLOW_BUCKET_SCOPED_UPGRADE_AUDIT = True         


RULES = [
    # Determinism, scope, and single-turn constraints
    "Given the same inputs and data snapshot, the agent must produce the same sequence of tool calls and outputs (deterministic behavior).",
    "Tasks are single-turn; all parameters passed to tools must come from the prompt or prior tool outputs (no hallucinated literals).",
    "All write tools must be deterministic: no random IDs, no non-deterministic timestamps; any IDs or timestamps must be derived deterministically from inputs or fixed sequences.",
    "Write tools MAY mutate existing objects in-memory (e.g., flights[].dates[].prices) but must NOT introduce new top-level datasets.",
    "Policy takes precedence over any single task instruction. When policy prohibits an action, the agent must refuse via a deterministic error.",
    "Write operations must be idempotent: if a value already equals the requested value, no-op with the same tool return shape.",

    # Date & rounding standards
    "Dates must be ISO 'YYYY-MM-DD'. Unparsable dates rank worst for tie-break and should surface {'error':'invalid_date_format'} when applicable.",
    # --- Output Contract ---
    "Verification outputs must be echoed directly from tool responses in the same run. Do not invent, reformat, or re-compute values.",
    "When a task says 'return no output', the outputs list must be empty.",
    "When a task asks to 'preview N', pass max_preview=N and return exactly those preview rows from the tool; do not synthesize samples.",

    "Monetary rounding & output representation: "
    "- Internal arithmetic and all comparisons MUST round to two decimals using HALF-UP rounding; final selections (min/sort) use these rounded numeric values. "
    "- Validation MUST compare values numerically after applying the same TWO-DECIMAL HALF-UP rounding; DO NOT judge by string formatting. "
    "- Output values MAY be emitted as plain JSON numbers with or without trailing zeros (e.g., 224, 224.2, 224.20, 224.00 are all acceptable if numerically equal). "
    "- Do NOT require fixed two-decimal strings; emit numbers, not strings. "
    "- If an input or intermediate value has more than two fractional digits, round to two decimals for comparison; if it has two or fewer, keep it as-is (no zero-padding required). "
    "Examples (all acceptable representations for the same numeric value): 224.205 → compare as 224.21; outputs such as 224.21, 224.210, 224.2100, or 224.21 (no trailing zeros) are equivalent; 224 → 224, 224.0, 224.00 are equivalent.",

    # Error handling
    "If a prerequisite tool call returns an 'error', the agent must not proceed to dependent calls and must surface that error in the final output.",
    "Standardize common errors: flight_not_found, reservation_not_found, price_not_available_for_date, fare_class_not_found, no_priced_legs, invalid_date_format, unsupported_by_dataset, operating_dates_unavailable.",

    # Operating dates
    "The 'Operating Dates Procedure' must be used when the next operating date is needed: enumerate flights[flight_number].dates keys, filter status=='available', sort ascending by ISO date, and select earliest future date (or earliest overall if no 'current date' context). If 'dates' is missing, return {'error':'operating_dates_unavailable'}.",

    # Reservation vs bucket pricing (fallbacks)
    "Reservation leg prices (reservations[].flights[].price) are authoritative. The agent may only fall back to flights.json buckets if explicitly enabled by the tool flag 'fallback_to_flights=True' OR if the task instruction explicitly authorizes fallback.",
    "Cabin for pricing fallbacks must be taken from reservations[].cabin (lowercased) and must match keys in flights[].dates[day].prices.",
    "When falling back to flights.json, if availability is required by the task or tool flag, verify flights[].dates[day].status=='available'.",

    # Cheapest-leg protocol
    "The 'Cheapest-Leg Protocol' must be executed when a task asks for the cheapest leg within a reservation; it uses get_cheapest_flight_from_reservation(reservation_id, require_available=True, return_all=True).",
    "Tie-breakers: lowest price, then earliest date, then the token 'lexicographic_flight_number' on flight_number.",

    # Staleness & reprice protocols
    "The 'Staleness Check Protocol' uses get_cheapest_flight_from_reservation then get_current_ticket_price on (flight_number, date, fare_class=reservation.cabin). Prices are rounded to 2 decimals; 'stale_price_detected' is True if the rounded values differ.",
    "The 'Itinerary Reprice Recommendation Protocol' compares reservation cheapest vs current buckets across all legs; recommend 'REPRICE' iff current cheapest is strictly cheaper (rounded) or is a different leg with lower rounded price.",

    # Bucket price lookup
    "The 'Bucket Price Lookup Procedure' uses get_current_ticket_price with parameters: flight_number, date (YYYY-MM-DD), fare_class in {'basic_economy','economy','business'}. Enforce: flight exists; date exists and status=='available'; fare_class key exists.",

    # Stats defaults (tokens grounded)
    "Unless otherwise specified, all pricing statistics use price_component 'base_fare'.",
    "The standard outlier filter is method 'iqr' with k=1.5.",
    "Statistics tools may return fields: average_price, median_price, sample_size, consistent with include={'median':True,'count':True}.",

    # Seasonal/discount adjustments (scope + preview + strict revert)
    "Revert operations that undo a previously applied discount MUST specify the target audit_id and set strict=True (unless the task explicitly instructs otherwise). If audit_id is omitted, select the most recent matching audit deterministically (by monotonic id sequence) and still enforce strict=True.",

    # Global tie-break reproducibility
    "When multiple action sequences could succeed, the agent must choose the sequence implied by policy tie-breakers to preserve reproducibility.",

    # --- Cabin write policy (bulk multi-cabin writes allowed) ---
    "Per-cabin or bulk pricing/inventory writes are both allowed: a single call MAY update one or multiple cabins in 'available_seats' and/or 'prices'.",
    "Multi-cabin writes MUST remain idempotent (re-applying the same values yields no change) and MUST update only the explicitly provided cabins (merge semantics).",
    "Published prices and seats live on the dated flight record under 'prices' and 'available_seats' (canonical buckets).",

    # --- Relative tools must be repeat-safe (Problem 4) ---
    "Relative pricing tools (e.g., deltas, multipliers) MUST be repeat-safe: implementations MUST either compute and write an absolute target value before committing (so a re-run sets the same value), OR deduplicate via a deterministic audit key so repeated runs no-op.",
    "Seasonal multiplier operations MUST log a deterministic audit keyed by (flight_number, date, cabin, multiplier). If an identical audit exists, the operation MUST no-op (no_change:true).",
    "When tasks specify relative adjustments, the agent MUST derive a single rounded target via HALF-UP, then perform a canonical 'set' write so results are identical under re-run.",

    # --- No-charge upgrades audit policy (Problem 7) ---
    "All no-charge upgrades MUST log a deterministic audit record that includes: date (ISO YYYY-MM-DD), flight_number, from_cabin, to_cabin, reason, and a monotonic audit id.",
    "Reservation-scoped upgrades MUST also include reservation_id.",
    "Bucket-scoped (inventory) upgrades performed by bulk tools MAY omit reservation_id, but MUST still log the fields above and be idempotent by the tuple (flight_number, date, from_cabin, to_cabin, reason). Duplicate attempts MUST no-op.",

    # --- Assignment visibility & readback (Problem 5) ---
    "When a task’s goal specifies an aircraft assignment, the terminal state MUST include an explicit dated assignment record written via 'assign_aircraft_to_flight'.",
    "A verification readback is REQUIRED and MAY be satisfied by 'get_flight_assignment_by_date' OR any dated-flight read that returns 'flight_number'.",

    # Composite pricing order
    "Composite price adjustments MUST be applied as ordered steps. If both a discount (markdown) and a seasonal multiplier are required, the canonical order is: apply discount first, then seasonal multiplier. Trace and previews MUST reflect both steps.",

    # Availability requirement for writes
    "No price or inventory writes are permitted unless the target flight-date has status=='available'. Exception only if a tool exposes an explicit override flag (e.g., require_available=False) AND the task instruction authorizes it explicitly.",
    
    # Canonical casing & literals
    "Enumerated values (e.g., statuses, cabin names) MUST use canonical lowercase forms as defined in this policy. Free-text literals that the task specifies (e.g., reasons/rationales, route arrows ‘→’, or en dashes ‘–’) MUST be matched exactly, including punctuation and spacing.",

    # --- Status Policy ---
    """
    Status Policy
    ---------------------------
    All statuses must be stored and returned in lowercase canonical form.
    Tasks must use lowercase literals only.

    Canonical enums:

    • Flight statuses:
        {"available", "cancelled", "delayed", "diverted", "landed"}

    • Aircraft statuses:
        {"active", "maintenance", "in maintenance", "stored"}

    • Crew member statuses:
        {"active", "inactive", "on leave"}

    • Operational event statuses/types:
        {"active", "resolved"}

    Rules:
    1. Inputs are case-insensitive, but any mixed-case input is normalized.
    2. Reads always echo the normalized lowercase value.
    3. When filtering by status, compare against the canonical enums.
    4. Tasks/instructions MUST reference only canonical lowercase values.
    """,

    # --- Assistant-visible clarifications -----
    "Published prices live in flights[].dates[day].prices (canonical). 'set_ticket_price' MUST flow into the canonical 'prices' bucket (shim allowed) and return a verified snapshot.",
    "The require_available flag applies ONLY to pricing WRITE operations. READ tools (e.g., get_current_ticket_price) do not accept unknown params and must reject them.",
    "Aircraft assignment must be performed via assign_aircraft_to_flight and be visible on the dated flight instance; editing schedule.aircraft is not equivalent for audit/visibility purposes.",
    "Exact punctuation in reasons/rationales must be preserved (e.g., en dash vs hyphen).",
    "Unless stated otherwise, taxes/fees are unchanged; base_fare only.",
    "Preview caps (max_preview) must be honored exactly when provided.",
    "All writes must be idempotent; if values already match, tools must no-op with the same return shape.",

    # --- Canonical writer & verification ---
    "update_flight_inventory_and_prices is the canonical path for dated-flight prices and available_seats; it may accept multiple cabins per call.",
    "A successful canonical writer response that includes an 'after' or equivalent per-date snapshot is the source of truth for judging state.",

    # --- Availability handling ---
    "Price/seat writes require status=='available'. It is compliant to (a) set status='available' in the same call, or (b) set/confirm availability in a prior action in the same task run.",

    # --- Legacy writer shim ---
    "'set_ticket_price' writes MUST flow into the canonical 'prices' bucket on the dated flight and return a verified snapshot.",
]