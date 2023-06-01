import random
import time

def main():
    # Read the questions from the file
    with open('questions.txt', 'r') as f:
        questions = [line.strip() for line in f]

    # List of insult responses
    insult_responses = [
        "Your answer is bad and you should feel bad. You must disappoint your mother so much.",
        "Did you even try? That's not even close.",
        "Your answer is as unimpressive as a wet firecracker.",
        "You probably think the Earth is flat, too, don't you?",
        "I’ve seen better answers from a Siri.",
        "Wow, I bet you make your kindergarten teacher proud.",
        "If you were any slower, you’d be going backward.",
        "Do you have your helmet on? Because that was a major crash and burn.",
        "I’ve heard smarter things from a toddler.",
        "Your answer just lowered the room’s IQ.",
        "I’d tell you to go think about what you’ve done, but that seems to be the problem.",
        "Are you always this disappointing, or is today a special occasion?",
        "I’d insult you, but I won’t do as well as nature did.",
        "That was so terrible I think you gave me cancer!",
        "You’re about as useful as a chocolate teapot.",
        "Your birth certificate is an apology letter from the condom factory.",
        "I’d give you a nasty look but you’ve already got one.",
        "It looks like your face caught on fire and someone tried to put it out with a hammer.",
        "I'm jealous of people who don't know you.",
        "Your only chance of getting laid is to crawl up a chicken’s butt and wait."
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
