# Step 1: Define characters with scores
characters = {
              "Naruto": 0,
              "Luffy": 0,
              "Deku": 0,
              "Goku": 0
              }


# Step 2: Define questions
questions = [
        {
            "question":"What is your favorite power?",
             "options": ["Ninjutsu", "Stretching", "Quirk", "Ki Blast"],
             "score": {"Ninjutsu": "Naruto", "Stretching": "Luffy", "Quirk": "Deku", "Ki Blast": "Goku"}
        },
        {
            "question":"Do you prefer comedy or action?",
            "options": ["Comedy", "Action"],
            "score": {"Comedy": "Luffy", "Action":"Naruto"}
        },
        {
            "question": "Are you brave or smart?",
            "options": ["Brave", "Smart"],
            "score": {"Brave": "Goku", "Smart": "Deku"}

        }
        ]


# Step 3: Function to ask questions
def ask_questions(questions, characters):
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("Enter your choice (1,2,3...): "))
                if 1<= choice <= len(q["options"]):
                    selected_option = q["options"] [choice-1]
                    break # exit loop
                else:
                    print("Invalid choice. Try again!")
            except ValueError:
                print("Please enter a number.")


        if selected_option in q["score"]:
            characters[q["score"][selected_option]] += 1

    return characters

# Step 4: Function to show result
def get_result(characters):
    winner = max(characters, key = characters.get)
    print(f"You are most like: {winner}!")


# Step 5: Run the quiz
characters = ask_questions(questions, characters)
get_result(characters)






