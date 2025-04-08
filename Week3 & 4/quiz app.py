"""Quiz app"""
import random

def quiz():
    score = 0
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["90", "95", "100", "105"],
            "correct_answer": "100"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Ernest Hemingway", "Harper Lee", "Mark Twain", "John Steinbeck"],
            "correct_answer": "Harper Lee"
        }
    ]


    random_question = quiz_questions.copy()
    # print(random_question)
    random.shuffle(random_question)


    for questions in random_question:
        print(questions["question"])

        for i, option in enumerate(questions["options"], start=1):
            print(f"{i}. {option}")

        answer = input("what is the correct answer ? \nWrite out the answer")

        if answer == questions["correct_answer"]:
            print("Correct")
            score += 1
        else:
            print("Na u are wrong")
    print(f"You got {score}/ {len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f"Percentage: {percentage:.2f}%")


    # print(random_question["question"])
    # print(random_question["options"])
    # print(random_question["correct_answer"])

quiz()
while True:
    promot = input("Would you like to begin the quiz game: y or n: ").strip().lower()
    if promot == "y":
        quiz()
