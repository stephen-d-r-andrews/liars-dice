import random

from action_functions import get_action_1, get_action_2, check_stronger, get_strongest


count = ["one", "two", "three", "four"]
numbers = [1, 2, 3, 4, 5, 6]

player_turn = 1
rejecting_player = 0

history = [[], []]
claim = None

def run_game():
    p1_hand = [random.randint(1,6), random.randint(1,6)]
    p2_hand = [random.randint(1,6), random.randint(1,6)]

    while claim != "reject":
        if player_turn == 1:
            next_action = get_action_1(history, p1_hand)

            if next_action == "reject":
                rejecting_player = 1
                final_claim = claim
            claim = next_action

            history[0].append(claim)
            player_turn = 2

        elif player_turn == 2:
            next_action = get_action_2(history, p2_hand)

            if next_action == "reject":
                rejecting_player = 2
                final_claim = claim
            claim = next_action

            history[1].append(claim)
            player_turn = 1

    strongest_claim = get_strongest(p1_hand, p2_hand)
    
    check_stronger(final_claim, strongest_claim)


def main():
    run_game()

if __name__ == "__main__":
    main()


