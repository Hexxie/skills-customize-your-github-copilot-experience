from io_utils import get_user_numbers
from math_utils import add_numbers, multiply_numbers


def main():
    num1, num2 = get_user_numbers()
    total = add_numbers(num1, num2)
    product = multiply_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {total}.")
    print(f"The product of {num1} and {num2} is {product}.")


if __name__ == "__main__":
    main()
