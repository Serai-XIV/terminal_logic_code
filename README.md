# Table of Contents

- [Discord Bot for Logic Calculations](#discord-bot-for-logic-calculations)
  - [Features](#features)
  - [Terminal-Logic-Code](#terminal-logic-code)
  - [Functions](#functions)
    - [`extracting_atoms(s: str) -> List[str]`](#extracting_atomss-str---liststr)

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
