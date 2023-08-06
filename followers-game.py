import game_data
import random
data = game_data.data
status = "Continue"
score = 0

def generate(data):
    character = random.choice(data)
    
    return character

def printing(character):
    for category in character:
        category_data = character[category]
        
        if category == "name":
            name = category_data
        elif category == "description":
            description = category_data
        else:
            country = category_data
        
    print(f"{name}, a {description} from {country}")

def the_answer(ans_user,character_1,character_2):
    winner_name = ""
    
    name_1 = character_1["name"]
    followers_1 = character_1["follower_count"]
    
    name_2 = character_2["name"]
    followers_2 = character_2["follower_count"]
    
    if followers_1 > followers_2:
        winner_name = name_1
    else:
        winner_name = name_2
        
    return winner_name

def winner_choosing(winner_name):
    for character in data:
        if winner_name == character["name"]:
            winner = character
            
    return winner

def compare(ans_user,winner_name):
    if ans_user == winner_name:
        status = "Continue"
    else:
        status = "Exit"
        
    return status

print("--------------------------")
print("Welcome to the Higher or Lower Game!")
print("")


if status == "Continue":
    character_1 = generate(data)
    printing(character_1)

while status == "Continue":
    print("")
    print("Versus")
    print("")

    character_2 = generate(data)
    while character_2 == character_1:
        character_2 = generate(data)
        
    printing(character_2)

    ans_user = input("Who has a higher follower count? (Full name): ")
    print("")
    winner_name = the_answer(ans_user,character_1,character_2)
    winner = winner_choosing(winner_name)
    
    if ans_user == winner_name:
        score = score + 1
        print("-------------")
        print(f"Correct! Current score: {score}")
    
    character_1 = winner
    printing(character_1)
    
    status = compare(ans_user,winner_name)
    
if status == "Exit":
    print("Has the higher follower count")
    print("")
    print(f"Final score: {score}")