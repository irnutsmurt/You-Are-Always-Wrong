import random
import time

def main():
    # Read the questions from the file
    with open('questions.txt', 'r') as f:
        questions = [line.strip() for line in f]

    # List of insult responses
    insult_responses = [
        "Wrong! Your answer is bad and you should feel bad. You must disappoint your mother so much.",
        "Incorrect! Did you even try? That's not even close.",
        "Nope! Your answer is as unimpressive as a wet firecracker.",
        "You're wrong! You probably think the Earth is flat, too, don't you?",
        "That's not right! I’ve seen better answers from a Siri.",
        "False! Wow, I bet you make your kindergarten teacher proud.",
        "Incorrect! If you were any slower, you’d be going backward.",
        "Wrong answer! Do you have your helmet on? Because that was a major crash and burn.",
        "Nope! I’ve heard smarter things from a toddler.",
        "Incorrect! Your answer just lowered the room’s IQ.",
        "Wrong! I’d tell you to go think about what you’ve done, but that seems to be the problem.",
        "Nope! Are you always this disappointing, or is today a special occasion?",
        "Incorrect! I’d insult you, but I won’t do as well as nature did.",
        "False! That was so terrible I think you gave me cancer!",
        "Wrong answer! You’re about as useful as a chocolate teapot.",
        "Nope! Your birth certificate is an apology letter from the condom factory.",
        "Incorrect! I’d give you a nasty look but you’ve already got one.",
        "Wrong! It looks like your face caught on fire and someone tried to put it out with a hammer.",
        "False! I'm jealous of people who don't know you.",
        "Wrong answer! Your only chance of getting laid is to crawl up a chicken’s butt and wait."
    ]


    question = random.choice(questions)
    for character in question:
        print(character, end='', flush=True)
        time.sleep(0.05)
    print()
    
    answer = input('Your answer: ')
    
    response = random.choice(insult_responses)
    for character in response:
        print(character, end='', flush=True)
        time.sleep(0.05)
    print()

if __name__ == "__main__":
    main()
