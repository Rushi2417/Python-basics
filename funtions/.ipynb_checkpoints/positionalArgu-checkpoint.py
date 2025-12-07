# def cal_vol(r, h):
#     volume = 3.14 * r*r *h
#     return volume
#
# radius = 40
# height = 10
#
# v= cal_vol(h = height, r = radius)
# print(v)


# Default height
def cal_vol(r, h=7):
    volume = 3.14 * r*r *h
    return volume

radius = 40
height = 10

v= cal_vol(r = radius)
print(v)