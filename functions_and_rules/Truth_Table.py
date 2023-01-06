from typing import List, Dict
from Logical_Symbols_and_Semantics import connectives


def extracting_atoms(s: str) -> List[str]:
    """Extracts single letters from a string that are not next to any alphabetical characters and eliminates any redundant characters.

    Args:
        s (str): The input string.

    Returns:
        atoms (List[str]): A list of single letters from the input string that are not next to any alphabetical characters, with any redundant characters removed.

    Example:
        >>> extracting_atoms("(P IF Q) AND (Q IF R) AND (R IF P)") -> ['P', 'Q', 'R']
        >>> extracting_atoms("(p → q) ∧ (q → r) ∧ (r → p)") -> ['p', 'q', 'r']
        >>> extracting_atoms("") -> []
    """
    atoms = []
    for i, c in enumerate(s):
        if c.isalpha():
            if (i == 0 or not s[i - 1].isalpha()) and (
                i == len(s) - 1 or not s[i + 1].isalpha()
            ):
                atoms.append(c)
    return list(set(atoms))


def extracting_truth_values(s: str) -> Dict[str, List[bool]]:
    """Generates a truth table for a logical statement by extracting the atoms and listing their possible truth values.

    Args:
        s (str): The input string representing a logical statement.

    Returns:
        atoms_dict (Dict[str, List[bool]]): A dictionary where the keys are the atoms in the logical statement and the values are lists of Booleans representing the possible truth values of the atoms.

    Example:
        >>> extracting_truth_values("(P IF Q) AND (Q IF R) AND (R IF P)") -> {'P': [False, True], 'Q': [False, True], 'R': [False, True]}
        >>> extracting_truth_values("(p → q) ∧ (q → r) ∧ (r → p)") -> {'p': [False, True], 'q': [False, True], 'r': [False, True]}
    """
    atoms = extracting_atoms(s)
    atoms_dict = {atom: [False, True] for atom in atoms}
    return atoms_dict


def truth_table(
    operator, values
):  # FIXME: Set the atomic propositions to the side, and the logical expression as the header. Also make it to where the function utilizes the function from the previous snippet.
    """
    Generate a truth table for a given logical operator applied to a list of boolean values.

    Parameters:
    - operator: a function that takes two boolean values as input and returns a boolean value.
    - values: a list of boolean values.

    Returns:
    - A list of tuples, each containing two input values and the result of applying the operator to those values.
    """
    # Create a list to hold the truth table tuples
    truth_table = []

    # Iterate over the input values
    for value1 in values:
        for value2 in values:
            # Apply the operator to the values and add the result to the truth table
            truth_table.append((value1, value2, operator(value1, value2)))

    col_widths = [max(len(str(value)) for value in col) for col in zip(*truth_table)]

    # Print a header row
    print("  ".join(str(i).ljust(col_widths[i]) for i in range(len(col_widths))))
    print("-" * sum(col_widths))

    # Print the data rows
    for row in truth_table:
        print("  ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row)))


# Test the truth table function
truth_table(connectives["and"], [True, False])
# Output:
# 0      1      2
# ---------------
# True   True   True
# True   False  False
# False  True   False
# False  False  False
