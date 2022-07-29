a = int(input("First Side: "))
b = int(input("Second Side: "))
c = int(input("Third Side: "))
if a<b+c and b<a+c and c<a+b:
    print("Triangle")
else:
    print("Not Triangle")