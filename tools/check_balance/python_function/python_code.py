def check_balance(account_id: str, platform_cd: str) -> dict:
    """
    Fetches current balance for a member.
    """

    try:
        if not account_id:
            return {
                "status": "error",
                "balance": None,
                "currency": None,
                "balance_announcement": None,
                "error": "Account ID is required"
            }

        # Mock logic (replace later with API)
        balance_amount = 325.75
        currency = "USD"

        if platform_cd == "CB":
            announcement = (
                f"Your current balance is {balance_amount} dollars. "
                "You can also view details on humana one members dot com."
            )
        else:
            announcement = f"Your current balance is {balance_amount} dollars."

        return {
            "status": "success",
            "balance": balance_amount,
            "currency": currency,
            "balance_announcement": announcement,
            "platform_cd": platform_cd,
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "balance": None,
            "currency": None,
            "balance_announcement": None,
            "error": f"Failed to fetch balance: {str(e)}"
        }