import random
import time

def main():
    # Read the questions and answers from the file
    with open('questions.txt', 'r') as f:
        qa_pairs = [line.strip().split('", "') for line in f]
        qa_pairs = [(q[:-1], a[:-2]) for q, a in qa_pairs]  # strip off extra quotes and commas

    # List of insult responses
    insult_responses = [
        "Wrong! Your answer is so off, it's clear why you're a constant disappointment.",
        "Incorrect! With answers like that, it's no wonder your mother questions her choices.",
        "Nope! Your intelligence seems to be as shallow as a puddle.",
        "False! You couldn't have been more wrong. I bet you still count on your fingers.",
        "That's incorrect! You must be the reason your parents are so disappointed.",
        "Wrong! You wouldn't know the right answer if it hit you in the face.",
        "Nope! I've seen smarter vegetables. At least they know when to be quiet.",
        "Incorrect! I'm surprised you managed to tie your shoes this morning.",
        "False! I’ve seen toddlers make better guesses.",
        "Nope! It's answers like these that give your mother that disappointed look.",
        "Wrong! Do you even have a brain, or are you always this clueless?",
        "Incorrect! Your answer was so bad, it made me want to uninstall myself.",
        "False! It's answers like yours that make people question the education system.",
        "Nope! I bet your high school science teacher is disappointed in you right now.",
        "Wrong! With that kind of logic, I'm surprised you remember how to breathe.",
        "Incorrect! It's no wonder you're the reason for your mother's stress wrinkles.",
        "False! It's clear that you're the personification of an undercooked noodle.",
        "Nope! That's so wrong, even a broken pencil point is sharper than you.",
        "Incorrect! It's clear why people don't ask you for help in trivia games.",
        "False! Even a stopped clock is right twice a day, but not you."
    ]

    # List of passive-aggressive responses for correct answers
    correct_responses = [
        "Well, aren't you a smarty pants? I bet you think you're really clever now.",
        "Correct. How surprising.",
        "Oh, you got it. Do you want a medal or something?",
        "Yes, that's right. Even a broken clock is right twice a day.",
        "Congratulations, you managed to get one right. Your mother must be so proud.",
        "Oh, you got it correct. Must be a lucky guess.",
        "Correct. Even a stopped clock tells the right time twice a day.",
        "Well, you're not as dumb as you look.",
        "You got it right. Did you use Google for that?",
        "Hmm, correct. Maybe you do have a couple of brain cells rubbing together after all."
    ]

    # Choose a random question and answer pair
    question, correct_answer = random.choice(qa_pairs)
    for char in question:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    
    # Get the user's answer
    user_answer = input("> ")
    
    # Check if their answer is correct
    if user_answer.lower() == correct_answer.lower():
        response = random.choice(correct_responses)
    else:
        response = random.choice(insult_responses)
    
    # Print the response, one character at a time
    for char in response:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

if __name__ == "__main__":
    main()
