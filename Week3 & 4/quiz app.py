import random

def run_quiz():
    score = 0
    total_questions = len(quiz_questions)
    
    questions = quiz_questions.copy()
    random.shuffle(questions)
    
    for question in questions:
        print("\n" + question["question"])
        
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
            
        while True:
            try:
                answer = int(input("\nEnter your choice (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if question["options"][answer-1] == question["correct_answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}")
            
    print(f"\nQuiz completed!")
    print(f"Your final score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.2f}%")

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

choice = input("Do you want to start the quiz? (yes/no): ").strip().lower()
if choice == "yes":
    run_quiz()
