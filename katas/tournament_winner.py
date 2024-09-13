def tournamentWinner(competitions, results):
    results_dictionary = {}

    for i in range(len(competitions)):
        if results[i] == 0:
            winner = competitions[i][1]

        else:
            winner = competitions[i][0]

        if winner in results_dictionary:
            results_dictionary[winner] += 3
        else:
            results_dictionary[winner] = 3

    winner_score = 0
    winner = ""
    for team in results_dictionary:
        if results_dictionary[team] > winner_score:
            winner = team
            winner_score = results_dictionary[team]

    return winner


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ],
results = [0, 0, 1]
print(tournamentWinner(competitions, results))
