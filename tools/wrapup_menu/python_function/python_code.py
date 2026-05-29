from typing import Optional


_MENU = [
	{"id": "check_balance", "label": "Check balance"},
	{"id": "payment_history", "label": "Check payment history"},
	{"id": "add_payment_method", "label": "Add payment method"},
	{"id": "update_payment_method", "label": "Update payment method"},
	{"id": "all_set", "label": "All set"},
]


def _normalize(text: str) -> str:
	return " ".join(text.strip().lower().split())


def _map_selection_to_intent(selection: str) -> Optional[str]:
	s = _normalize(selection)

	# Exact IDs
	valid_ids = {opt["id"] for opt in _MENU}
	if s in valid_ids:
		return s

	# Common spoken variants
	if s in {"1", "check balance", "balance", "hear balance", "play balance"}:
		return "check_balance"
	if s in {"2", "payment history", "history", "check payment history", "past payments"}:
		return "payment_history"
	if s in {"3", "add payment", "add payment method", "add card", "add bank", "add"}:
		return "add_payment_method"
	if s in {"4", "update payment", "update payment method", "change card", "replace card", "update"}:
		return "update_payment_method"
	if s in {"5", "all set", "done", "nothing else", "exit", "quit"}:
		return "all_set"

	return None


def wrapup_menu(selection: str) -> dict:
	"""Wrap-up menu tool.

	Runtime expectation: the agent prints the menu to the user, collects a user reply,
	then calls this tool with `selection` set to that reply.

	Returns:
	  - status: "needs_input" when selection missing/invalid, else "success"
	  - next_intent: one of the menu ids
	  - menu_options: the canonical menu (always included for consistency)
	"""
	if selection is None or not str(selection).strip():
		return {
			"status": "needs_input",
			"menu_options": _MENU,
			"error": "missing_selection",
		}

	mapped = _map_selection_to_intent(str(selection))
	if mapped is None:
		return {
			"status": "needs_input",
			"menu_options": _MENU,
			"error": "invalid_selection",
		}

	return {
		"status": "success",
		"next_intent": mapped,
		"menu_options": _MENU,
	}
