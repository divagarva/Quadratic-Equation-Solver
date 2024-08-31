import math


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The equation has two real and distinct roots: {root1:.2f} and {root2:.2f}"

    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return f"The equation has one real root: {root:.2f}"

    else:
        # No real roots, roots are complex
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"The equation has two complex roots: {real_part:.2f} ± {imaginary_part:.2f}i"


def main():
    print("Quadratic Equation Solver")
    print("The equation is of the form: ax^2 + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    # Check if 'a' is zero
    if a == 0:
        print("Coefficient 'a' cannot be zero in a quadratic equation.")
    else:
        result = solve_quadratic(a, b, c)
        print(result)


if __name__ == "__main__":
    main()
