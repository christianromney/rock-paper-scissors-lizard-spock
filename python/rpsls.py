#!/usr/bin/env python3
import readline, re, secrets

LONG_CHOICES  = ('rock', 'paper', 'scissors', 'lizard', 'spock')
SHORT_CHOICES = ("r", "p", "s", "l", "k")
SHORT_TO_LONG = dict(zip(SHORT_CHOICES, LONG_CHOICES))

def validate_choice(user_choice):
    "Validates an input value as one of the game options."
    match = re.match(r'^(r(ock)?|p(aper)?|s(cissors)?|l(izard)?|(spoc)?k|q(uit)?)$', user_choice)
    if match is None:
        return match
    elif match.group(1) in ('q', 'quit'):
        raise Exception("User quit game.")
    elif match.group(1) in SHORT_CHOICES:
        return SHORT_TO_LONG[match.group(1)]
    else:
        return match.group(1)

def evaluate(user, computer):
    "Scores the battle between user and computer."
    user_idx = LONG_CHOICES.index(user)
    comp_idx = LONG_CHOICES.index(computer)
    #        rock                paper              scissors            lizard              spock
    score = [[(0,  "" ),         (-1, "covers"),    (1,  "smashes"),    (1,  "crushes"),    (-1, "vaporizes")], # rock
             [(-1, "covers"),    (0,  ""),          (-1, "cut"),        (-1, "eats"),       (1,  "disproves")], # paper
             [(-1, "crushes"),   (1,  "cut"),       (0,  ""),           (1,  "decapitate"), (-1, "smashes")],   # scissors
             [(-1, "crushes"),   (1,  "eats"),      (-1, "decapitate"), (0,  ""),           (1,  "poisons")],   # lizard
             [(1,  "vaporizes"), (-1, "disproves"), (1,  "smashes"),    (-1, "poisons"),    (0,  "")]]          # spock
    return score[user_idx][comp_idx]

def format_results(user, computer, results):
    "Formats the outcome for printing to the screen."
    (outcome, verb) = results
    human_readable = {
        -1: "Loss! Computer's {2} {1} your {0}.",
         0: "Tie! You and the computer each chose '{0}'.",
         1: "Win! Your {0} {1} computer's {2}."
    }
    return human_readable[outcome].format(user.capitalize(), verb, computer.capitalize())

def read_choice():
    "Prompts the user to input a choice or quit. Will keep asking until it gets valid input."
    while True:
        user_choice = input("Choose: (r)ock (p)aper (s)cissors (l)izard spoc(k) (q)uit >>> ")
        valid = validate_choice(user_choice)
        if valid is None:
            print("Invalid choice, try again.")
            continue
        return valid

def play():
    "Runs the game REPL continuously until quit."
    try:
        print("Welcome to " + ", ".join([s.capitalize() for s in LONG_CHOICES]) + "!", end="\n\n")
        while True:  # loop
            user     = read_choice() # read
            computer = secrets.choice(LONG_CHOICES)
            results  = evaluate(user, computer)  # eval
            print(format_results(user, computer, results), end="\n\n") # print
    except Exception as e:
        print(e, "Goodbye!")

 # When run from the command line
if __name__ == "__main__":
    play()
