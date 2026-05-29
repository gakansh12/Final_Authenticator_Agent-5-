import json
from datetime import datetime

def add_payment_interaction_handler(sub_step_scope: str, verbiage_variant: str, interaction_type: str) -> dict:
    """
    Handles payment collection interaction errors and returns recovery prompts.
    
    Args:
        sub_step_scope: e.g., "routing_number_collection", "card_number_collection"
        verbiage_variant: e.g., "routing_number", "card_number_hold_on", "unsupported"
        interaction_type: "NO_INPUT", "INVALID", "NO_MATCH"
    
    Returns:
        Recovery prompt and counter
    """
    
    recovery_prompts = {
        "routing_number_collection": {
            "routing_number": "Say or enter your 9 digit bank routing number. Or if you need a moment, say 'hold on'.",
            "routing_number_hold_on": "Whenever you're ready, say or enter your 9 digit bank routing number.",
            "routing_number_validation_fail": "That didn't seem right. Please say or enter a valid 9 digit routing number."
        },
        "account_number_collection": {
            "account_number": "Say or enter your bank account number."
        },
        "card_number_collection": {
            "card_number": "Say or enter your card number. Or if you need a moment, say 'hold on'.",
            "card_number_hold_on": "Let's get your card details. Say or enter your card number.",
            "unsupported": "Unfortunately, we don't support that card type. Please use a Visa, Mastercard, American Express, or Discover card.",
            "invalid_length": "That didn't seem right. Please check your card number and try again."
        },
        "expiration_date_collection": {
            "expiration_date": "Say the expiration date, like January 26 or type zero one, two six."
        },
        "payment_method_selection": {
            "ask_payment_method": "Got it. Do you want to add a new card or bank account to make this payment?"
        }
    }
    
    prompt = recovery_prompts.get(sub_step_scope, {}).get(verbiage_variant, "Let's try that again.")
    
    return {
        "prompt": prompt,
        "recovery_counter": 1,
        "interaction_type": interaction_type,
        "sub_step_scope": sub_step_scope,
        "timestamp": datetime.now().isoformat()
    }
