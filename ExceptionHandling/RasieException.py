balance = 0

def deposit(amount):
    global balance
    if(amount<=0):
        raise ValueError("Amount should grater than zero")
    balance+=amount

deposit(5)
deposit(4)
print(balance)
deposit(0)