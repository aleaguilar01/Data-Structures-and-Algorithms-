def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        print("End word not in word list.")
        return 0

    # Initialize the queue with a list
    queue = [(beginWord, 1)]

    while queue:
        current_word, steps = queue.pop(0)  # Pop from the front of the list (this is O(n))

        if current_word == endWord:
            return steps

        # Try changing each character in the current word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == current_word[i]:
                    continue  # Skip same character
                next_word = current_word[:i] + c + current_word[i + 1:]

                if next_word in word_set:
                    queue.append((next_word, steps + 1))  # Append to the end of the list (this is O(1))
                    word_set.remove(next_word)  # Mark as visited

    return 0

# Example usage:
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]



print("Shortest transformation sequence length:", ladderLength(begin_word, end_word, word_list))