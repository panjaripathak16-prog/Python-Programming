length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than Perimeter")
else:
    print("Area is not greater than Perimeter")
