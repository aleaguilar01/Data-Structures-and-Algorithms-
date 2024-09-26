def compute_closest_to_zero(ts):
    if len(ts) == 0:
        return 0

    diff = float("inf")

    for temp in ts:
        int_diff = abs(temp)

        if int_diff < diff:
            diff = temp

    return diff

print(compute_closest_to_zero([-273]))
print(compute_closest_to_zero([-15, -7, -9, -14, -12]))
print(compute_closest_to_zero([-10, -10]))
