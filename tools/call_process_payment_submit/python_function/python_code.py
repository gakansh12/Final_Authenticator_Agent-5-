from datetime import datetime
from typing import Optional

def call_process_payment_submit(
    account_id: str,
    selected_payment_method: str,
    dv_token: str,
    routing_number: str,
    account_number: str
) -> dict:
    """
    Submits payment method.

    Returns:
        {
            "status": "success | error",
            "returnCode": 0 | 1,
            "next_step": "WRAP_UP",
            "error_type": None,
            "message": None
        }
    """

    try:
        # ✅ Validate account
        if not account_id:
            return {
                "status": "error",
                "returnCode": 1,
                "next_step": None,
                "error_type": "missing_account_id",
                "message": "Account ID is required"
            }

        # ✅ Validate CC flow
        if selected_payment_method == "CC":
            if not dv_token:
                return {
                    "status": "error",
                    "returnCode": 1,
                    "next_step": None,
                    "error_type": "missing_dv_token",
                    "message": "DV token missing"
                }

        # ✅ Validate ACH flow
        elif selected_payment_method == "ACH":
            if not routing_number or not account_number:
                return {
                    "status": "error",
                    "returnCode": 1,
                    "next_step": None,
                    "error_type": "missing_bank_details",
                    "message": "Routing or account number missing"
                }

        else:
            return {
                "status": "error",
                "returnCode": 1,
                "next_step": None,
                "error_type": "invalid_payment_type",
                "message": "Invalid payment method"
            }

        # ✅ Simulate success
        return {
            "status": "success",
            "returnCode": 0,
            "next_step": "WRAP_UP",
            "payment_method": selected_payment_method,
            "account_id": account_id,
            "timestamp": datetime.now().isoformat(),
            "error_type": None,
            "message": None
        }

    except Exception as e:
        return {
            "status": "error",
            "returnCode": 1,
            "next_step": None,
            "error_type": "system_error",
            "message": f"Submission failed: {str(e)}"
        }