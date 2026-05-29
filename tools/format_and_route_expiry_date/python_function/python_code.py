import re
from datetime import datetime

def format_and_route_expiry_date(expiry_input: str) -> dict:
    """
    Parses and validates expiry date.

    Returns:
        {
            "status": "success | error",
            "card_expiry": "MM/YY",
            "next_step": "SUBMIT_PAYMENT",
            "error_type": "invalid_format | expired",
            "message": None
        }
    """

    try:
        if not expiry_input:
            return {
                "status": "error",
                "card_expiry": None,
                "next_step": None,
                "error_type": "invalid_format",
                "message": "Expiry date is required"
            }

        # ✅ Normalize input (remove spaces for cases like "01 28")
        expiry_input = expiry_input.replace(" ", "")

        # ✅ Extract numbers
        numbers = re.findall(r'\d+', expiry_input)

        # ✅ Case 1: MMYY format like "0630"
        if len(numbers) == 1 and len(numbers[0]) == 4:
            month = int(numbers[0][:2])
            year = int(numbers[0][2:])

        # ✅ Case 2: MM YY or M YY (e.g., "06 30", "6 30")
        elif len(numbers) >= 2:
            month = int(numbers[0])
            year = int(numbers[1])

        # ❌ Invalid format
        else:
            return {
                "status": "error",
                "card_expiry": None,
                "next_step": None,
                "error_type": "invalid_format",
                "message": "Invalid format"
            }

        # ✅ Validate month
        if month < 1 or month > 12:
            return {
                "status": "error",
                "card_expiry": None,
                "next_step": None,
                "error_type": "invalid_format",
                "message": "Invalid month"
            }

        # ✅ Normalize year
        if year < 100:
            year = 2000 + year

        # ✅ Expiry validation (end of month logic)
        current_date = datetime.now()

        if month == 12:
            expiry_date = datetime(year + 1, 1, 1)
        else:
            expiry_date = datetime(year, month + 1, 1)

        if expiry_date <= current_date:
            return {
                "status": "error",
                "card_expiry": None,
                "next_step": None,
                "error_type": "expired",
                "message": "Card expired"
            }

        # ✅ Format MM/YY
        formatted = f"{month:02d}/{year % 100:02d}"

        return {
            "status": "success",
            "card_expiry": formatted,
            "next_step": "SUBMIT_PAYMENT",
            "error_type": None,
            "message": None
        }

    except Exception as e:
        return {
            "status": "error",
            "card_expiry": None,
            "next_step": None,
            "error_type": "system_error",
            "message": f"Failed to parse expiry: {str(e)}"
        }