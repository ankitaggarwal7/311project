import collections
from itertools import combinations

number = 0
types_of_players = [{"name": "T4T", "points": 0, "history": [], "id": None}, {"name": "G", "points": 0, "history": [], "id": None}, {"name": "AC", "points": 0, "history": [], "id": None}, {"name": "AD", "points": 0, "history": [], "id": None}]


def play_game(n, m, p, k):
    players = []
    for i in range(len(types_of_players)):
        for j in range(int(n/len(types_of_players))):
            players.append(types_of_players[i])
            players[i*int(n/len(types_of_players))+j]["id"] = i*int(n/len(types_of_players))+j
    for gen in range(k):
        for player in players:
            player["history"] = []
            player["points"] = 0
        for _ in range(m):
            for combination in list(combinations(players, 2)):
                player1_choice = None
                player2_choice = None
                if combination[0]["name"] == "AD":
                    player1_choice = "Defect"
                elif combination[0]["name"] == "AC":
                    player1_choice = "Cooperate"
                elif combination[0]["name"] == "T4T":
                    for choice in reversed(combination[0]["history"]):
                        if choice["id"] == combination[1]["id"]:
                            player1_choice = choice["choice"]
                            break
                    if player1_choice is None:
                        player1_choice = "Cooperate"
                elif combination[0]["name"] == "G":
                    for choice in combination[0]["history"]:
                        if choice["id"] == combination[1]["id"] and choice["choice"] == "Defect":
                            player1_choice = "Defect"
                    if player1_choice is None:
                        player1_choice = "Cooperate"
                if combination[1]["name"] == "AD":
                    player2_choice = "Defect"
                elif combination[1]["name"] == "AC":
                    player2_choice = "Cooperate"
                elif combination[1]["name"] == "T4T":
                    for choice in reversed(combination[1]["history"]):
                        if choice["id"] == combination[0]["id"]:
                            player2_choice = choice["choice"]
                            break
                    if player2_choice is None:
                        player2_choice = "Cooperate"
                elif combination[1]["name"] == "G":
                    for choice in combination[1]["history"]:
                        if choice["id"] == combination[0]["id"] and choice["choice"] == "Defect":
                            player2_choice = "Defect"
                    if player2_choice is None:
                        player2_choice = "Cooperate"
                if player1_choice == "Defect" and player2_choice == "Defect":
                    combination[0]["points"] += 1
                    combination[1]["points"] += 1
                elif player1_choice == "Defect" and player2_choice == "Cooperate":
                    combination[0]["points"] += 5
                elif player1_choice == "Cooperate" and player2_choice == "Defect":
                    combination[1]["points"] += 5
                elif player1_choice == "Cooperate" and player2_choice == "Cooperate":
                    combination[0]["points"] += 3
                    combination[1]["points"] += 3

                combination[0]["history"].append({"id": combination[1]["id"], "choice": player2_choice})
                combination[1]["history"].append({"id": combination[0]["id"], "choice": player1_choice})

        players = sorted(players, key=lambda q:q["points"], reverse=True)
        top_five = int(n*p/100)
        c = collections.Counter([player["name"] for player in players])
        # print(c)
        # print([{player["name"]: player["points"]} for player in players])
        print([{x: c[x]/n} for x in list(c)])
        player_sum = {"T4T": 0, "G": 0, "AC": 0, "AD": 0}
        for player in players:
            player_sum[player["name"]] += player["points"]

        total_sum = player_sum.values()
        print(player_sum)
        print([{player: player_sum[player] / c[player]} for player in c])
        print(f" {gen} ===============")
        # print([{k: v/len(n)} for k, v in list(c)])
        players = players[:-top_five] + players[:top_five]


play_game(100, 5, 5, 20)
