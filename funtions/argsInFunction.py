# def allsum(*args):
#     print(args)
#     s=0
#     for i in args:
#         s+=i
#     return s
#
# total = allsum(1,5,6,7,9,4)
# print(total)


#
def Values(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])


Values(ticker='Hello', ans="hey", que="hii")