import hashlib

def call_generate_dv_token(account_id: str, card_number: str, card_expiry: str) -> dict:
    """
    Generates DV token for card.

    Returns:
        {
            "status": "success | error",
            "dv_token": "...",
            "card_last_4": "...",
            "next_step": "SUBMIT_PAYMENT",
            "error_type": None
        }
    """

    try:
        if not account_id or not card_number or not card_expiry:
            return {
                "status": "error",
                "dv_token": None,
                "card_last_4": None,
                "next_step": None,
                "error_type": "missing_input",
                "message": "Required fields missing"
            }

        # ✅ Generate token (stub)
        token_input = f"{account_id}_{card_number[-4:]}_{card_expiry}"
        dv_token = hashlib.sha256(token_input.encode()).hexdigest()[:32]

        return {
            "status": "success",
            "dv_token": dv_token,
            "card_last_4": card_number[-4:],
            "next_step": "SUBMIT_PAYMENT",
            "error_type": None,
            "message": None
        }

    except Exception as e:
        return {
            "status": "error",
            "dv_token": None,
            "card_last_4": None,
            "next_step": None,
            "error_type": "system_error",
            "message": f"Failed to generate DV token: {str(e)}"
        }