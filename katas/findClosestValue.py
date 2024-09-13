def findClosestValueInBst(tree, target):

    current = tree
    closest = current.value
    difference = abs(closest - target)

    while current is not None:
        if closest == target:
            return closest

        if target < current.value:
            current = current.left
        else:
            current = current.right

        if abs(current.value - target) < difference:
            difference = abs(current.value - target)
            closest = current.value

    return closest


