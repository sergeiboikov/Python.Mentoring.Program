import fractions


def sum_fractions():
    first_fraction = fractions.Fraction(input(f"Input the first fraction (a/b): "))
    second_fraction = fractions.Fraction(input(f"Input the second fraction (a/b): "))
    result = first_fraction + second_fraction
    print(f'Result is {result}')


sum_fractions()
