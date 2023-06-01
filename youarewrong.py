import json
import random
import time

def main():
    # Read the questions and answers from the file
    with open('questions.json', 'r') as f:
        qa_pairs = json.load(f)

    # List of all answers
    all_answers = [qa['answer'] for qa in qa_pairs]

    # List of insult responses
    insult_responses = [
        "Wrong! Your answer is bad and you should feel bad. This is why your parents are always so disappointed.",
        "Incorrect! Did your brain take a vacation today?",
        "You're wrong again. Does it hurt being this wrong all the time?",
        "Nope! Your lack of knowledge is astonishing.",
        "Wrong! You're the reason this country needs to invest more in education.",
        "Wrong again! You're slower than a herd of snails traveling through peanut butter.",
        "Incorrect! With thinking like that, I now understand why you’re in this situation.",
        "Nope! Your guess was so far off, it's almost impressive.",
        "Wrong! It's astonishing that you can function in society.",
        "Incorrect! I can't believe how incredibly wrong you are.",
        "Wrong! This is why everyone talks about you behind your back.",
        "Nope! Do you even listen to yourself when you speak?",
        "Incorrect! Your wrongness is the stuff of legends.",
        "Wrong! I was hoping for incompetence, but you exceeded even my expectations.",
        "Incorrect! I see the education system has failed you.",
        "Nope! You couldn’t pour water out of a boot if the instructions were on the heel.",
        "Wrong! Your parents must be so proud of you right now.",
        "Incorrect! If I were you, I would have hidden my ignorance a bit better.",
        "Nope! I guess you prove that even god makes mistakes sometimes.",
        "Wrong! I don’t know what makes you so stupid, but it really works."
    ]

    # List of passive-aggressive responses for correct answers
    correct_responses = [
        "Correct! I’m genuinely shocked. You must have guessed.",
        "Right! Well, even a broken clock is right twice a day.",
        "Correct. Don't get too excited, it's just one question.",
        "Wow! You got it. You must have cheated, right?",
        "Correct! This doesn't mean I respect your intelligence.",
        "Oh my! A right answer. Did you ask your smarter friend for help?",
        "Hooray! You got one. Even a blind squirrel finds a nut occasionally.",
        "Correct! I suppose even the sun shines on a dog's rear end some days.",
        "Surprisingly, you're right! I bet you're as shocked as I am.",
        "Wow, you got it! Even a stopped clock is right twice a day.",
        "Right, for once. Don't let it get to your head.",
        "Correct. A miraculous guess, I presume.",
        "Oh, you got one. How quaint.",
        "Finally, a right answer. Was it as painful for you as it was for me?",
        "Correct. A momentary lapse, no doubt.",
        "Right. Don't think this changes my opinion of you.",
        "Congratulations! You managed to stumble upon the correct answer.",
        "I can't believe it, but that's actually correct.",
        "Well done. A fluke, surely.",
        "Even a broken clock is right twice a day, I guess."
    ]

    # List of final responses based on score
    low_score_responses = [
        "Your score is so low, it's no wonder you didn't graduate from high school.",
        "With a score like that, I'm surprised you can tie your own shoes.",
        "I've seen snails with more cognitive prowess than what you've demonstrated here.",
        "Your score is an embarrassment. Even a pigeon would have performed better.",
        "You should consider wearing a helmet at all times."
    ]

    mediocre_score_responses = [
        "You're as mediocre as they come. But hey, at least you're consistent.",
        "Wow, an average score. You must be used to this kind of mediocrity.",
        "Your score is like lukewarm water, neither hot nor cold. Just meh.",
        "Congratulations on being perfectly average. It must be so exciting being you.",
        "Your score is the epitome of mediocrity. I guess that's something?"
    ]

    high_score_responses = [
        "Wow, you look dimmer than a burnt-out lightbulb but you managed to answer most of them right.",
        "Your score is high. I'm as surprised as you are. Did you cheat?",
        "I can't believe you got this many right. You must be having a lucky day.",
        "I'm honestly shocked you managed to get such a high score. No really, I am.",
        "Well aren't you a smarty pants? Now don't let this go to your head."
    ]

    score = 0
    total_questions = 0

    while True:
        # Choose a random question and answer pair
        qa_pair = random.choice(qa_pairs)
        question, correct_answer = qa_pair['question'], qa_pair['answer']

        # Generate multiple-choice answers
        incorrect_answers = random.sample([a for a in all_answers if a != correct_answer], 3)
        options = incorrect_answers + [correct_answer]
        random.shuffle(options)  # Randomize the order of the options

        for char in question:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

        # Print the options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print("5. Exit quiz")

        # Get the user's answer
        user_answer = input("> ")

        # Check if user wants to exit
        if user_answer == "5":
            percentage = (score/total_questions) * 100
            if percentage < 70:
                response = random.choice(low_score_responses)
            elif percentage < 80:
                response = random.choice(mediocre_score_responses)
            else:
                response = random.choice(high_score_responses)
            print(f"Your score: {score}/{total_questions}. {response}")
            break

        # Check if the user's answer is correct
        if options[int(user_answer)-1] == correct_answer:
            print_slow(random.choice(correct_responses))
            score += 1
        else:
            print_slow(random.choice(insult_responses))

def print_slow(str):
    for char in str:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

if __name__ == "__main__":
    main()
