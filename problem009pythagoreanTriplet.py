"""
A Pythagorean triplet is set of natural numbers such that 
a<b<c, 
a**2 + b**2 = c**

Find the Pythagorean triplet such that,
a+b+c=1000

"""

for a in range(1000):
    for b in range(a + 1, 1000):
        c: int = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            if b < c:
                print(f"a={a}, b={b}, c={c}, product is:{a * b * c}")

