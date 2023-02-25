# Table of Contents

- [Discord Bot for Logic Calculations](#discord-bot-for-logic-calculations)
  - [Features](#features)
  - [Terminal-Logic-Code](#terminal-logic-code)
  - [Functions](#functions)
    - [`extracting_atoms(x)`](#extracting_atomss-str---liststr)
    - [`extracting_truth_values(x)`](#extracting_truth_valuess-str---dictstr-listbool)
  - [Modules](#modules)
    - [`Logical_Symbols_and_Semantics.py`](#logical_symbol_and_semanticspy)
    - [Dictionarys](#dictionarys)
      - [Logical Symbols](#logical-symbols)
      - [Non-Logical Symbols](#non-logical-symbols)
      - [Operator Mapping to Python Operators](#operator-mapping-to-python-operators)
      - [Bivalence](#bivalence)


# Discord Bot for Logic Calculations

This bot is designed to take natural language input and convert it into formal language for logical calculations. The primary focus is on generating truth tables and understanding the semantics of logical operators.

## Features: 

- Natural language to formal language conversion (limited)
- Truth table generation (needs some work)
- Calculation of truth functions 
- Determination of valid arguments (coming soon)
- more coming soon

## Terminal-Logic-Code: 

The code for this bot is designed to create a foundation for logic calculations in a Discord bot. It uses string methods and logic semantics to generate truth tables and perform other logic calculations.

# Functions:
### `extracting_atoms(s: str) -> List[str]`

Extracts single letters from a string that are not next to any alphabetical characters and eliminates any redundant characters.

### Arguments

* `s` (`str`): The input string.

### Returns

* `atoms` (`List[str]`): A list of single letters from the input string that are not next to any alphabetical characters, with any redundant characters removed.

### Example Usage

```python
extracting_atoms("(P IF Q) AND (Q IF R) AND (R IF P)")
extracting_atoms("(p → q) ∧ (q → r) ∧ (r → p)")
extracting_atoms("")
```
### Output

    ['P', 'Q', 'R']
    ['p', 'q', 'r']
	[]

### `extracting_truth_values(s: str) -> Dict[str, List[bool]]`

Generates a truth table for a logical statement by extracting the atoms and listing their possible truth values.

#### Arguments

- `s` (`str`): The input string representing a logical statement.

#### Returns

- `atoms_dict` (`Dict[str, List[bool]]`): A dictionary where the keys are the atoms in the logical statement and the values are lists of Booleans representing the possible truth values of the atoms.

#### Example Usage

```python
extracting_truth_values("(P IF Q) AND (Q IF R) AND (R IF P)")
extracting_truth_values("(p → q) ∧ (q → r) ∧ (r → p)")
```
### Output

	{'P': [False, True], 'Q': [False, True], 'R': [False, True]}
	{'p': [False, True], 'q': [False, True], 'r': [False, True]}

## Modules:

The purpose of this section is to provide information regarding modules and files that are designed to support the main file of a programming project. These modules may contain functions, classes, or other resources that can enhance the project's overall functionality. It is important to note that additional modules may be added gradually over time, so the number of modules implemented thus far should not be overwhelming.

### `Logical_Symbols_and_Semantics.py`

> This module defines a dictionary of logical operator symbols that contains entries for various logical operators, including negation, conjunction, and material conditional. The dictionary provides a list of symbols that can be used to represent each operator and serves as a reference for logical operator symbols. Additionally, the dictionary is easily updatable and extendable to add more operators or symbols. (this module also uses the operator library supported by python; you can check it out at [Standard operators as functions](https://docs.python.org/3/library/operator.html "Standard operators as functions") this is to ensure readbility)

#### Dictionarys

##### Logical Symbols

The `Logical_Symbols` dictionary maps logical operators to their corresponding symbols in various notation systems. It contains the following entries:

| Operator                 | Symbols           |
|--------------------------|-------------------|
| Negation                 | ["¬", "~", "!"]    |
| Conjunction              | ["∧", "&", "·"]    |
| Inclusive Disjunction    | ["∨"]              |
| Material Conditional     | ["→", "⇒", "⊃"]   |
| Material Bi-Conditional  | ["↔", "⇔", "≡"]   |
| Universal Quantifier     | "∀"               |
| Existential Quantifier   | "∃"               |
| Falsum                   | "⊥"               |
| Verum                    | "⊤"               |
| Identical To             | "="               |
| Variables                | ["x", "y", "z"]   |

You can easily update and extend the dictionary to add more operators or symbols.

**Example Usage:**
```python
from logical_symbols import Logical_Symbols

# Print the symbol for negation in different notations
print(Logical_Symbols["Negation"])  # ["¬", "~", "!"]

```

##### Non-Logical Symbols

The `Non_Logical_Symbols` dictionary maps various non-logical symbols used in logic to their corresponding symbols. It contains the following entries:

| Type              | Symbols                                |
|-------------------|----------------------------------------|
| Subscript         | ["₀", "₁", "₃", "₄", "₅", "₆", "₇", "₈", "₉"] |
| Predicate         | "ABCDEFGHIJKLMNOPQRSTUVWXYZ"         |
| Constants         | "abcdefghijklmopqrstuvw"                |
| Function Symbol   | "𝑓"                                    |
| Punctuation Marks | "(,) ,"                                |

**Example Usage:**
```python
from non_logical_symbols import Non_Logical_Symbols

# Print the subscripts
print(Non_Logical_Symbols["Subscript"])  # ["₀", "₁", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

```

##### Operator Mapping to Python Operators

The `ops` dictionary maps operator symbols to Python operators. It contains the following entries:

| Operator   | Python Operator |
|------------|-----------------|
| and        | operator.and_   |
| or         | operator.or_    |
| not        | operator.not_   |
| implies    | lambda a, b: (not a) or b |
| iff        | operator.eq     |

**Example Usage:**
```python
from operators import ops

# Evaluate a logical expression using the 'and' operator
a = True
b = False
print(ops["and"](a, b))  # False

```

##### Bivalence

The `Bivalence` dictionary is a semantic principle that states only two truth states are present (within a given logical system). It maps boolean values to their corresponding symbols:

| Boolean Value | Symbol |
|---------------|--------|
| True          | T      |
| False         | F      |

**Example Usage:**
```python
from bivalence import Bivalence

# Print the symbol for the truth value True
print(Bivalence["True"])  # "T"

```