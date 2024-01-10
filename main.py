from game_data import data
from art import logo, vs
import random




def compare(A, B, guess,):
    if  A['follower_count'] > B['follower_count']:
         return guess == "A"
      
    else:
        return guess=="B"

B=random.choice(data)
score = 0
is_continue=True

while is_continue:   
    A=B
    B=random.choice(data)
    if A==B:
        B=random.choice(data)
    print(logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B':").upper()

    
    is_correct = compare(A,B,guess)

    if is_correct:
        score=score+1
        print(f"You're right! Current score: {score}.")
    

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_continue=False