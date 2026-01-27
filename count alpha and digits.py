s = input("Enter a string: ")

alpha = 0
digit = 0

for ch in s:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1

print("Alphabets:", alpha)
print("Digits:", digit)
