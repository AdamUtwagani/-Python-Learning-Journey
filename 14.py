import random
import os

# Sample Data
data = [
    {'name': 'Instagram', 'followers': 346, 'description': 'Social Media Platform', 'country': 'USA'},
    {'name': 'Cristiano Ronaldo', 'followers': 400, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Diamond Platnumz', 'followers': 10, 'description': 'Musician', 'country': 'Tanzania'},
    {'name': 'Davido', 'followers': 15, 'description': 'Musician', 'country': 'Nigeria'},
    {'name': 'Elon Musk', 'followers': 100, 'description': 'Owner of X', 'country': 'South Africa'},
    {'name': 'MrBeast', 'followers': 250, 'description': 'YouTuber', 'country': 'USA'},
    {'name': 'Ariana Grande', 'followers': 360, 'description': 'Musician/Actress', 'country': 'USA'},
    {'name': 'Neymar Jr', 'followers': 220, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Kylie Jenner', 'followers': 380, 'description': 'Entrepreneur', 'country': 'USA'},
    {'name': 'Shakira', 'followers': 90, 'description': 'Singer', 'country': 'Colombia'}
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(person):
    """Format the data for printing"""
    return f"{person['name']}, a {person['description']} from {person['country']}."

def get_random_choice(exclude=None):
    """Returns a random person not equal to 'exclude'"""
    while True:
        choice = random.choice(data)
        if choice != exclude:
            return choice

def check_guess(guess, a_followers, b_followers):
    """Check if the user's guess is correct"""
    return (guess == 'H' and b_followers > a_followers) or (guess == 'L' and b_followers < a_followers)

# Game Start
score = 0
game_should_continue = True
person_a = get_random_choice()

print("Welcome to the Higher or Lower Game!")

while game_should_continue:
    person_b = get_random_choice(exclude=person_a)

    print(f"\nCompare A: {format_data(person_a)}")
    print("vs")
    print(f"Compare B: {format_data(person_b)}")

    guess = input("Is B has more followers than A? Type 'H' for higher or 'L' for lower: ").upper()

    a_followers = person_a['followers']
    b_followers = person_b['followers']

    is_correct = check_guess(guess, a_followers, b_followers)

    clear_console()

    if is_correct:
        score += 1
        print(f" You're right! Current score: {score}.")
        person_a = person_b
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
