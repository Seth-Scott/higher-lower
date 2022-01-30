import art
import game_data
import random

# performs ranking calcs to establish winner, game logic
def calcs(a, b, a_or_b):
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    if a_followers > b_followers and a_or_b == "a":
        return "win"
    elif b_followers > a_followers and a_or_b == "b":
        return "win"
    else:
        return "lose"

# function that randomly selects an item from game_data (dictionary nested in a list)
def randomizer():
    return game_data.data[random.randint(0,len(game_data.data) -1)]

print(art.logo)

# running score
score = 0
# is the user's first round? 
first_round = True
# are we still in a game or have we lost? 
game = True
# for the first round, sets option "a" to a random selection
option_a = randomizer()

while game:

    # if the user passes the first round, option 'a' is set to the winner of the previous game
    if first_round is False:
        option_a = winner
    option_b = randomizer()

    # if the option 'a' and option 'b' randomly select the same item, re-shuffle item 'b' to a new item
    while option_a == option_b:
        option_b = game_data.data[random.randint(0,len(game_data.data))]

    # "Compare A: item, a widget, from Iraq.""
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")

    print(art.vs)

    #  "Against B: item, a widget, from Iran."
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    #  who has more followers? A or B? 
    user_selection = input("Who has more followers? 'a' or 'b'? ").lower()

    # if you win, increase the score, set option 'a' to the previous round's winner.
    if calcs(option_a, option_b, user_selection) == "win":
        score += 1
        first_round = False
        if user_selection == "a":
            winner = option_a
            loser = option_b
        if user_selection == "b":
            loser = option_a
            winner = option_b 

    # if you lose, you lose
    if calcs(option_a, option_b, user_selection) == "lose":
        print("You LOSE!")
        game = False
        if user_selection == "a":
            loser = option_a
            winner = option_b
        if user_selection == "b":
            winner = option_a 
            loser = option_b

    # print the follower counts and the score
    print(f" SCORE: {score}")
    print(f"{winner['name']}: {winner['follower_count']}: {loser['name']}: {loser['follower_count']} ")
