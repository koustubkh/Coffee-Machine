
from art import logo,vs
from game_data import data
import random


from game_data import data
import random

def data_format (account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    print(f"name:{account_name} \n",f"description:{account_description}\n",f"country:{account_country}")

def answer_check (choice,a_follower,b_follower):
    if a_follower > b_follower:
        return choice == "a"
    else:
        return choice == "b"
print(logo)
level = 0
continue_should =  True

while continue_should:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A  : {data_format(account_a)}")
    print(vs)
    print(f"compare B  : {data_format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    print("\n" * 20)
    print(logo)


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = answer_check(guess, a_follower_count, b_follower_count)

    if is_correct:
        level += 1
        print(f"You're right! Current score {level}")
    else:
        print(f"Sorry, that's wrong. Final score: {level}.")
        game_should_continue = False

