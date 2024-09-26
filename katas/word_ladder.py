##https://leetcode.com/problems/word-ladder/description/
def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        print("Word not in here")
        return 0

    start_position = 0
    final_position = 0
    begin_word_on_list = False

    for i in range(len(wordList)):
        counter = 0
        for j in range(len(wordList[i])):
            if word_list[i][j] == beginWord[j]:
                counter += 1
        if counter == len(wordList):
            start_position = i + 1
            begin_word_on_list = True

        if counter == len(wordList[i]) - 1:
            start_position = i + 1

    for i in range(len(wordList)):
        counter = 0
        for j in range(len(wordList[i])):
            if wordList[i][j] == endWord[j]:
                counter += 1
        if counter == len(wordList[i]) - 1:
            final_position = i + 1
            break

    if begin_word_on_list:
        return final_position - start_position + 2
    if not begin_word_on_list:
        return final_position - start_position + 3


begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

print("return: ", ladderLength(begin_word, end_word, word_list))

