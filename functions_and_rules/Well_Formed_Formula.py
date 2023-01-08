from Logical_Symbols_and_Semantics import Logical_Symbols
from typing import List
import re


def choose_set_of_symbols(index):
    """
    Choose a set of symbols to represent logical operators.

    Parameters:
    index (int): The index of the symbol to be chosen from the Logical_Symbols dictionary.

    Returns:
    list: A list of chosen symbols.

    Logical_Symbols:
    A dictionary containing various logical symbols used in logic and mathematics, such as symbols for:
        - Negation: represents the logical operation of negation, which is the reversal of the truth value of a proposition
        - Conjunction: represents the logical operation of conjunction, which is the combination of two propositions in such a way that the resulting proposition is only true if both of the original propositions are true
        - Inclusive disjunction: represents the logical operation of inclusive disjunction, which is the combination of two propositions in such a way that the resulting proposition is true if either of the original propositions are true (or if both are true)
        - Material conditional: represents the logical operation of material conditional, which is a type of conditional statement in logic that is only considered true if the antecedent is false or the consequent is true
        - Material biconditional: represents the logical operation of material biconditional, which is a type of conditional statement in logic that is only considered true if the antecedent and consequent are both true or both false
    """
    # Create an empty list to store the chosen symbols
    chosen_symbols = []
    # Iterate over the items in the Logical_Symbols dictionary
    for _, symbols in Logical_Symbols.items():
        # If the index is within the range of the symbols list, append the symbol at the given index to the chosen_symbols list
        # Otherwise, append an empty string to the chosen_symbols list
        if index < len(symbols):
            chosen_symbols.append(symbols[index])
        else:
            chosen_symbols.append("")

    if index > 0:
        # replace the empty string with the symbol at index 2
        chosen_symbols[2] = Logical_Symbols["Inclusive_Disjunction"][0]
    # Return the list of chosen symbols
    return chosen_symbols


def choose_set_of_symbols(index):
    """
    Choose a set of symbols to represent logical operators.

    Parameters:
    index (int): The index of the symbol to be chosen from the Logical_Symbols dictionary.

    Returns:
    list: A list of chosen symbols.

    Logical_Symbols:
    A dictionary containing various logical symbols used in logic and mathematics, such as symbols for:
        - Negation: represents the logical operation of negation, which is the reversal of the truth value of a proposition
        - Conjunction: represents the logical operation of conjunction, which is the combination of two propositions in such a way that the resulting proposition is only true if both of the original propositions are true
        - Inclusive disjunction: represents the logical operation of inclusive disjunction, which is the combination of two propositions in such a way that the resulting proposition is true if either of the original propositions are true (or if both are true)
        - Material conditional: represents the logical operation of material conditional, which is a type of conditional statement in logic that is only considered true if the antecedent is false or the consequent is true
        - Material biconditional: represents the logical operation of material biconditional, which is a type of conditional statement in logic that is only considered true if the antecedent and consequent are both true or both false
    """
    # Create an empty list to store the chosen symbols
    chosen_symbols = []
    # Iterate over the items in the Logical_Symbols dictionary
    for _, symbols in Logical_Symbols.items():
        # If the index is within the range of the symbols list, append the symbol at the given index to the chosen_symbols list
        # Otherwise, append an empty string to the chosen_symbols list
        if index < len(symbols):
            chosen_symbols.append(symbols[index])
        else:
            chosen_symbols.append("")

    if index > 0:
        # replace the empty string with the symbol at index 2
        chosen_symbols[2] = Logical_Symbols["Inclusive_Disjunction"][0]
    # Return the list of chosen symbols
    return chosen_symbols


def translate_expression(expression: str, chosen_symbol: List[str]) -> str:
    """
    Translates a logical expression in natural language to a logical expression in
    symbolic notation.

    Parameters:
    expression (str): The logical expression in natural language to be translated.

    Returns:
    str: The logical expression in symbolic notation.

    Examples:
    >>> translate_expression("p and q")
    "P & Q"
    >>> translate_expression("p or q")
    "P ∨ Q"
    >>> translate_expression("not-p")
    "~P"
    >>> translate_expression("if p then q")
    "P → Q"
    >>> translate_expression("p iff q")
    "P ↔ Q"
    """

    # Replace the logical operators in the expression with the chosen symbols
    replacements = [
        ("and", chosen_symbol[1]),
        ("or", chosen_symbol[2]),
        ("not-", chosen_symbol[0]),
        ("if ", ""),
        ("then", chosen_symbol[3]),
        ("iff", chosen_symbol[4]),
    ]
    for old, new in replacements:
        expression = expression.replace(old, new)
    # Make every atomic alphabetical character capitalized
    expression = "".join(
        [c.upper() if c.isalpha() and len(c) == 1 else c for c in expression]
    )

    return expression


def convert_formula(
    formula: str,
) -> str:  # FIXME: This function does not swap the antecedent with the consequent in a conditional statement.
    """
    Convert a propositional logic formula to natural language.

    Parameters:
    formula (str): The propositional logic formula to convert.

    Returns:
    str: The natural language equivalent of the formula.

    Examples:
    >>> convert_formula("(¬p ∧ q) ∨ (p ∧ ¬q)")
    "(NOT P AND Q) OR (P AND NOT Q)"
    >>> convert_formula("(p → q) ∧ (q → r) ∧ (r → p)")
    "(Q IF P) AND (R IF Q) AND (P IF R)"
    """
    # Replace logical connectives with natural language equivalents
    for key in Logical_Symbols:
        for symbol in Logical_Symbols[key]:
            formula = formula.replace(symbol, convert_connective(key))
    # Find all atomic propositions (lowercase letters)
    atomic_props = re.findall(r"[a-z]", formula)
    # Capitalize atomic propositions
    for prop in atomic_props:
        formula = formula.replace(prop, prop.upper())
    # Swap position of "if" and atomic proposition
    formula = re.sub(r"if (.)", r"\1 if", formula)

    return formula.replace("--", "-")


def convert_connective(connective: str) -> str:
    """
    Convert a logical connective to its natural language equivalent.

    Parameters:
    connective (str): The logical connective to convert.

    Returns:
    str: The natural language equivalent of the connective.

    Examples:
    >>> convert_connective("Negation")
    "not"
    >>> convert_connective("Conjunction")
    "and"
    >>> convert_connective("Inclusive_Disjunction")
    "or"
    """
    if connective == "Negation":
        return "not-"
    elif connective == "Conjunction":
        return "and"
    elif connective == "Inclusive_Disjunction":
        return "or"
    elif connective == "Material_Conditional":
        return "if"
    else:
        return connective


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

    formula = convert_formula(formula)

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


def test_translate_expression():
    # Test the translate_expression function with each symbol in the Logical_Symbols dictionary
    for i in range(3):
        chosen_symbols = choose_set_of_symbols(i)
        print(f"Testing with symbols {chosen_symbols}")
        print(translate_expression("p and q", chosen_symbols))
        print(translate_expression("p or q", chosen_symbols))
        print(translate_expression("not-p", chosen_symbols))
        print(translate_expression("if p then q", chosen_symbols))
        print(translate_expression("p iff q", chosen_symbols))


if __name__ == "__main__":
    # This function should say "All tests passed!" if all tests pass
    test_is_well_formed()
    print("All tests passed!")
    print(convert_formula("(p → q) ∧ (q → r) ∧ (r → p)"))
    print(convert_formula("(¬p ∧ q) ∨ (p ∧ ¬q)"))
    test_translate_expression()
