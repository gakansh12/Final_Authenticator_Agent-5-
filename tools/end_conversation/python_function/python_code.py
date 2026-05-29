from __future__ import annotations


def end_conversation(reason: str | None = None) -> dict:
	"""End-conversation tool.

	This tool is intentionally minimal: calling agents should treat this as a terminal
	action and stop generating further steps.

	Args:
		reason: Optional string for logging/telemetry.

	Returns:
		A small status payload that can be logged or surfaced by the runtime.
	"""
	payload: dict = {"status": "success", "action": "end_conversation"}
	if reason is not None and str(reason).strip():
		payload["reason"] = str(reason).strip()
	return payload
