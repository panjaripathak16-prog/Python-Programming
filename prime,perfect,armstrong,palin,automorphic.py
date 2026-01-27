n = int(input("Enter a number: "))

# Prime
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print("Prime" if count == 2 else "Not Prime")

# Perfect
sum1 = 0
for i in range(1, n):
    if n % i == 0:
        sum1 += i
print("Perfect" if sum1 == n else "Not Perfect")

# Armstrong
temp = n
sum2 = 0
while temp > 0:
    d = temp % 10
    sum2 += d**3
    temp //= 10
print("Armstrong" if sum2 == n else "Not Armstrong")

# Palindrome
if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Automorphic
sq = n*n
if str(sq).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")
