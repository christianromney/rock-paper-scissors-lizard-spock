#!/usr/bin/env python3
import readline, re, random

def read_choice():
    "Prompts the user to input a choice or quit. Will keep asking until it gets valid input."
    while True:
        user_choice = input("Choose: (r)ock (p)aper (s)cissors (l)izard spoc(k) (q)uit >>> ")
        mapping = {"r": "rock", "p": "paper", "s": "scissors", "l": "lizard", "k": "spock"}
        match = re.match(r'^(r(ock)?|p(aper)?|s(cissors)?|l(izard)?|(spoc)?k|q(uit)?)$', user_choice)
        if match is None:
            print("Invalid choice, try again.")
        elif match.group(1) in ('q', 'quit'):
            raise Exception("User quit game.")
        elif match.group(1) in mapping:
            return mapping[match.group(1)]
        else:
            return match.group(1)

def evaluate(choices, user, computer):
    "Scores the battle between user and computer."
    user_idx = choices.index(user)
    comp_idx = choices.index(computer)
    #        rock                paper              scissors            lizard              spock
    score = [[(0,  "" ),         (-1, "covers"),    (1,  "smashes"),    (1,  "crushes"),    (-1, "vaporizes")], # rock
             [(-1, "covers"),    (0,  ""),          (-1, "cut"),        (-1, "eats"),       (1,  "disproves")], # paper
             [(-1, "crushes"),   (1,  "cut"),       (0,  ""),           (1,  "decapitate"), (-1, "smashes")],   # scissors
             [(-1, "crushes"),   (1,  "eats"),      (-1, "decapitate"), (0,  ""),           (1,  "poisons")],   # lizard
             [(1,  "vaporizes"), (-1, "disproves"), (1,  "smashes"),    (-1, "poisons"),    (0,  "")]]          # spock
    return score[user_idx][comp_idx]

def human_readable(outcome):
    "Returns a human-readable message format string for the outcome."
    format_string = {
        -1: "Loss! Computer's {2} {1} your {0}.",
        0:  "Tie! You and the computer each chose '{0}'.",
        1:  "Win! Your {0} {1} computer's {2}."
    }
    return format_string[outcome]

def print_results(user, computer, results):
    "Prints the outcome to the screen."
    (outcome, verb) = results
    print(human_readable(outcome).format(user.capitalize(), verb, computer.capitalize()), end="\n\n")
    
def repl(choices):
    "Runs the game loop continuously until quit."
    try:
        while True:  # loop
            user     = read_choice() # read
            computer = random.choice(choices)
            results  = evaluate(choices, user, computer) # eval
            print_results(user, computer, results) # print
    except Exception as e:
        print(e, "Goodbye!")

def play():
    "Prints a welcome message and starts the game loop."
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    print("Welcome to " + ", ".join([s.capitalize() for s in choices]) + "!", end="\n\n")
    repl(choices)

# When run from the command line 
if __name__ == "__main__":
    play()
