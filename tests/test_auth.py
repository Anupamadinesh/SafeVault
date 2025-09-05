from auth import authenticate_user, authorize_user

def test_auth():
    token = authenticate_user("admin", "admin123")
    assert token is not None
    assert authorize_user(token, "admin") == True
    assert authorize_user(token, "user") == False

def test_invalid_auth():
    token = authenticate_user("admin", "wrongpass")
    assert token is None
