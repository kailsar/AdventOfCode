from itertools import cycle

counter = 1
players = 459
last_marble = 7132000
player_totals = []
player_numbers = []
play_state = [0]
element_in_play = 0
for x in range(players):
    player_totals.append(0)
    player_numbers.append(x)
active_player = cycle(player_numbers)

while counter <= last_marble:
    if counter % 23 == 0:
        player_index = next(active_player)
        player_totals[player_index] += counter
        for x in range(7):
            element_in_play -= 1
            if element_in_play < 0:
                element_in_play = len(play_state) - 1
        player_totals[player_index] += play_state.pop(element_in_play)
        counter += 1
    else:
        element_in_play += 1
        if element_in_play >= len(play_state):
            element_in_play = 0
        element_in_play += 1
        play_state.insert(element_in_play, counter)
        counter += 1
        next(active_player)

print(max(player_totals))
    


