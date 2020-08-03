
import random
while True:
    question = input(("Give me a question: "))

    #user_status = ""

    eightball_choices = {
        "1": "outlook unclear",
        "2": "looks good to me",
        "3": "Its all good",
        "4": "There's no way",
        "5": "Give me a second to think... hard no!",
        "6": "I don't think so..." ,
        "7": "I'd have a beer",
        "8": "You're spare parts bud",
        "9": "Good enough",
        "10": "How're ya now?"
    }

    random_selection = eightball_choices[str(random.randint(1,10))]

    if random_selection == "How're ya now?":
        print(random_selection,end='')
        user_status = input("")
        print("Not so bad")
    else:
        print(random_selection)

    user_input = input("Would you like to ask another question (Y/N)")
    if user_input.upper() != "Y" or "N":
        print("Not an option")
    if user_input.upper() != "Y": break
