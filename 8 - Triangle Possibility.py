a = int(input("First Side: "))
b = int(input("Second Side: "))
c = int(input("Third Side: "))
if a**2<=b**2+c**2 and b**2<=a**2+c**2 and c**2<=a**2+b**2:
    print("Triangle")
else:
    print("Not Triangle")