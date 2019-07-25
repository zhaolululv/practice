from math import sqrt
from math import pow

# 04-1
# 查验素数
"""
a = int(input("enter a number:"))
i = 2
is_prime = True
while i < a:
    if a <= 3:
        break
    elif a % i == 0:
        is_prime = False
        break
    else:
        i += 1
if is_prime:
    print("prime")
else:
    print("not prime")
"""

# 04-2
# 最大公约最小公倍数
"""
a = int(input("enter first number "))
b = int(input("enter second number"))
if a > b:
    a, b = b, a
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print("%d and %d has GCD %d" % (a, b, i))
        break
"""

# 04-3
# 打印三角形
"""
lines = int(input("enter number of line"))
for i in range(0, lines):
    print("*" * (i + 1))
for i in range(lines, 0, -1):
    print(" " * (i - 1) + "*" * (lines - i + 1))
for i in range(0, lines):
    print(" " * ((lines - i)) + "*" * (2 * i + 1))

"""

# 05-1
# 寻找水仙花数
"""
for i in range(100, 1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    sum = pow(a, 3) + pow(b, 3) + pow(c, 3)
    if sum == i:
        print(i)
"""
# 05-2
# 寻找完备数
"""
for num in range(1, 10000):
    sum = 0
    if num > 2:
        for i in range(num - 1, 0, -1):
            if num % i == 0:
                sum += i
    if sum == num:
        print(num)
"""

