# dictionary of all logical operator symbols
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

# Lexicon for all non-logical symbols
Non_Logical_Symbols = {
    "Subscript": ["₀", "₁", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    "Predicate": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Constants": "abcdefghijklmopqrstuvw",
    "Function Symbol": "𝑓",
    "Punctuation marks": "(,) ,",
}

# the principal of bivalnce is a semantic princiapl that states only two truth states are present (within a given logical system)
Bivalence = {"True": "T", "False": "F"}


def valuation(Forumla):  # The Defintion of the valuation Function

    if Forumla == Bivalence["True"]:
        Formula = True
    else:
        Formula = False

    return Formula


def negation(Proposition):

    if valuation(Proposition):
        Proposition = Bivalence["False"]
    else:
        Proposition = Bivalence["True"]

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


def m_condtional(Left_Proposition, Right_Proposition):

    if disjunction(negation(Left_Proposition), Right_Proposition):
        Formula = Bivalence["True"]
    else:
        Formula = Bivalence["False"]

    return Formula


def m_biconditional(Left_implication, right_implication):

    if m_condtional(Left_implication, right_implication) and m_condtional(
        right_implication, Left_implication
    ):
        Formula = Bivalence["True"]
    else:
        Formula = Bivalence["False"]

    return Formula


def truth_table(
    *statements,
):  # FIXME create a for loop, and express the relationship between num of atomic propositions and lines in a truth table

    truth_values = {"T", "F"}

    for n in truth_values:
        for number in {"F", "T"}:
            print(n, number)

    pass


# Down below should be testing ground for all operators, and the operators should be defined by these conditions

print(
    f'If P is false, then {Logical_Symbols["Negation"][0]}P shall return true: {negation("F")}'
)  # negation should return true if false, and false if true
print(
    f'If P is true, then {Logical_Symbols["Negation"][0]}P shall return false: {negation("T")}\n'
)

print(
    f'If P is true, and Q true; then P {Logical_Symbols["Conjunction"][0]} Q shall return true: {conjunction("T", "T")}'
)  # the conjunction should return true if and only if both operands are true, and false otherwise
print(
    f'If P is true, and Q is false; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("T", "F")}'
)
print(
    f'If P is false, and Q is true; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("F", "T")}'
)
print(
    f'If P is false, and Q is false; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("F", "F")}\n'
)

print(
    f'If P is true, and Q true; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("T", "T")}'
)  # the inclusive disjunction should return false if and only if both operands are false, and true otherwise
print(
    f'If P is true, and Q is false; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("T", "F")}'
)
print(
    f'If P is false, and Q is true; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("F", "T")}'
)
print(
    f'If P is false, and Q is false; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return false: {disjunction("F", "F")}\n'
)

print(
    f'If P is true, and Q true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("T", "T")}'
)  # the material conditional should return false if and only if the right operand is false while leaving the left operand true; otherwise true
print(
    f'If P is true, and Q is false; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("T", "F")}'
)
print(
    f'If P is false, and Q is true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return false: {m_condtional("F", "T")}'  # FIXME this should return false
)
print(
    f'If P is false, and Q is false; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("F", "F")}\n'
)

print(
    f'If P is true, and Q true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_biconditional("T", "T")}'
)  # the material bi-conditional should return true if and only if both operands have the same truth value, and otherwise false
print(
    f'If P is true, and Q is false; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return false: {m_biconditional("T", "F")}'  # FIXME this should return false
)
print(
    f'If P is false, and Q is true; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return false: {m_biconditional("F", "T")}'  # FIXME this should return false
)
print(
    f'If P is false, and Q is false; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return true: {m_biconditional("F", "F")}\n'
)
