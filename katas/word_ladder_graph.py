def word_ladder(start_word, end_word, word_list):
    if end_word not in word_list:
        return 0

    queue = [(start_word, 1)]
    #abc = ["a", "b", "c", "d", "e", "f", "g", "h", "k", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abc = "abcdefghijklmnopqrstuvwxyz"

    while queue:
        current_word, counter = queue.pop(0)

        if current_word == end_word:
            return counter

        for index in range(len(current_word)):
            print(current_word)
            for letter in abc:
                if letter == current_word[index]:
                    continue
                else:
                    next_word = current_word[:index] + letter + current_word[index + 1:]
                    print(next_word)
                if next_word in word_list:
                    print(next_word)
                    queue.append((next_word, counter + 1))

    return 0


begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

print("return: ", word_ladder(begin_word, end_word, word_list))