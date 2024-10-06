def minDominoRotations(tops, bottoms):
    rotations_top = 0
    rotations_bottom = 0

    def check_rotations(x, rotations_top, rotations_bottom):
        for i in range(len(tops)):
            if tops[i] == x or bottoms[i] == x:
                if tops[i] != x:
                    rotations_top += 1
                if bottoms[i] != x:
                    rotations_bottom += 1
            else:
                return -1
        return min(rotations_top, rotations_bottom)

    check_top = check_rotations(tops[0], rotations_top, rotations_bottom)
    check_bottom = check_rotations(bottoms[0], rotations_top, rotations_bottom)

    if check_top != -1 and check_bottom != -1:
        return min(check_top, check_bottom)
    elif check_top == -1:
        return check_bottom
    else:
        return check_top


tops = [1,2,1,1,1,2,2,2]
bottoms = [2,1,2,2,2,2,2,2]

print(minDominoRotations(tops, bottoms))
