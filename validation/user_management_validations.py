def validate_sign_up(data):
    required_fields = ["username", "password", "email", "user_type"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None
