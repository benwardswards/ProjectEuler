def factorial(num: int) -> int:
    prod: int = 1
    for i in range(1, num + 1):
        prod = prod * i

    return prod


assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(4) == 24

# note factorial(40) is larger than a int64! so numba fails
print("number of paths is ", int(factorial(40) / factorial(20) / factorial(20)))

