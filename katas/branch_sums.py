

def getQueryAnswers(cache_entries, queries):
    key_dictionary = {}
    results = []
    print(cache_entries)
    print(queries)

    for entry in cache_entries:
        key_dictionary[entry[1]] = {
            entry[0]: entry[2]
        }

    for query in queries:
        results.append(key_dictionary[query[0]][query[1]])

    return results
