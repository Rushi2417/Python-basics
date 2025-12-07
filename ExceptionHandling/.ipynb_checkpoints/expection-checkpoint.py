a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    d = a/b
except:
    d= -1
    print("Exception is handled")

print(f"D is {d}")