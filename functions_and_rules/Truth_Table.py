from typing import List, Dict, Union, Any
from Logical_Symbols_and_Semantics import ops
import itertools
import string
import functools
import re


def delete_nulls(lst: List[List[int]]) -> List[List[int]]:
    """
    Removes all occurrences of None in the given list and its nested lists.

    Parameters:
    - lst: a list of lists of integers.

    Returns:
    - The list with all occurrences of None removed.
    """
    for i, elem in enumerate(lst):
        if elem is None:
            del lst[i]
        elif isinstance(elem, list):
            delete_nulls(elem)
    return lst


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


# Regular expression pattern for matching atomic propositions
prop_pattern = re.compile("[a-z]")

# FIXME: Make the propostional variables match the atomic propositions of the formula.
def generate_truth_table(
    formula: str, num_props: int, semantics: Dict[str, Any]
) -> List[List[int]]:
    """
    Generates a truth table for the given logical formula.

    Parameters:
    - formula: a string representing a logical formula in propositional logic.
        The formula can contain the following operators: negation ('~'), conjunction ('&'),
        disjunction ('|'), and implication ('->').
    - num_props: an integer representing the number of atomic propositions in the formula.
    - semantics: a dictionary mapping each operator in the formula to a function that defines
        its semantics. The functions should take in two boolean arguments and return a boolean.
        For example, the semantics for negation could be defined as:
        {'~': lambda x: not x}

    Returns:
    - A truth table as a list of lists, where each inner list represents a row in the table.
        The first row contains the labels for each column (i.e. the atomic propositions and 'output').
        Each subsequent row contains the truth values for each atomic proposition and the output
        of the formula for those truth values.
    """
    # Initialize empty truth table with num_props + 1 columns (for output)
    truth_table = []

    # Generate a list of atomic propositions (e.g. ['p', 'q', 'r', ...])
    atomic_props = list(string.ascii_lowercase)[:num_props]

    # Generate all possible combinations of inputs
    input_combinations = itertools.product([0, 1], repeat=num_props)

    # Evaluate the formula for each combination of inputs and add a row to the truth table
    for inputs in input_combinations:
        # Bind each atomic proposition to its corresponding input value
        prop_values = dict(zip(atomic_props, inputs))
        # Parse and evaluate the formula with the given input values and add the output to the truth table
        truth_table.append(
            list(inputs) + [parse_and_eval(formula, semantics, prop_values)]
        )

    # Add the atomic propositions as column labels
    truth_table.insert(0, atomic_props + ["output"])

    return delete_nulls(truth_table)


def parse_and_eval(
    formula: str, semantics: Dict[str, Any], prop_values: Dict[str, int]
) -> int:
    """
    Recursively parses and evaluates a logical formula.

    Parameters:
    - formula: a string representing a logical formula in propositional logic.
        The formula can contain the following operators: negation ('~'), conjunction ('&'),
        disjunction ('|'), and implication ('->').
    - semantics: a dictionary mapping each operator in the formula to a function that defines
        its semantics. The functions should take in two boolean arguments and return a boolean.
        For example, the semantics for negation could be defined as:
        {'~': lambda x: not x}
    - prop_values: a dictionary mapping each atomic proposition in the formula to its truth value
        (either 0 or 1).

    Returns:
    - The truth value of the formula (either 0 or 1).
    """
    # Check if the formula is an atomic proposition
    match = prop_pattern.fullmatch(formula)
    if match:
        # Return the value of the atomic proposition
        return prop_values[formula]
    else:
        # Check if the formula is a negation
        if formula[:3] == "not":
            # Parse and evaluate the negated formula
            return not parse_and_eval(formula[3:], semantics, prop_values)
        else:
            # Find the first operator in the formula
            for i, c in enumerate(formula):
                if c in ops:
                    # Split the formula into the operator and its operands
                    op = c
                    left = formula[:i]
                    right = formula[i + 1 :]
                    # Parse and evaluate the operands
                    left_eval = parse_and_eval(left, semantics, prop_values)
                    right_eval = parse_and_eval(right, semantics, prop_values)
                    # Apply the operator to the operands
                    return ops

def print_truth_table(truth_list: List[List[Union[int, str]]], formula: str) -> None:
    """
    Prints a modified truth table with the given formula.

    Parameters:
    truth_list (List[List[Union[int, str]]]): A list of lists representing the truth table, where each sublist
        represents a row in the truth table. The last element of the first list represents the formula, and the
        last element of every other list is a result of the formula being applied to that row.
    formula (str): The formula to be applied to each row in the truth table.

    Returns:
    None
    """
    # Initialize the modified truth table with the input list
    modified_truth_table = truth_list

    # Replace the last element of the first list with the formula
    modified_truth_table[0][-1] = formula

    # Put the last element within every other list in a separate list at the bottom of the formula
    for row in modified_truth_table[1:]:
        result = row.pop(-1)
        row.append([result])

    # Calculate the maximum width of each column
    column_widths = [len(str(item)) for row in modified_truth_table for item in row]
    column_widths = [max(column_widths[i::len(modified_truth_table[0])]) for i in range(len(modified_truth_table[0]))]

    # Print the modified truth table with the columns aligned
    for row in modified_truth_table:
        print("  ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row)))
# below is a little test, plus let me know if there are any bugs

formula = "(p and q) or (r and s)"
num_props = 4
semantics = (
    {}
)  # I understand that this is an empty dictionary, and I explicityly state in the documenation above that the user must define the semantics of the operators. I'm not sure how to do this, but what is really doing the work is the 'ops' disctionary, I just wanted to use semantics since it made it more meaningful.
truth_table = generate_truth_table(formula, num_props, semantics)
print(truth_table)

truth_list = [['p', 'q', 'r', 'output'], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
formula2 = "(p or q) and r"

print_truth_table(truth_list, formula2)