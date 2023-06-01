import random
import time

def main():
    # Read the questions from the file
    with open('questions.txt', 'r') as f:
        questions = [line.strip() for line in f]

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
        "False! Even a stopped clock is right twice a day, but not you.",
        "Nope! You're like the end pieces of a loaf of bread. Everyone touches you, but nobody wants you.",
        "Wrong! I can't believe you'd get something so simple incorrect. What would your mother say?"
    ]



    question = random.choice(questions)
    for character in question:
        print(character, end='', flush=True)
        time.sleep(0.01) #adjust number for the text to print slower or faster
    print()
    
    answer = input('Your answer: ')
    
    response = random.choice(insult_responses)
    for character in response:
        print(character, end='', flush=True)
        time.sleep(0.01) #adjust number for the text to print slower or faster
    print()

if __name__ == "__main__":
    main()
