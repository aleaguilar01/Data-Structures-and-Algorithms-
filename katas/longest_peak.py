def longestPeak(array):
    max_counter = 0
    counter = 1
    going_up = False
    going_down = False


    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            if going_down:
                counter += 1
                going_up = True
            else:
                counter = 2
                going_up = False
                going_down = True
        elif array [i - 1] > array[i] and going_up:
            counter += 1
            going_down = True
            going_up = False
        elif array[i - 1] > array[i] and going_down:
            counter += 1
        else:
            print("There is a break here: ", array[i])
            if counter > max_counter:
                max_counter = counter
            going_up = False
            going_down = False
            counter = 1
            print("set counter to: ", counter, " at: ", array[i])

        print(array[i])
        print("counter: ", counter)
        print("going_up: ", going_up)
        print("going_down: ", going_down)
    return max_counter

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(array))