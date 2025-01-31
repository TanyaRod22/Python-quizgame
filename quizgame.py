questions = [
    {
        "prompt": "Which of the following sorting algorithms can used to sort a random linked list with minimum time complexity?",
        "options": ["A. Insertion sort", "B. Quick sort", "C. Heap sort", "D. Merge sort"],
        "answer": "D"
    },
    {
        "prompt": "What is the average case time complexity of the Bubble sort algorithm?",
        "options": ["A. O(n^2)", "B. O(n log n)", "C. O(n)", "D. O(log n)"],
        "answer": "A"
    },
    {
        "prompt": "What is the best case time complexity of the Quick sort algorithm?",
        "options": ["A. O(n^2)", "B. O(n log n)", "C. O(n)", "D. O(log n)"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following correctly declares an array?",
        "options": ["A. int geeks[20]", "B. int geeks", "C. geeks{20}", "D. array geeks[20]"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, OR D): ")
        if answer.strip().upper() == question["answer"]:
            print("Correct! \n")
            score += 1
        else:
            print("Wrong answer! The correct answer is", question["answer"], "\n")
            
    print(f"You got {score} out of {len(questions)} questions correct")
    
    
run_quiz(questions)