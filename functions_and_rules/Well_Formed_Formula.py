def is_well_formed(
    formula: str,
) -> bool:  # FIXME This function needs to convert logical symbols into a natural language expression, and then capitalize all letters.
    """
    Check if a propositional formula is well-formed.

    A propositional formula is well-formed if it satisfies the following conditions:
    1. It is a non-empty string.
    2. It starts with a letter or an opening parenthesis.
    3. It ends with a letter, a digit, or a closing parenthesis.
    4. It only contains letters, digits, and parentheses.
    5. It has balanced parentheses.

    Parameters:
    formula (str): The propositional formula to check.

    Returns:
    bool: True if the formula is well-formed, False otherwise.

    Raises:
    Exception: If the formula is not well-formed.
    """

    # Check if the formula starts with two capital letters next to each other
    if len(formula) >= 2 and formula[0].isupper() and formula[1].isupper():
        raise Exception(
            "The formula starts with two capital letters next to each other"
        )

    # Define the valid characters
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()"
    # Define the valid starting characters
    valid_starts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ("
    # Define the valid ending characters
    valid_ends = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Check if the string is empty
    if len(formula) == 0:
        raise Exception("The formula is empty")

    # Check if the first character is valid
    if formula[0] not in valid_starts:
        raise Exception("The formula starts with an invalid character")

    # Check if the last character is valid
    if formula[-1] not in valid_ends:
        raise Exception("The formula ends with an invalid character")

    # Check if all the characters in the string are valid
    for c in formula:
        if c not in valid_chars:
            raise Exception("The formula contains an invalid character")

    # Check if the parentheses are balanced
    paren_count = 0
    for c in formula:
        if c == "(":
            paren_count += 1
        elif c == ")":
            paren_count -= 1
        if paren_count < 0:
            raise Exception("The formula has unbalanced parentheses")
    if paren_count != 0:
        raise Exception("The formula has unbalanced parentheses")

    # If all checks pass, the formula is well-formed
    return True


def test_is_well_formed():
    # Test for empty formula
    try:
        is_well_formed("")
    except Exception as e:
        assert str(e) == "The formula is empty", f"Unexpected exception: {e}"
    else:
        assert False, "Exception not raised for empty formula"

    # Test for formula starting with invalid character
    try:
        is_well_formed("1A")
    except Exception as e:
        assert (
            str(e) == "The formula starts with an invalid character"
        ), f"Unexpected exception: {e}"
    else:
        assert False, "Exception not raised for formula starting with invalid character"

    # Test for formula ending with invalid character
    try:
        is_well_formed("A1+")
    except Exception as e:
        assert (
            str(e) == "The formula ends with an invalid character"
        ), f"Unexpected exception: {e}"
    else:
        assert False, "Exception not raised for formula ending with invalid character"

    # Test for formula with invalid characters
    try:
        is_well_formed("A1+B")
    except Exception as e:
        assert (
            str(e) == "The formula contains an invalid character"
        ), f"Unexpected exception: {e}"
    else:
        assert False, "Exception not raised for formula with invalid characters"

    # Test for unbalanced parentheses
    try:
        is_well_formed("A(B")
    except Exception as e:
        assert (
            str(e) == "The formula has unbalanced parentheses"
        ), f"Unexpected exception: {e}"
    else:
        assert False, "Exception not raised for unbalanced parentheses"

    # Test for formula starting with two capital letters next to each other
    try:
        is_well_formed("AB")
    except Exception as e:
        assert (
            str(e) == "The formula starts with two capital letters next to each other"
        ), f"Unexpected exception: {e}"
    else:
        assert (
            False
        ), "Exception not raised for formula starting with two capital letters next to each other"


if __name__ == "__main__":
    # This function should say "All tests passed!" if all tests pass
    test_is_well_formed()
    print("All tests passed!")
