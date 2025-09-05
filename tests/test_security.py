from security import sanitize_input

def test_sanitize_input():
    assert sanitize_input("normal") == "normal"
    assert sanitize_input("DROP TABLE;") == "DROP TABLE"
    assert sanitize_input("<script>") == "&lt;script&gt;"
    assert sanitize_input(123) == ""
