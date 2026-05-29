from datetime import datetime

def call_payment_history_details(account_id: str, platform_cd: str) -> dict:
    """
    Fetches payment history for a member.
    
    Args:
        account_id: Member account ID
        platform_cd: Platform code ("CB" for CBIS, "LV" or "EM" for Non-CBIS)
    
    Returns:
        Payment history announcement and details
    """
    
    # Stub implementation - replace with actual API call
    
    try:
        if not account_id:
            return {
                "status": "error",
                "number_of_payments_returned": 0,
                "error": "Account ID is required"
            }
        
        # Simulate payment history for demonstration
        if platform_cd == "CB":
            # CBIS member - they view on website
            announcement = "To view your past payments, please visit our website at humana one members dot com."
        else:
            # Non-CBIS member - provide recent payments
            announcement = "Your recent payments are: May 15th, Two hundred dollars. April 10th, Two hundred dollars. March 5th, Two hundred dollars."
        
        return {
            "status": "success",
            "payment_announcement": announcement,
            "number_of_payments_returned": 3,
            "payments": [
                {"date": "2026-05-15", "amount": 200},
                {"date": "2026-04-10", "amount": 200},
                {"date": "2026-03-05", "amount": 200}
            ],
            "platform_cd": platform_cd,
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "number_of_payments_returned": 0,
            "error": f"Failed to fetch payment history: {str(e)}"
        }
