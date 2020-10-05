"""The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
"""

print(
    "1000^^1000 overflows an int64 but python's built in type int expands to fit arbitrary large int"
)

significant_total = sum(i ** i % 10_000_000_000 for i in range(1, 1001))

# print( sum)

print("The first 10 digits of the sum is: ", significant_total % 10_000_000_000)
