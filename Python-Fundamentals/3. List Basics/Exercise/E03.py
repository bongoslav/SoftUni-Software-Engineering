team_a = ["A-" + str(i) for i in range(1, 12)]
team_b = ["B-" + str(i) for i in range(1, 12)]
game_is_terminated = False

sent_off_players = input().split()
for player in sent_off_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_terminated:
    print("Game was terminated")