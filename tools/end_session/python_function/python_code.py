def end_session(req: dict | None = None) -> dict:
    """Signal that the conversation should end.

    The surrounding runtime is responsible for actually terminating audio/telephony.
    """

    return {"status": "success", "ended": True}
