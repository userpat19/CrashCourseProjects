questions = ("What is the primary source of energy for life on Earth?" , 
            "Which gas do plants primarily use during photosynthesis?",
            "What is the chemical formula for water?",
            "Which part of the human brain controls balance and coordination?",
            "What is the process by which cells divide to form two identical daughter cells?")

options = (("A. The Moon", "B. The Sun", "C. Volcanoes", "D. Earth's Core"),
           ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Methane"),
           ("A. H2O", "B. CO2", "C. NaCl", "D. O2"),
           ("A. Cerebrum", "B. Cerebellum", "C. Brainstem", "D. Hypothalamus"),
           ("A. Meiosis", "B. Mitosis", "C. Osmosis", "D. Diffusion"))

answers = ("B" , "B" , "A" , "B" , "B")
guesses = []
score = 0
num_QUESTION = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[num_QUESTION]:
        print(option)
    
    guess = input("Enter (A , B , C , D):").upper()
    guesses.append(guess)
    if guess == answers[num_QUESTION]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer is {answers[num_QUESTION]}")
    num_QUESTION += 1

print("--------------------------")
print("        RESULTS           ")
print("--------------------------")

print("Answers: ", end = "")
for answer in answers:
    print(answer, end=" ")

print()

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end=" ")

print()

average = int(score / len(questions) * 100)

print(f"Your scored {average}%")