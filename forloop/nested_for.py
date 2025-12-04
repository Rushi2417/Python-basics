products = ["iphone", "tv", "machine"]
contry = ["USA", "India", "Chaina"]
revenue = [50,10,60,45,10,20,30,45,10]
i=0
for product in products:
    for rev in revenue:
        i += 1
        print(f"{product} {rev} revenue is {revenue[i]}")