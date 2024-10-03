def longestPeak(array):
    longest_peak = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        print("peak: ", array[i - 1], array[i], array[i + 1])

        left_index = i - 2
        right_index = i + 2



        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            print("here", array[left_index])
            left_index -= 1

        while right_index < len(array) - 1 and array[right_index] < array[right_index - 1]:
            print("here", array[right_index])
            right_index += 1


        current_peaks_lenght = right_index - left_index - 1
        print(right_index, "-", left_index, "=", current_peaks_lenght)

        longest_peak = max(longest_peak, current_peaks_lenght)
        i = right_index

    return longest_peak



array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(array))