WIKI = """
"The agent is required to generate an identical sequence of tool calls and outputs when provided with the same inputs and data snapshot, ensuring deterministic behavior.",
    "Each task is single-turn; every parameter supplied to tools must originate from the prompt or from outputs of previous tools, with no fabricated literals permitted.",
    "All write tools are to function deterministically: random IDs and non-deterministic timestamps are not allowed; any IDs or timestamps must be deterministically derived from the inputs or from predefined sequences.",
    "Write tools MAY modify existing objects in-memory (such as flights[
"""
