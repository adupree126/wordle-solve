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
answers = [s[:-1] for s in ans_file.readlines()]
ans_file.close()

# give instruction text
print("key:")
print("_ -> character not found")
print("* -> character in wrong place")
print("+ -> character in right place")


# loop until we've got an answer
for i in range(1, 7):
    guess = answers[randrange(0, len(answers))]
    if len(answers) > 10:
        print("contains shard: {}".format(answers.count("shard") == 1))
    print("guess {} (answers left: {}): {}".format(i, len(answers), guess))
    feedback = input("result: ")
    # error check
    if len(feedback) != 5:
        print("error: length must be 5")
        break
    elif feedback.count("_") + feedback.count("*") + feedback.count("+") != 5:
        print("error: must contain only _,+,*")
    # filter out answers
    for j in range(5):
        char = guess[j]
        expected = sum([1 if "+*".count(feedback[i]) != 0 and guess[i] == char else 0
                        for i in range(5)])
        if feedback[j] == "_":
            answers = list(
                filter(lambda s: s.count(char) == expected, answers))
        elif feedback[j] == "*":
            answers = list(filter(lambda s: s.count(char) == expected
                                  and s[j] != char, answers))
        elif feedback[j] == "+":
            answers = list(filter(lambda s: s[j] == char, answers))

# we're done... give an answer
if len(answers) == 0:
    print("solution: {}".format(answers))
else:
    print("failed with final candidates: {}".format(answers))
