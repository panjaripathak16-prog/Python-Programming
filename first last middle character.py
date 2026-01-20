s = input("Enter a string: ")

print("First character:", s[0])
print("Last character:", s[-1])

if len(s) % 2 != 0:
    mid = len(s) // 2
    print("Middle character:", s[mid])
else:
    print("No middle character (length is even)")
