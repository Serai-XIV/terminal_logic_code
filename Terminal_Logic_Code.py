from functions_and_rules.quantifier_rules import universal_instantiation
from functions_and_rules.Logical_Symbols_and_Semantics import conjunction, m_condtional, disjunction, m_biconditional, negation, Logical_Symbols, Logical_operators

def answer():
    """
    Prompt the user to input a constant and apply the rule of universal instantiation.
    
    This function prompts the user to input a constant value and applies the rule of
    universal instantiation to a given formula using the `universal_instantiation`
    function from the `quantifier_rules` module.
    
    The function prints the resulting formula after applying the rule of universal
    instantiation, or a goodbye message if the user chooses not to enter a constant.
    """
    # Prompt the user to input a constant
    user_aws = str(input("Would you like to to Enter a constant?: "))
    
    # If the user inputs "Yes" or "yes", apply the rule of universal instantiation
    if (user_aws == "Yes") or (user_aws == "yes"):
        user_constant = str(input("Enter a Constant: "))
        print(universal_instantiation(formula, user_constant))
    
    # Otherwise, print a goodbye message
    else:
        print("Goodbye")


# Prompt the user to input a variable
user_variable = str(input("Enter a variable from x, y, z: "))

# Construct a formula using the input variable
formula = f"∀{user_variable}(S{user_variable} ⇒ P{user_variable})"
print(f'Your formula" {formula}')

# Call the `answer` function
answer()

# Prompt the user to view the conditions for the main logical operators
user_aws = input('Would you like to see the conditions for the main logical operators?: ')
print()

# If the user inputs "Yes" or "yes" or "y", display the conditions
if user_aws == 'Yes' or 'yes' or 'y':
    Logical_operators()

# Otherwise, print a goodbye message
else:
    print('Goodbye')
