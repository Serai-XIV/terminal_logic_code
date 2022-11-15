from Functions_and_Rules import universal_intantiation  # FIXME import functions from file 'Quantifier Rules.py'


def answer():
    user_aws = str(input("Would you like to to Enter a constant?: "))
    if (user_aws == "Yes") or (user_aws == "yes"):
        user_constant = str(input("Enter a Constant: "))
        print(universal_intantiation(formula, user_constant))
    else:
        print("Goodbye")


user_variable = str(input("Enter a variable from x, y, z: "))
formula = f"∀{user_variable}(S{user_variable} ⇒ P{user_variable})"
print(f'Your formula" {formula}')

answer()
