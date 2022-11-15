def universal_intantiation(formula="∀x(Sx ⇒ Px)", constant="a"):
    variable = "x" or "y" or "z"
    New_formula = (
        formula.replace(variable, constant)
        .replace("∀", "")
        .replace("(", "")
        .replace(")", "")
    )
    New_formula2 = New_formula.replace(constant, "", 1)

    return New_formula2


def existential_intantiation(formula="∃x(Sx ∧ Px)", constant="a"):
    variable = "x" or "y" or "z"
    New_formula = (
        formula.replace(variable, constant)
        .replace("∃", "")
        .replace("(", "")
        .replace(")", "")
    )
    New_formula2 = New_formula.replace(constant, "", 1)

    return New_formula2
