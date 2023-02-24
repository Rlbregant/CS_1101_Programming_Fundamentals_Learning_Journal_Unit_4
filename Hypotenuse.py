# #Step 1:
# #Define the function hypotenuse that takes two arguments, a and b, and returns their sum.
#
# def hypotenuse(a, b):
#     return a + b
#
# print(hypotenuse(3, 4))  # Output: 7
#
# #Step 2:
# #Modify the function to return the square root of the sum of the squares of the two arguments.
#
# def hypotenuse(a, b):
#     return math.sqrt(a**2 + b**2)
# #test
# print(hypotenuse(3, 4))  # Output: 5.0
#
# #Step 3:
# #error handling to ensure that a and b are both positive numbers.
#
# def hypotenuse(a, b):
#     if a < 0 or b <=0:
#         raise ValueError("a and b must be positive")
#     return math.sqrt(a**2 + b**2)
# #test
# print(hypotenuse(-3, 4))  # Output: ValueError: a and b must be positive
#
# #Step 4:
# #Mash it together
#
import math


def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both arguments must be positive")
    return math.sqrt(a ** 2 + b ** 2)


def main():
    # Example usage of hypotenuse function
    print(hypotenuse(3, 4))  # Output: 5.0
    print(hypotenuse(5, 12))  # Output: 13.0
    print(hypotenuse(7, 24))  # Output: 25.0
    print(hypotenuse(9, 40))  # Output: 41.0


if __name__ == '__main__':
    main()
