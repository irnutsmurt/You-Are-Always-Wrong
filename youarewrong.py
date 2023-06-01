import json
import random
import time

def main():
    # Read the questions and answers from the file
    with open('questions.json', 'r') as f:
        qa_pairs = json.load(f)

    # List of all answers
    all_answers = [qa['answer'] for qa in qa_pairs]

    # Read the responses from the file
    with open('responses.json', 'r') as f:
        responses = json.load(f)

    insult_responses = responses['incorrect']
    correct_responses = responses['correct']
    low_score_responses = responses['low_score']
    mediocre_score_responses = responses['medium_score']
    high_score_responses = responses['high_score']

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

        print_slow(f"{qa_pair['topic']}\n{question}")

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
            print_slow(f"Your score: {score}/{total_questions}. {response}")
            break

        total_questions += 1

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
