# Sample functions to test the Doc-Genie documentation generator


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


def add_numbers(a, b):
    result = a + b
    return result


def find_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def calculate_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price
