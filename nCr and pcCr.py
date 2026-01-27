n = int(input("Enter n: "))
r = int(input("Enter r: "))

fact = 1
for i in range(1, n+1):
    fact *= i
fn = fact

fact = 1
for i in range(1, r+1):
    fact *= i
fr = fact

fact = 1
for i in range(1, n-r+1):
    fact *= i
fnr = fact

nCr = fn // (fr * fnr)
nPr = fn // fnr

print("nCr =", nCr)
print("nPr =", nPr)
