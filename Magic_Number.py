teams = int(input("Number of trailing teams: ", ))
lwins = int(input("Leading number of wins: ", ))
for teams in range(1, teams + 1, 1):
    losses = int(input("How many times did the team lose? "))
    games = 162
    mnumber = int(games) - int(lwins) - int(losses) + 1
    if mnumber < 0:
        print("Elininated from playoff contention")
    else:
        print("Magic number is: ", mnumber)
