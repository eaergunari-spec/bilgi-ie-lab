forecast = [32, 28, 24, 16]
rate = [4, 3, 5, 2]

best_score = -1
best_plan = None

for beyo in range(21):
    for sisli in range(21 - beyo):
        for kagithane in range(21 - beyo - sisli):
            besiktas = 20 - beyo - sisli - kagithane
            plan = [beyo, sisli, kagithane, besiktas]

            served = sum(
                min(forecast[i], rate[i] * plan[i])
                for i in range(4)
            )

            if served > best_score:
                best_score = served
                best_plan = plan

print('Best allocation [Beyoglu, Sisli, Kagithane, Besiktas]:', best_plan)
print('Orders served:', best_score)
