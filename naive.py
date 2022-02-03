"""
a naive wordle solution
Algorithm as follows:
    - guess a random answer from list
    - have user enter feedback
    - filter answer list
    - repeat
"""
from random import randrange

# get the answers as a list
ans_file = open("answers.txt")
answers = ans_file.readlines()
ans_file.close()

# give instruction text
print("key:")
print("_ -> character not found")
print("* -> character in wrong place")
print("+ -> character in right place")


# loop until we've got an answer
for i in range(1, 6):
    guess = answers[randrange(0, len(answers))]
    print("guess {}: {}".format(i, guess))
    feedback = input("result: ")
    if len(feedback) != 6:
        print("error: length must be 6")
        break
    elif feedback.count("_") + feedback.count("*") + feedback.count("+") != 6:
        print("error: must contain only _,+,*")
# we're done... give an answer
if len(answers) == 0:
    print("solution: {}".format(answers))
else:
    print("failed with final candidates: {}".format(answers))
