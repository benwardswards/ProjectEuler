# find sum of all even fibonacci numbers below 4 million

fib1: int = 1
fib2: int = 2
sumofevenfibs: int = 0
print("The even fibonacci numbers are:")
while fib2 <= 4_000_000:
    if fib2 % 2 == 0:
        print(fib2)
        sumofevenfibs += fib2

    fib2, fib1 = fib1 + fib2, fib2


print(f"The sum of all even fibonacci number below 4 million is {sumofevenfibs}")
