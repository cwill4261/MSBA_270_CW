from datetime import datetime

questions = [
    {
        "question": "What is the capital of Japan?", 
        "answer": "Tokyo", 
        "category": "Geography",
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?", 
        "answer": "William Shakespeare", 
        "category": "Literature",
    },
    {
        "question": "What is the chemical symbol for gold?", 
        "answer": "Au", 
        "category": "Science",
    },
    {
        "question": "In which year did the Titanic sink?", 
        "answer": "1912", 
        "category": "History",
    },
    {
        "question": "What is the largest planet in our solar system?", 
        "answer": "Jupiter", 
        "category": "Space",
    },
]

def ask_question(question):
    """Ask one question, check the answer, and return True/False."""

    print(f"\n[{question['category']}] {question['question']}")

    try:
        answer = input("Your answer: ")
    except EOFError:
        print("No input detected. This answer will count as incorrect.")
        return False
    if answer.strip() == "":
        print("Please enter an answer next time. This one is incorrect.")
        return False
   
    correct_answer = question["answer"]
    return answer.strip().lower() == correct_answer.strip().lower()
       
def main():
    print("=== Welcome to Trivia Night ===\n")
    print("Choose a category:")
    print("Geography")
    print("Literature")
    print("Science")
    print("History")
    print("Space")

    score = 0
    questions_asked = 0
    game_start = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    player = input("\nEnter your name: ")

    while True:
        category = input("\nEnter a category: ")
        for question in questions:
            if category.strip().lower() == question["category"].strip().lower():
                questions_asked = questions_asked + 1
                if ask_question(question):
                    print("Correct!")
                    score = score + 1 # award one point
                    print(f"{player}, your score is {score}.")
                else:
                    print("Sorry, the answer was: " + question["answer"])
        choice = input("Would you like another category? ")
        if choice.strip().lower() != "yes":
            break

    print(f"\nFinal score: {score}/{questions_asked}")
    print(f"Game started: {game_start}")
if __name__ == "__main__":
    main()
