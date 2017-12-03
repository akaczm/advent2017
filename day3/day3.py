from math import sqrt, fabs

def check_corner(i):
    corner = i
    while not float(sqrt(corner)).is_integer():
        corner += 1

    if sqrt(corner) % 2 != 0:
        print(corner)
        return corner
    else: return check_corner(corner + 1)

def check_distance(inp):
    corner_lr = check_corner(inp)
    side = sqrt(corner_lr)
    vertical_dist = (side - 1) / 2
    # range is prev corner + 1 and curr corner
    pcorner = int(pow((side - 2), 2))
    rnge = [pcorner ,corner_lr]
    side_size = (rnge[1] - rnge[0] + 4) / 4
    corner_ll = corner_lr - side_size + 1
    corner_ul = corner_ll - side_size + 1
    corner_ur = corner_ul - side_size + 1
    corners = [corner_ur, corner_ul, corner_ll, corner_lr]
    distances = []
    for corner in corners: #get closest corner
        distances.append(fabs(corner - inp))
    distance_from_corner = min(distances)
    hor_dist = vertical_dist - distance_from_corner
    print(distance_from_corner)
    print(vertical_dist)
    distance = vertical_dist + hor_dist
    print(distance)

check_distance(368078)