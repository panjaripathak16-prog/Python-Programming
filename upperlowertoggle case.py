#conver to lower case
def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

text = input("Enter a string: ")
print("Lower case:", to_lower(text))

#convert to upper case
def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

text = input("Enter a string: ")
print("Upper case:", to_upper(text))

#convert to toggle case
def toggle_case(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

text = input("Enter a string: ")
print("Toggle case:", toggle_case(text))
