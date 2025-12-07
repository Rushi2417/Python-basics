n = input("input a number: ")
n = int(n)

if n%2==0:
    print("Even number")
else:
    print("Odd number")


Message = "number is even" if n%2==0 else "number is odd"
print(Message)


if not n%2==0:
    print("odd number")
else:
    print("even number")