import re

def validate_and_route_card_number(card_number: str) -> dict:
    """
    Validates card number and determines next step.

    Returns:
        {
            "status": "success | error",
            "next_step": "COLLECT_EXPIRY",
            "error_type": "invalid_length | invalid_number | unsupported",
            "card_type": "visa/mastercard/amex/discover",
            "card_last_4": "1234"
        }
    """

    try:
        if not card_number:
            return {
                "status": "error",
                "next_step": None,
                "error_type": "invalid_number",
                "message": "Card number is required"
            }

        # Clean input
        card_digits = re.sub(r'[^0-9]', '', str(card_number))

        # ✅ Length validation
        if len(card_digits) < 13 or len(card_digits) > 19:
            return {
                "status": "error",
                "next_step": None,
                "error_type": "invalid_length",
                "message": "Invalid card length"
            }

        # ✅ Luhn check
        def luhn_check(num):
            total = 0
            reverse_digits = num[::-1]

            for i, digit in enumerate(reverse_digits):
                n = int(digit)
                if i % 2 == 1:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n

            return total % 10 == 0

        if not luhn_check(card_digits):
            return {
                "status": "error",
                "next_step": None,
                "error_type": "invalid_number",
                "message": "Failed Luhn validation"
            }

        # ✅ Card type detection
        if card_digits.startswith('4'):
            card_type = "visa"
        elif card_digits.startswith('5'):
            card_type = "mastercard"
        elif card_digits.startswith('3'):
            card_type = "amex"
        elif card_digits.startswith('6'):
            card_type = "discover"
        else:
            return {
                "status": "error",
                "next_step": None,
                "error_type": "unsupported",
                "message": "Unsupported card type"
            }

        # ✅ SUCCESS
        return {
            "status": "success",
            "next_step": "COLLECT_EXPIRY",
            "card_type": card_type,
            "card_last_4": card_digits[-4:],
            "error_type": None,
            "message": None
        }

    except Exception as e:
        return {
            "status": "error",
            "next_step": None,
            "error_type": "system_error",
            "message": f"Validation failed: {str(e)}"
        }