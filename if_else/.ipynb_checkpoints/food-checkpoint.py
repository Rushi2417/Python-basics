indian = ["Dal", "Chaval", "Roti", "Chapati"]
italian = ["Pizza", "Burger", "Pasta"]
Chaines = ["Rice", "Noddles"]

dish = input("Input a dish: ")
if dish in indian:
    print(f"Dish {dish} is indian")
elif dish in italian:
    print(f"Dish {dish} is italian")
else:
    print(f"Dish {dish} is Chaines")