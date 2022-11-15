Logical_Symbols = {
    "Negation": ["¬", "~", "!", "not"],
    "Conjunction": ["∧", "&", "·", "and"],
    "Inclusive Disjunction": ["∨", "or"],
    "Material Conditional": ["→", "⇒", "⊃", "if, then"],
    "Material Bi-Conditional": ["↔", "⇔", "≡"],
    "Universal Quantifier": "∀",
    "Existential Quantifier": "∃",
    "Falsum": "⊥",
    "Verum": "⊤",
    "Identical to": "=",
    "Variables": ["x", "y", "z"],
}

Non_Logical_Symbols = {
    "Subscript": ["₀", "₁", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    "Predicate": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Constants": "abcdefghijklmopqrstuvw",
    "Function Symbol": "𝑓",
    "Punctuation marks": "(,) ,",
}

Bivalence = {"True": "T", "False": "F"}


def valuation(Forumla):  # The Defintion of the valuation Function

    if Forumla == True:
        Formula = True
    else:
        Formula = False

    return Formula


def negation(Proposition):

    if valuation(Proposition):
        Proposition = Bivalence["True"]
    else:
        Proposition = Bivalence["False"]

    return Proposition


def conjunction(Left_Hand_Proposition, Right_Hand_Proposition):

    if valuation(Left_Hand_Proposition) and valuation(Right_Hand_Proposition):
        Formula = Bivalence["True"]

    elif valuation(Left_Hand_Proposition) or valuation(Right_Hand_Proposition):
        Formula = Bivalence["False"]
    else:
        Formula = Bivalence["False"]

    return Formula


def disjunction(Left_hand_disjunct, Right_Hand_Disjunct):

    if valuation(Left_hand_disjunct) or valuation(Right_Hand_Disjunct):
        Formula = Bivalence["True"]

    elif valuation(Left_hand_disjunct) and valuation(Right_Hand_Disjunct):
        Formula = Bivalence["False"]
    else:
        Formula = Bivalence["False"]

    return Formula


def m_condtional(
    Left_Proposition, Right_Proposition
):  # FIXME define material conditional

    pass


def truth_table(
    *statements,
):  # FIXME create a for loop, and express the relationship between num of atomic propositions and lines in a truth table

    for num in Bivalence:
        for number in {"F", "T"}:
            print(num, number)


