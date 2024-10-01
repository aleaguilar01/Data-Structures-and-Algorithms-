def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        print("End word not in word list.")
        return 0

    if len(beginWord) == 1:
        return 2

    start_position = 0
    end_position = 0

    for i in range(len(wordList)):
        counter = 0
        for j in range(len(wordList[i])):
            if wordList[i][j] == beginWord[j]:
                counter += 1
        if counter == len(beginWord) - 1:
            start_position = i
            break

    for i in range(len(wordList)):
        counter = 0
        for j in range(len(wordList[i])):
            if wordList[i][j] == endWord[j]:
                counter += 1
        if counter == len(endWord) - 1:
            end_position = i

    if end_position == 0:
        return 0

    results = end_position - start_position + 1

    if beginWord in wordList:
        results += 1

    return results





# Example usage:
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
word_list_2 = ["hot","dot","dog","lot","log"]



print("Shortest transformation sequence length:", ladderLength(begin_word, end_word, word_list))
print("Shortest transformation sequence length:", ladderLength(begin_word, end_word, word_list_2))
