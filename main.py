import art
import game_data
import random

def calcs(a, b, a_or_b):
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    if a_followers > b_followers and a_or_b == "a":
        return "win"
    elif b_followers > a_followers and a_or_b == "b":
        return "win"
    else:
        return "lose"



# create function that randomly selects an item from game_data (dictionary nested in a list)
print(art.logo)

score = 0
while True:
    option_a = game_data.data[random.randint(0,len(game_data.data))]
    option_b = game_data.data[random.randint(0,len(game_data.data))]
    while option_a == option_b:
        option_b = game_data.data[random.randint(0,len(game_data.data))]

    # Compare A: item, a widget, from Iraq.
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    # vs. art
    print(art.vs)

    #  Against B: item, a widget, from Iran.
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    #  Who has more followers? A or B? 
    user_selection = input("Who has more followers? 'a' or 'b'? ").lower()

    if calcs(option_a, option_b, user_selection) == "lose":
        print("You LOSE!")
        print(f" SCORE: {score}")
        break
    elif calcs(option_a, option_b, user_selection) == "win":
        score += 1
        print(f" SCORE: {score}")


