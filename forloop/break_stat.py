tar = [50, 42, 32, 45, 1, 84]
month = ["jan", "fed", "mar", "apr", "may", "june"]
thrashfold = 35

# for t in tar:
#     if t<thrashfold:
#         print(f"thrashfold hits {t}")
#         break
#     print(f"tar is greater than thrashfold hits {t}")

for t, m in zip(tar, month):
    print(t, m)