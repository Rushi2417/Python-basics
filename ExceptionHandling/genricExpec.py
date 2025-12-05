a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    d = a/b
    c = "Hello" + b
except Exception as e:
    d= -1
    print("Exception is handled", e)


print(f"D is {d}")