
def flashcard():
    answer = input(prompt)
    if answer.lower() == cards:
        print("Correct!")
    else:
        print("Sorry, that is wrong....")

def read_cards(filename):
    cards = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split(",")
            cards[parts[1]] = parts[0]
    return cards

cards = read_cards("capitals-all.txt")
count_right = 0

cards = {
    'Capital' : 'State'
}

for prompt, answer in cards.items():
    flashcard(prompt, answer)

user_entry = input("what is the capital of " + prompt + "?")


prompt = "What is the capital of Arkansas? "
flashcard()
prompt = "What is the capital of Montana? "
flashcard()
prompt = "What is the capital of North Dakota? "
flashcard()
prompt = "What is the capital of Wyoming? "
flashcard()