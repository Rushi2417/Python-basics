a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    d = a/b
    c = "Hello" + b
except ZeroDivisionError as ze:
    d= -1
    print("Exception is handled", ze)

except TypeError as tp:
    d=-2
    print("Expection is handled", tp)

print(f"D is {d}")