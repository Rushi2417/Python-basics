file= None
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Exception is handled", e)
finally:
    if file:
        file.close()
    print("File is closed")

