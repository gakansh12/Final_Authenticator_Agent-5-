def verify_caller_dob(account_id: str, date_of_birth: str) -> dict:
    """
    Verifies a caller's identity using their account ID and date of birth.
    
    Args:
        account_id: The caller's account ID
        date_of_birth: The caller's date of birth in DD/MM/YYYY format
    
    Returns:
        A dict with verified (bool) and caller_name (str)
    """

    # ------------------------------------
    # Replace this mock data with your
    # actual data source or logic later
    # ------------------------------------

    CUSTOMER_RECORDS = {
        "ACC001": {"dob": "15/08/1990", "name": "Alice Smith"},
        "ACC002": {"dob": "22/03/1985", "name": "Bob Johnson"},
        "ACC003": {"dob": "07/11/1992", "name": "Carol White"},
    }

    record = CUSTOMER_RECORDS.get(account_id.upper().strip())

    if record and record["dob"] == date_of_birth.strip():
        return {"verified": True, "caller_name": record["name"]}
    
    return {"verified": False, "caller_name": ""}
    