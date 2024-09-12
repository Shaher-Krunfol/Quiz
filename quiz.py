import time

def start_quiz():
    choice = input("Welcome to the ultimate quiz! Please write 'yes' if you want to continue... ").lower()
    
    if choice != "yes":
        quit()
    
    print("Great! The quiz will start in 3 seconds")
    time.sleep(3)

def display_questions_and_get_answers(questions, answers):
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        
        answer = input("Your answer: ").lower()
        
        if answer == answers[i]:
            print("Correct")
            score += 1
        else:
            print(f"Incorrect. The correct answer is '{answers[i]}'.")
        
        print()
    
    return score

def main():
    questions = [
        "What is the name of the process by which bacteria convert nitrogen in the atmosphere into ammonia?",
        "Which physicist is known for the discovery of the neutron in 1932?",
        "What is the term for the phenomenon where the decay rate of a radioactive substance changes based on its temperature?",
        "In the field of computer science, what does the acronym 'KISS' stand for?",
        "What ancient civilization developed the earliest known use of a written script, called cuneiform?"
    ]
    
    answers = [
        "nitrogen fixation",
        "james chadwick",
        "temperature dependence of decay",
        "keep it simple, stupid",
        "sumerian"
    ]

    while True:
        start_quiz()
        score = display_questions_and_get_answers(questions, answers)
        
        print(f"The quiz is over. Your score is {score}/{len(questions)}.")
        option = input("Do you want to retake the quiz? (yes/no) ").lower()
        
        if option != "yes":
            break 

if __name__ == "__main__":
    main()
