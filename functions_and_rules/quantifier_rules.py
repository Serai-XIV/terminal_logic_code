def universal_instantiation(formula="∀x(Sx ⇒ Px)", constant="a"):
    variable = "x" or "y" or "z"
    new_formula = (
        formula.replace(variable, constant)
        .replace("∀", "")
        .replace("(", "")
        .replace(")", "")
    )
    new_formula2 = new_formula.replace(constant, "", 1)

    return new_formula2


def existential_instantiation(formula="∃x(Sx ∧ Px)", constant="a"):
    variable = "x" or "y" or "z"
    new_formula = (
        formula.replace(variable, constant)
        .replace("∃", "")
        .replace("(", "")
        .replace(")", "")
    )
    new_formula2 = new_formula.replace(constant, "", 1)

    return new_formula2
