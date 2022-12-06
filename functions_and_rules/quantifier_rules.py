def universal_instantiation(formula="∀x(Sx ⇒ Px)", constant="a"):
    """
    Apply the rule of universal instantiation to a given formula.
    
    The rule of universal instantiation states that if a formula of the form
    ∀x(Px) is true, then the formula Pc is also true, where c is any constant.
    
    This function takes a formula and a constant as input, and returns the
    resulting formula after applying the rule of universal instantiation.
    
    Args:
        formula: a string representing the formula to be instantiated.
        constant: a string representing the constant to be used in the instantiation.
    
    Returns:
        The resulting formula after applying the rule of universal instantiation.
    """
    # Extract the variable from the formula using a hardcoded list of possible variables
    variable = "x" or "y" or "z"

    # Replace the variable and quantifier in the formula with the constant, and remove the parentheses
    new_formula = (
        formula.replace(variable, constant)
        .replace("∀", "")
        .replace("(", "")
        .replace(")", "")
    )
    
    # Remove the first occurrence of the constant in the formula
    new_formula2 = new_formula.replace(constant, "", 1)

    return new_formula2

def existential_instantiation(formula="∃x(Sx ∧ Px)", constant="a"):
    """
    Apply the rule of existential instantiation to a given formula.
    
    The rule of existential instantiation states that if a formula of the form
    ∃x(Px) is true, then the formula Pc is also true, where c is any constant.
    
    This function takes a formula and a constant as input, and returns the
    resulting formula after applying the rule of existential instantiation.
    
    Args:
        formula: a string representing the formula to be instantiated.
        constant: a string representing the constant to be used in the instantiation.
    
    Returns:
        The resulting formula after applying the rule of existential instantiation.
    """
    # Extract the variable from the formula using a hardcoded list of possible variables
    variable = "x" or "y" or "z"

    # Replace the variable and quantifier in the formula with the constant, and remove the parentheses
    new_formula = (
        formula.replace(variable, constant)
        .replace("∃", "")
        .replace("(", "")
        .replace(")", "")
    )
    
    # Remove the first occurrence of the constant in the formula
    new_formula2 = new_formula.replace(constant, "", 1)

    return new_formula2
