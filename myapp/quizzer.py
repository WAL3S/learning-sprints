import random, csv, json, atexit


# 1. Load best score
try:
    with open("highscore.json") as f:
        best = json.load(f).get("high_score", 0)
except FileNotFoundError:
    best = 0

# 2. Register save on exit
def save_best_score():
    with open("highscore.json","w") as f:
        json.dump({"high_score": best}, f, indent=2)
atexit.register(save_best_score)

def equalize_string(string):
    string = string.lower()
    cleaned_string=""

    for ch in string:
        if ch.isalnum():
            cleaned_string+=ch
    
    return cleaned_string
    
# 3. Load cards
def make_flashcards():
    cards = []
    with open("Country_Capitals_Flashcards.csv", newline="") as f:
        reader =csv.reader(f)
        next(reader, None)
        for row in reader:
            q, a = row
            cards.append((q.strip(), a.strip()))
    return cards

# 4. Quiz once
def start_quiz(cards):
    score = 0
    for question, answer in cards:
        reply = input(f"The capital of {question} is: ").strip().lower()
        if equalize_string(reply) == equalize_string(answer):
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Sorry, the answer is {answer}")
    return score

def check_proper_input(prompt):
     while True:
        reply = input(prompt).strip().lower()
        if reply and reply[0] in ('y', 'n'):
            return reply[0] == 'y'
        print("Please enter 'Y' or 'N'")

# 5. Main flow
def main():
    global best
    stay = True
    cards = make_flashcards()
    random.shuffle(cards)           # shuffle up-front

    while True:
        score = start_quiz(cards)
        if score > best:
            best = score
            print(f"🎉 New high score: {best}/{len(cards)}")
        else:
            print(f"High score: {best}/{len(cards)}  You scored: {score}/{len(cards)}")

        if check_proper_input("Play again? (Y/N): "):
            if check_proper_input("Reshuffle cards? (Y/N): "):
                random.shuffle(cards)
                print("Cards reshuffled!")
        else:
            print('Thanks for playing!')
            break
        

if __name__ == "__main__":
    main()

