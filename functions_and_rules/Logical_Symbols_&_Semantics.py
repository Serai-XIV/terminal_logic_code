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

    if Forumla == Bivalence["False"]:
        Formula = False
    else:
        Formula = True
    
    return Formula


def Negation(Proposition = 'P'):

    if valuation(Proposition):
        Proposition = Bivalence["False"]
    else:
        Proposition = Bivalence["True"]
    
    return Proposition

print(Negation('P'))
