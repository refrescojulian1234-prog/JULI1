import random
import time

def create_question(min_num, max_num):
    """
    Creates a random maths question with numbers between min_num and max_num.
    
    Parameters:
    min_num (int): The smallest number to use in the question
    max_num (int): The largest number to use in the question
    
    Returns:
    str: A string representing the maths question
    """
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(['+', '-'])
    return f"{num1} {operator} {num2}"

def ask_question(question):
    """
    Asks the user a question and records their response time.
    
    Parameters:
    question (str): The question to ask the user
    
    Returns:
    tuple: (boolean, int) representing correctness and time taken in seconds
    """
    start_time = time.time()
    try:
        user_answer = int(input(f"{question} = "))
    except ValueError:
        user_answer = None  # Will be marked as incorrect
    end_time = time.time()
    
    time_taken = int(end_time - start_time)
    
    try:
        correct_answer = eval(question)
        is_correct = user_answer == correct_answer
    except:
        is_correct = False
        
    return (is_correct, time_taken)

def main():
    # Welcome message
    print("Welcome to Julian's Maths Test Program !")
    print("Test your addition and subtraction skills.")
    print()
    
    # Difficulty selection
    difficulties = {
        '1': ('easy', 5, 10),
        'e': ('easy', 5, 10),
        'easy': ('easy', 5, 10),
        '2': ('medium', 10, 20),
        'm': ('medium', 10, 20),
        'medium': ('medium', 10, 20),
        '3': ('hard', 15, 50),
        'h': ('hard', 15, 50),
        'hard': ('hard', 15, 50)
    }
    
    while True:
        choice = input("Choose difficulty (1-Easy, 2-Medium, 3-Hard): ").lower().strip()
        if choice in difficulties:
            difficulty, questions, max_num = difficulties[choice]
            print(f"You selected {difficulty.capitalize()} difficulty.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    print(f"The test will have {questions} questions.")
    print()
    
    # Initialize variables for the test
    score = 0
    correct_answers = []
    response_times = []
    questions_list = []
    
    # Administer the test
    for i in range(1, questions + 1):
        print(f"Score: {score} | Question {i} of {questions}")
        
        # Determine the range for numbers in this question
        if i == questions:  # Challenge question
            print("Challenge question!")
            min_range = max_num
            max_range = max_num * 2
        else:
            min_range = max_num // 2
            max_range = max_num
        
        # Create and ask the question
        question = create_question(min_range, max_range)
        questions_list.append(question)
        is_correct, time_taken = ask_question(question)
        
        # Process the response
        if is_correct:
            points = max(1, 10 - time_taken)
            score += points
            print(f"Correct! You took {time_taken} second{'s' if time_taken != 1 else ''} and earned {points} point{'s' if points != 1 else ''}.")
        else:
            print(f"Incorrect! You took {time_taken} second{'s' if time_taken != 1 else ''} and earned 0 points.")
        
        correct_answers.append(is_correct)
        response_times.append(time_taken)
        print()
    
    # Calculate results
    correct_count = sum(correct_answers)
    correct_percentage = round((correct_count / questions) * 100)
    avg_response_time = round(sum(response_times) / questions)
    
    # Display results
    print("=" * 40)
    print("TEST RESULTS")
    print("=" * 40)
    print(f"Final Score: {score}")
    print(f"Correct Answers: {correct_count}/{questions} ({correct_percentage}%)")
    print(f"Average Response Time: {avg_response_time} seconds")
    print()
    
    # Question breakdown table
    print("Question Breakdown:")
    print("-" * 40)
    print(f"{'Question':<10} {'Correct':<8} {'Time':>8}")
    print("-" * 40)
    for i, (correct, time_taken) in enumerate(zip(correct_answers, response_times), 1):
        status = "YES" if correct else "NO"
        print(f"Q{i:<9} {status:<8} {time_taken:>7}s")
    print("-" * 40)

if __name__ == "__main__":
    main()
