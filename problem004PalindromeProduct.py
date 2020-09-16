# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

listofpalindromes = []
for num1 in range(99, 9, -1):
    for num2 in range(99, num1 - 1, -1):
        product12 = num1 * num2
        if int(str(product12)[::-1]) == product12:
            listofpalindromes.append(product12)
            break
print(
    f"The maximum product of two, 2 digit numbers that is a palindrome is {max(listofpalindromes)}"
)

listofpalindromes = []
for num1 in range(999, 99, -1):
    for num2 in range(999, num1 - 1, -1):
        product12 = num1 * num2
        if int(str(product12)[::-1]) == product12:
            listofpalindromes.append(product12)
            break
print(
    f"The maximum product of two, 2 digit numbers that is a palindrome is {max(listofpalindromes)}"
)

