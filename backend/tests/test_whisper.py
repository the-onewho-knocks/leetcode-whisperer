from app.patterns.correctors import correct_pattern


def test_palindrome_correction():
    problem = "Check if a string is a palindrome"
    assert correct_pattern(problem, "sliding_window") == "two_pointers"