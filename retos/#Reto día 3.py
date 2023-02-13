def play_tennis(points):
    scores = {"P1": 0, "P2": 0}
    score_names = {0: "Love", 1: "15", 2: "30", 3: "40"}
    for point in points:
        scores[point] += 1
        if scores["P1"] >= 4 and scores["P1"] - scores["P2"] >= 2:
            print("Ha ganado el P1")
            return
        elif scores["P2"] >= 4 and scores["P2"] - scores["P1"] >= 2:
            print("Ha ganado el P2")
            return
        elif scores["P1"] >= 4 and scores["P2"] >= 4:
            print("Deuce")
            continue
        else:
            print(score_names[scores["P1"]] + " - " + score_names[scores["P2"]])

points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
play_tennis(points)
