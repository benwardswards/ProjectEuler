total: int = sum(num for num in range(1000) if num % 3 == 0 or num % 5 == 0)


print(f"The total of the numbers divisible by 3 and 5 less than 1000 is {total}")
